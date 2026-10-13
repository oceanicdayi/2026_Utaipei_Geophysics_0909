# -*- coding: utf-8 -*-
"""202610_UTELS 淺層折射震測資料分析套件。

以 ObsPy 為基礎，提供讀檔、前處理、初達波挑選、品質檢核、
走時反演與繪圖。所有模組都不修改傳入的資料，一律回傳新物件。
"""
from .config import Survey, DEFAULT_SURVEY
from .loader import load_segy, load_seg2, parse_geom
from .preprocess import bandpass, agc, normalise
from .picking import pick_stream, pick_trace
from .quality import trace_snr, reciprocal_pairs
from .inversion import fit_two_layer, TwoLayerModel

__all__ = [
    "Survey", "DEFAULT_SURVEY",
    "load_segy", "load_seg2", "parse_geom",
    "bandpass", "agc", "normalise",
    "pick_stream", "pick_trace",
    "trace_snr", "reciprocal_pairs",
    "fit_two_layer", "TwoLayerModel",
]

__version__ = "1.0.0"
