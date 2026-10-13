# -*- coding: utf-8 -*-
"""觀測參數與分析預設值。

所有「魔術數字」集中在這裡，不散落在各個模組中。
數值來自 2026-10-07 的野外紀錄紙與儀器檔頭。
"""
from __future__ import annotations

import sys
from dataclasses import dataclass, field


def use_utf8_console() -> None:
    """讓 Windows 終端機能正確輸出中文。

    Windows 預設 stdout 編碼為 cp950，印出中文會丟 UnicodeEncodeError。
    在 script 最前面呼叫一次即可。
    """
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8")
            except (ValueError, OSError):
                pass  # 某些環境（如被重導向的管線）不支援，忽略即可


@dataclass(frozen=True)
class Survey:
    """一條測線的觀測幾何與分析參數（不可變）。"""

    name: str = "202610_UTELS"
    n_channels: int = 24
    receiver_spacing: float = 2.0      # m
    receiver_x0: float = 0.0           # 第一支受波器的位置 (m)
    shot_spacing: float = 4.0          # m
    n_shots: int = 12
    first_ffid: int = 101
    sample_interval: float = 0.00025   # s
    record_length: float = 0.5         # s

    # --- 分析預設值 ---
    bandpass_low: float = 40.0         # Hz，壓低 20-40 Hz 的表面波
    bandpass_high: float = 400.0       # Hz
    noise_window: tuple[float, float] = (0.40, 0.50)   # s，估計雜訊的末端視窗
    signal_window: tuple[float, float] = (0.00, 0.20)  # s，訊號視窗
    snr_threshold_db: float = 30.0     # 納入走時分析的最低訊噪比
    usable_threshold_db: float = 25.0  # 判定「可用」的訊噪比
    # 初達波搜尋的視速度範圍 (m/s)：上限排除直達 P 不可能的高速，
    # 下限 180 m/s 刻意高於本測線約 127 m/s 的表面波，避免挑到表面波。
    vel_search_max: float = 2500.0
    vel_search_min: float = 180.0

    @property
    def receiver_x(self) -> list[float]:
        """24 支受波器的座標 (m)。"""
        return [self.receiver_x0 + i * self.receiver_spacing
                for i in range(self.n_channels)]

    @property
    def shot_x(self) -> list[float]:
        """12 個炮點的座標 (m)。"""
        return [i * self.shot_spacing for i in range(self.n_shots)]

    @property
    def spread(self) -> tuple[float, float]:
        """受波器展距 (起, 迄)，單位 m。"""
        xs = self.receiver_x
        return xs[0], xs[-1]


DEFAULT_SURVEY = Survey()
