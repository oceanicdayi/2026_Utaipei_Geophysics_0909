# -*- coding: utf-8 -*-
"""資料品質檢核：訊噪比與互換時間（reciprocity）。"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from obspy import Stream, Trace

from .config import DEFAULT_SURVEY, Survey


def _window_rms(trace: Trace, start: float, end: float) -> float:
    """取 [start, end) 秒區間的 RMS 振幅。"""
    i0 = max(0, int(start / trace.stats.delta))
    i1 = min(trace.stats.npts, int(end / trace.stats.delta))
    if i1 <= i0:
        raise ValueError(f"視窗 [{start}, {end}) s 超出紀錄長度")
    segment = trace.data[i0:i1]
    return float(np.sqrt(np.mean(segment.astype(float) ** 2)))


def trace_snr(trace: Trace, survey: Survey = DEFAULT_SURVEY) -> float:
    """單道訊噪比 (dB)。

    訊號 = 早期視窗（預設 0-0.2 s）的最大絕對振幅；
    雜訊 = 末端視窗（預設 0.40-0.50 s，訊號早已過去）的 RMS。
    兩者相除再取 20log10。
    """
    i0 = int(survey.signal_window[0] / trace.stats.delta)
    i1 = min(trace.stats.npts, int(survey.signal_window[1] / trace.stats.delta))
    signal = float(np.abs(trace.data[i0:i1]).max())
    noise = _window_rms(trace, *survey.noise_window)
    if noise <= 0:
        return float("inf")
    return 20.0 * np.log10(signal / noise)


def stream_snr(stream: Stream, survey: Survey = DEFAULT_SURVEY) -> np.ndarray:
    """整個 Stream 每一道的訊噪比 (dB)，順序與 Stream 相同。"""
    return np.array([trace_snr(tr, survey) for tr in stream])


def snr_by_offset(stream: Stream, bin_width: float = 4.0,
                  survey: Survey = DEFAULT_SURVEY) -> list[tuple[float, float, int]]:
    """依支距分組統計訊噪比中位數。

    回傳 [(分組中心 m, 中位數 dB, 道數), ...]。
    """
    if bin_width <= 0:
        raise ValueError("bin_width 必須為正數")
    snr = stream_snr(stream, survey)
    offsets = np.array([tr.stats.utels.abs_offset for tr in stream])

    out = []
    edges = np.arange(0, offsets.max() + bin_width, bin_width)
    for lo in edges:
        mask = (offsets >= lo) & (offsets < lo + bin_width)
        if mask.any():
            out.append((float(lo + bin_width / 2),
                        float(np.median(snr[mask])), int(mask.sum())))
    return out


@dataclass(frozen=True)
class ReciprocalPair:
    """一組互換配對：A 打 B 與 B 打 A。"""

    x_a: float
    x_b: float
    t_ab: float      # s
    t_ba: float      # s

    @property
    def difference(self) -> float:
        """互換時間差的絕對值 (s)。理論上應為 0。"""
        return abs(self.t_ab - self.t_ba)


def reciprocal_pairs(picks: dict[tuple[float, float], float],
                     tolerance: float = 0.01) -> list[ReciprocalPair]:
    """從挑選結果中找出互換配對。

    `picks` 的鍵是 (炮點座標, 受波器座標)，值是到時 (s)。
    互換時間是折射震測最重要的自我檢核：震波路徑可逆，所以
    「A 點打、B 點收」與「B 點打、A 點收」的總走時必須相同。
    差太多就代表其中一個到時挑錯了，或幾何記錄有誤。

    `tolerance` 是座標比對的容許誤差 (m)。
    """
    out = []
    for (sx, gx), t_ab in picks.items():
        if sx >= gx:
            continue  # 每組只取一次，避免重複
        for (sx2, gx2), t_ba in picks.items():
            if abs(sx2 - gx) <= tolerance and abs(gx2 - sx) <= tolerance:
                out.append(ReciprocalPair(sx, gx, t_ab, t_ba))
                break
    return out

def ground_roll_velocity(stream: Stream, min_offset: float = 10.0,
                         tmax: float = 0.30) -> float:
    """估計表面波（ground roll）的視速度 (m/s)。

    表面波是本資料中能量最強的訊號。取每道最大振幅出現的時間，
    對支距做線性擬合，斜率的倒數就是它的視速度。

    知道這個數字很重要：初達波挑選的搜尋視窗下限必須高於它，
    否則自動程式會挑到表面波而不是初達波。
    """
    offsets, peak_times = [], []
    for tr in stream:
        offset = tr.stats.utels.abs_offset
        if offset < min_offset:
            continue
        n = min(tr.stats.npts, int(tmax / tr.stats.delta))
        peak_times.append(int(np.argmax(np.abs(tr.data[:n]))) * tr.stats.delta)
        offsets.append(offset)

    if len(offsets) < 3:
        raise ValueError(f"支距 >= {min_offset} m 的道數不足，無法估計表面波速度")

    slope, _ = np.polyfit(np.asarray(offsets), np.asarray(peak_times), 1)
    if slope <= 0:
        raise ValueError("擬合斜率非正值，無法換算成速度")
    return float(1.0 / slope)
