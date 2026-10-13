# -*- coding: utf-8 -*-
"""前處理：去趨勢、帶通濾波、AGC、歸一化。

所有函式都回傳**新的** Stream／陣列，不會動到傳入的資料。
"""
from __future__ import annotations

import numpy as np
from obspy import Stream

from .config import DEFAULT_SURVEY, Survey


def bandpass(stream: Stream, freqmin: float | None = None,
             freqmax: float | None = None, corners: int = 4,
             survey: Survey = DEFAULT_SURVEY) -> Stream:
    """帶通濾波（零相位）。

    本次資料未做任何儀器端濾波，低頻（2-16 Hz）漂移與 20-40 Hz 的
    表面波能量都很強。預設 40-400 Hz 可壓低這兩者，凸顯初達 P 波。

    零相位（``zerophase=True``）很重要：單向濾波會讓波形延遲，
    直接污染到時判讀。
    """
    freqmin = freqmin if freqmin is not None else survey.bandpass_low
    freqmax = freqmax if freqmax is not None else survey.bandpass_high
    nyquist = stream[0].stats.sampling_rate / 2.0
    if not 0 < freqmin < freqmax < nyquist:
        raise ValueError(
            f"濾波頻帶不合法：需滿足 0 < {freqmin} < {freqmax} < {nyquist} Hz")

    out = stream.copy()
    out.detrend("demean")
    out.detrend("linear")
    out.filter("bandpass", freqmin=freqmin, freqmax=freqmax,
               corners=corners, zerophase=True)
    return out


def agc(data: np.ndarray, window_samples: int = 80,
        floor_ratio: float = 0.02) -> np.ndarray:
    """自動增益控制：以滑動視窗的平均絕對振幅做歸一化。

    遠支距振幅只有近支距的幾十分之一，不做 AGC 的話，遠道在圖上
    會是一條直線。`floor_ratio` 防止安靜段被放大成純雜訊。
    """
    if window_samples < 2:
        raise ValueError("AGC 視窗至少要 2 個樣本")
    data = np.asarray(data, dtype=float)
    envelope = np.convolve(np.abs(data), np.ones(window_samples) / window_samples,
                           mode="same")
    floor = envelope.max() * floor_ratio
    return data / np.maximum(envelope, max(floor, 1e-20))


def normalise(data: np.ndarray, window: slice | None = None) -> np.ndarray:
    """把波形除以（指定視窗內的）最大絕對值，使尖峰為 1。"""
    data = np.asarray(data, dtype=float)
    reference = data if window is None else data[window]
    peak = np.abs(reference).max()
    return data / peak if peak > 0 else data.copy()


def time_axis(trace) -> np.ndarray:
    """回傳該道的時間軸 (s)。"""
    return np.arange(trace.stats.npts) * trace.stats.delta
