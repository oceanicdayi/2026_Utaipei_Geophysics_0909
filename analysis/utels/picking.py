# -*- coding: utf-8 -*-
"""初達波（first break）自動挑選。

本測線的難點：能量最強的不是初達 P 波，而是視速度僅約 127 m/s 的
表面波（ground roll）。任何只看「最大能量」的演算法都會挑到它。
因此這裡的策略是：

1. 先用視速度把搜尋範圍限制在一個物理上合理的時間視窗；
   下限 180 m/s 刻意高於表面波，直接把表面波排除在視窗外。
2. 在該視窗內用 AIC（Akaike Information Criterion）找最佳分割點，
   也就是「雜訊段」與「訊號段」統計性質差異最大的位置。

務必記得：自動挑選只是**基線**，不是答案。訊噪比低的道一定要人工覆核。
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from obspy import Stream, Trace

from .config import DEFAULT_SURVEY, Survey
from .quality import trace_snr


@dataclass(frozen=True)
class Pick:
    """單道的初達波挑選結果。"""

    ffid: int
    channel: int
    shot_x: float
    receiver_x: float
    offset: float      # 帶正負號 (m)
    time: float        # 到時 (s)
    snr: float         # 訊噪比 (dB)

    @property
    def abs_offset(self) -> float:
        return abs(self.offset)

    @property
    def apparent_velocity(self) -> float:
        """該道的視速度 (m/s)，到時為 0 時回傳 inf。"""
        return self.abs_offset / self.time if self.time > 0 else float("inf")

    @property
    def reliable(self) -> bool:
        return self.snr >= DEFAULT_SURVEY.snr_threshold_db


def aic_pick(data: np.ndarray, i0: int, i1: int) -> int:
    """在 [i0, i1) 範圍內用 AIC 找訊號起始樣本。

    AIC(k) = k·ln(var(x[:k])) + (n-k-1)·ln(var(x[k:]))
    最小值出現在「前段變異數小、後段變異數大」的交界，也就是初達位置。
    """
    i0 = max(0, int(i0))
    i1 = min(len(data), int(i1))
    segment = np.asarray(data[i0:i1], dtype=float)
    n = len(segment)
    if n < 12:
        return i0  # 視窗太短，無法可靠分割

    aic = np.full(n, np.inf)
    for k in range(3, n - 3):
        var_before = segment[:k].var()
        var_after = segment[k:].var()
        if var_before > 0 and var_after > 0:
            aic[k] = k * np.log(var_before) + (n - k - 1) * np.log(var_after)
    if not np.isfinite(aic).any():
        return i0
    return i0 + int(np.argmin(aic))


def sta_lta(data: np.ndarray, n_sta: int, n_lta: int) -> np.ndarray:
    """因果型 STA/LTA：在樣本 i，STA 取 [i-n_sta, i)，LTA 取 [i-n_lta, i)。

    這裡保留此函式供教學比較之用；正式挑選使用 AIC，因為 STA/LTA
    對本資料的表面波太敏感。
    """
    if not 0 < n_sta < n_lta:
        raise ValueError("需滿足 0 < n_sta < n_lta")
    energy = np.asarray(data, dtype=float) ** 2
    cumulative = np.concatenate([[0.0], np.cumsum(energy)])
    out = np.zeros(len(data))
    idx = np.arange(n_lta, len(data))
    sta = (cumulative[idx] - cumulative[idx - n_sta]) / n_sta
    lta = (cumulative[idx] - cumulative[idx - n_lta]) / n_lta
    out[idx] = sta / np.maximum(lta, 1e-20)
    return out


def pick_trace(trace: Trace, survey: Survey = DEFAULT_SURVEY) -> Pick:
    """挑選單道的初達波。假設 trace 已做過帶通濾波。"""
    geom = trace.stats.utels
    offset = abs(geom.offset)
    snr = trace_snr(trace, survey)

    if offset == 0:
        time = 0.0  # 零支距：受波器就在炮點上，到時定義為 0
    else:
        delta = trace.stats.delta
        i_min = max(4, int(offset / survey.vel_search_max / delta))
        i_max = min(trace.stats.npts - 1,
                    int(offset / survey.vel_search_min / delta))
        if i_max <= i_min:
            raise ValueError(
                f"支距 {offset} m 的搜尋視窗為空，請檢查 vel_search_* 設定")
        time = aic_pick(trace.data, i_min, i_max) * delta

    return Pick(ffid=geom.ffid, channel=geom.channel, shot_x=geom.shot_x,
                receiver_x=geom.receiver_x, offset=geom.offset,
                time=float(time), snr=float(snr))


def pick_stream(stream: Stream, survey: Survey = DEFAULT_SURVEY) -> list[Pick]:
    """挑選整個 Stream，回傳 Pick 清單（順序與 Stream 相同）。"""
    return [pick_trace(tr, survey) for tr in stream]


def reliable_picks(picks: list[Pick],
                   survey: Survey = DEFAULT_SURVEY) -> list[Pick]:
    """只保留訊噪比足夠、且支距大於 0 的挑選結果。"""
    return [p for p in picks
            if p.snr >= survey.snr_threshold_db and p.abs_offset > 0]


def bin_picks(picks: list[Pick], bin_width: float = 2.0,
              min_count: int = 1) -> list[tuple[float, float, int, float]]:
    """依支距分組取中位到時。

    回傳 [(支距 m, 中位到時 s, 道數, 視速度 m/s), ...]。
    取中位數而非平均，是為了讓少數挑錯的道不會拉歪整條曲線。
    """
    if bin_width <= 0:
        raise ValueError("bin_width 必須為正數")
    if not picks:
        return []

    offsets = np.array([p.abs_offset for p in picks])
    times = np.array([p.time for p in picks])

    out = []
    for lo in np.arange(0, offsets.max() + bin_width, bin_width):
        mask = (offsets >= lo) & (offsets < lo + bin_width)
        if mask.sum() >= min_count:
            x = float(np.median(offsets[mask]))
            t = float(np.median(times[mask]))
            velocity = x / t if t > 0 else float("inf")
            out.append((x, t, int(mask.sum()), velocity))
    return out
