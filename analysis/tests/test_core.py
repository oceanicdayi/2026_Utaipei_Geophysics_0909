# -*- coding: utf-8 -*-
"""核心數值功能的單元測試。

重點放在「算錯了會讓結論整個不同」的部分：截距時間法的公式、
AIC 挑選器、互換時間配對、以及反演的物理約束。

執行：
    pytest -q
    pytest --cov=utels --cov-report=term-missing
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utels.config import Survey  # noqa: E402
from utels.inversion import (crossover_distance, fit_single_line,  # noqa: E402
                             fit_two_layer, layer_depth)
from utels.picking import aic_pick, sta_lta  # noqa: E402
from utels.preprocess import agc, normalise  # noqa: E402
from utels.quality import reciprocal_pairs  # noqa: E402


# ───────────────────────── Survey 幾何 ─────────────────────────

def test_survey_geometry_matches_field_sheet():
    """預設 Survey 必須與野外紀錄紙一致。"""
    s = Survey()
    assert s.n_channels == 24
    assert s.receiver_spacing == 2.0
    assert s.spread == (0.0, 46.0)          # 展距 0-46 m，不是 0-44 m
    assert s.shot_x == [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44]
    assert len(s.receiver_x) == 24


def test_survey_is_immutable():
    s = Survey()
    with pytest.raises(Exception):
        s.n_channels = 48       # frozen dataclass 不可修改


# ───────────────────────── 截距時間法 ─────────────────────────

def test_layer_depth_known_case():
    """以課本公式手算驗證：V1=400, V2=800, ti=10 ms。

    h = ti/2 * V1*V2/sqrt(V2^2-V1^2)
      = 0.005 * 320000 / sqrt(640000-160000)
      = 0.005 * 320000 / 692.82 = 2.309 m
    """
    assert layer_depth(400.0, 800.0, 0.010) == pytest.approx(2.309, abs=0.01)


def test_crossover_distance_known_case():
    """xc = ti / (1/V1 - 1/V2) = 0.010 / (1/400 - 1/800) = 8.0 m"""
    assert crossover_distance(400.0, 800.0, 0.010) == pytest.approx(8.0, abs=0.01)


def test_depth_rejects_v2_not_greater_than_v1():
    """折射法的前提是速度隨深度遞增，違反時必須明確報錯而非回傳 NaN。"""
    with pytest.raises(ValueError, match="V2 > V1"):
        layer_depth(800.0, 400.0, 0.010)
    with pytest.raises(ValueError, match="V2 > V1"):
        crossover_distance(500.0, 500.0, 0.010)


def test_depth_rejects_negative_intercept():
    with pytest.raises(ValueError):
        layer_depth(400.0, 800.0, -0.001)


# ───────────────────────── 兩層反演 ─────────────────────────

def _synthetic_two_layer(v1=400.0, v2=900.0, h=3.0, noise=0.0, seed=0):
    """用已知模型產生合成走時資料，用來驗證反演能否還原原參數。"""
    rng = np.random.default_rng(seed)
    ic = np.arcsin(v1 / v2)
    ti = 2 * h * np.cos(ic) / v1
    x = np.arange(1.0, 40.0, 0.5)
    t = np.minimum(x / v1, ti + x / v2)
    if noise > 0:
        t = t + rng.normal(0.0, noise, size=t.shape)
    return x, t, ti


def test_fit_two_layer_recovers_known_model():
    """無雜訊的合成資料應能準確還原 V1、V2 與深度。"""
    x, t, ti = _synthetic_two_layer(v1=400.0, v2=900.0, h=3.0)
    model = fit_two_layer(x, t)
    assert model is not None
    assert model.v1 == pytest.approx(400.0, rel=0.05)
    assert model.v2 == pytest.approx(900.0, rel=0.05)
    assert model.depth == pytest.approx(3.0, rel=0.10)
    assert model.intercept == pytest.approx(ti, rel=0.10)


def test_fit_two_layer_tolerates_small_noise():
    x, t, _ = _synthetic_two_layer(noise=0.0015, seed=42)
    model = fit_two_layer(x, t)
    assert model is not None
    assert model.v1 == pytest.approx(400.0, rel=0.20)
    assert model.v2 == pytest.approx(900.0, rel=0.20)


def test_fit_two_layer_returns_none_for_single_layer_data():
    """單層資料不該被硬湊成兩層模型——寧可回傳 None。"""
    x = np.arange(1.0, 40.0, 0.5)
    t = x / 500.0
    assert fit_two_layer(x, t) is None


def test_fit_two_layer_rejects_mismatched_input():
    with pytest.raises(ValueError):
        fit_two_layer(np.arange(10.0), np.arange(9.0))


def test_fit_single_line_recovers_velocity():
    x = np.arange(1.0, 30.0)
    velocity, intercept, rms = fit_single_line(x, x / 650.0)
    assert velocity == pytest.approx(650.0, rel=0.01)
    assert intercept == pytest.approx(0.0, abs=1e-6)
    assert rms == pytest.approx(0.0, abs=1e-9)


# ───────────────────────── 挑選器 ─────────────────────────

def test_aic_pick_finds_onset_in_synthetic_trace():
    """前 500 點為低振幅雜訊、之後為大振幅訊號，AIC 應落在交界附近。"""
    rng = np.random.default_rng(1)
    trace = np.concatenate([rng.normal(0, 0.01, 500),
                            rng.normal(0, 1.00, 500)])
    assert abs(aic_pick(trace, 0, len(trace)) - 500) < 25


def test_aic_pick_handles_short_window():
    """視窗太短時回傳起點，不應拋例外。"""
    assert aic_pick(np.zeros(100), 10, 15) == 10


def test_sta_lta_peaks_at_onset():
    rng = np.random.default_rng(2)
    trace = np.concatenate([rng.normal(0, 0.01, 500),
                            rng.normal(0, 1.00, 500)])
    ratio = sta_lta(trace, n_sta=10, n_lta=100)
    assert 500 <= int(np.argmax(ratio)) < 560


def test_sta_lta_rejects_bad_windows():
    with pytest.raises(ValueError):
        sta_lta(np.zeros(100), n_sta=100, n_lta=10)


# ───────────────────────── 前處理 ─────────────────────────

def test_normalise_scales_peak_to_one():
    assert np.abs(normalise(np.array([0.0, -4.0, 2.0]))).max() == pytest.approx(1.0)


def test_normalise_handles_all_zero_trace():
    """全零道不可除以零。"""
    assert np.allclose(normalise(np.zeros(10)), 0.0)


def test_agc_equalises_amplitude_between_segments():
    """AGC 應把原本相差 100 倍的兩段振幅拉近到個位數倍率。

    不會完全等化：floor_ratio 會為安靜段設下限，避免把純雜訊
    放大到跟訊號一樣大。這是刻意的設計。
    """
    data = np.concatenate([np.sin(np.linspace(0, 40, 500)) * 100.0,
                           np.sin(np.linspace(0, 40, 500)) * 1.0])
    out = agc(data, window_samples=50)
    ratio = np.abs(out[100:400]).mean() / np.abs(out[600:900]).mean()
    assert 1.0 < ratio < 4.0          # 原始比值為 100


def test_agc_floor_prevents_amplifying_silence():
    """安靜段不應被放大到與訊號同等級。"""
    data = np.concatenate([np.sin(np.linspace(0, 40, 500)) * 100.0,
                           np.zeros(500)])
    out = agc(data, window_samples=50)
    assert np.abs(out[600:900]).max() < 0.1


def test_agc_rejects_tiny_window():
    with pytest.raises(ValueError):
        agc(np.zeros(100), window_samples=1)


# ───────────────────────── 互換時間 ─────────────────────────

def test_reciprocal_pairs_found_and_not_duplicated():
    picks = {(0.0, 4.0): 0.010, (4.0, 0.0): 0.011,
             (0.0, 8.0): 0.020, (8.0, 0.0): 0.019}
    pairs = reciprocal_pairs(picks)
    assert len(pairs) == 2                       # 每組只算一次
    assert pairs[0].difference == pytest.approx(0.001)


def test_reciprocal_pairs_empty_when_no_match():
    assert reciprocal_pairs({(0.0, 4.0): 0.01, (0.0, 8.0): 0.02}) == []
