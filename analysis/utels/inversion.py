# -*- coding: utf-8 -*-
"""兩層水平介質的截距時間法（intercept-time method）反演。

t-x 圖上：
  直達波   t = x / V1              （過原點，斜率 1/V1）
  折射波   t = x / V2 + ti         （斜率 1/V2，截距 ti）

由 ti 可求界面深度：
  h = (ti / 2) * V1 * V2 / sqrt(V2^2 - V1^2)

轉折距離（crossover distance）：
  xc = ti / (1/V1 - 1/V2)

前提假設：介面水平、速度隨深度遞增、地表平坦。本測線未測高程，
因此只能在這個假設下求解。
"""
from __future__ import annotations

import warnings
from dataclasses import dataclass

import numpy as np


# 接受一個「兩層解」的最低門檻。若只用 V2 > V1 與 ti > 0 判斷，
# 單層資料會因為浮點誤差產生 V2/V1 = 1.0000000001、ti = 1e-17
# 這種毫無意義的解，程式卻回報「找到兩層模型」。
MIN_VELOCITY_CONTRAST = 1.05   # V2 至少要比 V1 快 5%
MIN_INTERCEPT = 1e-4           # 截距至少 0.1 ms（遠小於取樣間隔就沒有意義）


@dataclass(frozen=True)
class TwoLayerModel:
    """兩層速度模型的反演結果。"""

    v1: float            # 上層速度 (m/s)
    v2: float            # 下層速度 (m/s)
    intercept: float     # 折射波截距時間 ti (s)
    crossover: float     # 轉折距離 (m)
    depth: float         # 界面深度 (m)
    breakpoint: float    # 擬合時採用的分段距離 (m)
    rms: float           # 殘差均方根 (s)
    n_near: int          # 近支距（直達波段）資料筆數
    n_far: int           # 遠支距（折射波段）資料筆數

    def describe(self) -> str:
        return (f"V1 = {self.v1:.0f} m/s, V2 = {self.v2:.0f} m/s, "
                f"ti = {self.intercept * 1000:.1f} ms, "
                f"深度 = {self.depth:.2f} m, "
                f"轉折距離 = {self.crossover:.1f} m, "
                f"殘差 rms = {self.rms * 1000:.1f} ms")


def layer_depth(v1: float, v2: float, intercept: float) -> float:
    """由截距時間求界面深度 (m)。"""
    if v2 <= v1:
        raise ValueError(f"折射法要求 V2 > V1，收到 V1={v1}, V2={v2}")
    if intercept < 0:
        raise ValueError(f"截距時間不可為負：{intercept}")
    return intercept / 2.0 * v1 * v2 / np.sqrt(v2 ** 2 - v1 ** 2)


def crossover_distance(v1: float, v2: float, intercept: float) -> float:
    """轉折距離 (m)：直達波與折射波到時相等之處。"""
    if v2 <= v1:
        raise ValueError(f"折射法要求 V2 > V1，收到 V1={v1}, V2={v2}")
    return intercept / (1.0 / v1 - 1.0 / v2)


def fit_two_layer(offsets: np.ndarray, times: np.ndarray,
                  search_range: tuple[float, float] = (3.0, 20.0),
                  step: float = 0.5, min_points: int = 4
                  ) -> TwoLayerModel | None:
    """搜尋分段點，對 t-x 資料做兩段直線擬合。

    對每一個候選分段距離各做一次最小平方擬合，取總殘差最小者。
    若找不到任何滿足物理門檻的解，回傳 None——這代表資料本身
    **不支援**兩層模型，不應該硬湊一個答案出來。門檻為：
    V2 至少比 V1 快 MIN_VELOCITY_CONTRAST 倍，且截距 >= MIN_INTERCEPT。

    offsets: |支距| (m)；times: 到時 (s)。
    """
    offsets = np.asarray(offsets, dtype=float)
    times = np.asarray(times, dtype=float)
    if offsets.shape != times.shape:
        raise ValueError("offsets 與 times 長度必須相同")
    if len(offsets) < 2 * min_points:
        raise ValueError(f"資料點太少（{len(offsets)}），無法做兩段擬合")

    best = None
    for xc in np.arange(search_range[0], search_range[1] + 1e-9, step):
        near, far = offsets <= xc, offsets > xc
        if near.sum() < min_points or far.sum() < min_points:
            continue
        with warnings.catch_warnings():
            # 分段點掃到邊緣時，某一段可能只剩幾個幾乎共線的點，
            # numpy 會提示條件數不佳。這是搜尋過程的正常現象，
            # 該候選解會在下方的物理約束被淘汰，不需要顯示給使用者。
            warnings.simplefilter("ignore", np.exceptions.RankWarning)
            slope1, icept1 = np.polyfit(offsets[near], times[near], 1)
            slope2, icept2 = np.polyfit(offsets[far], times[far], 1)
        # 物理約束：折射段必須明顯更平緩（V2 比 V1 快至少 5%）、
        # 且截距大到有物理意義。只用 ">" 判斷會被浮點誤差騙過去。
        if slope2 <= 0 or slope1 <= 0:
            continue
        if slope1 / slope2 < MIN_VELOCITY_CONTRAST or icept2 < MIN_INTERCEPT:
            continue
        residual = np.concatenate([
            np.polyval([slope1, icept1], offsets[near]) - times[near],
            np.polyval([slope2, icept2], offsets[far]) - times[far]])
        rms = float(np.sqrt(np.mean(residual ** 2)))
        if best is None or rms < best[0]:
            best = (rms, xc, slope1, slope2, icept2,
                    int(near.sum()), int(far.sum()))

    if best is None:
        return None

    rms, xc, slope1, slope2, intercept, n_near, n_far = best
    v1, v2 = 1.0 / slope1, 1.0 / slope2
    return TwoLayerModel(
        v1=v1, v2=v2, intercept=intercept,
        crossover=crossover_distance(v1, v2, intercept),
        depth=layer_depth(v1, v2, intercept),
        breakpoint=float(xc), rms=rms, n_near=n_near, n_far=n_far)


def fit_single_line(offsets: np.ndarray, times: np.ndarray
                    ) -> tuple[float, float, float]:
    """單一直線擬合，回傳 (視速度 m/s, 截距 s, 殘差 rms s)。

    用來跟兩層模型比較：如果兩者殘差差不多，就代表資料**無法**
    分辨兩層與單層，不能宣稱看到了界面。
    """
    offsets = np.asarray(offsets, dtype=float)
    times = np.asarray(times, dtype=float)
    slope, intercept = np.polyfit(offsets, times, 1)
    rms = float(np.sqrt(np.mean(
        (np.polyval([slope, intercept], offsets) - times) ** 2)))
    return 1.0 / slope, float(intercept), rms
