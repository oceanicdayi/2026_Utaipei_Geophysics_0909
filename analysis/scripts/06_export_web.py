# -*- coding: utf-8 -*-
"""Step 6（選用）：把分析結果輸出成網站用的 results-data.js。

讓教學網站上的每一個數字，都由這套公開程式產生——別人跑一次
就能得到一模一樣的結果。

用法：
    python scripts/06_export_web.py --web-out ../../site/docs/seismic-inquiry
"""
from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path

import numpy as np

from _common import banner, build_parser, load_data, prepare

from utels.config import DEFAULT_SURVEY
from utels.inversion import fit_single_line
from utels.picking import bin_picks, pick_stream, reliable_picks
from utels.preprocess import bandpass
from utels.quality import (ground_roll_velocity, reciprocal_pairs,
                           snr_by_offset, stream_snr)

VEL_MIN_VALUES = (160.0, 180.0, 200.0, 220.0, 250.0, 300.0)
STABILITY_TOLERANCE = 0.15

SHOTS = [(101, 0, 15, "11:13:29"), (102, 4, 14, "11:17:28"),
         (103, 8, 14, "11:19:54"), (104, 12, 15, "11:21:48"),
         (105, 16, 13, "11:23:54"), (106, 20, 9, "11:25:33"),
         (107, 24, 11, "11:29:12"), (108, 28, 3, "11:30:15"),
         (109, 32, 11, "11:32:53"), (110, 36, 13, "11:34:39"),
         (111, 40, 9, "11:36:16"), (112, 44, 14, "11:38:01")]


def stability(stream) -> dict[float, bool]:
    """重跑敏感度測試，回傳 {支距: 是否穩定}。"""
    results = {}
    for v_min in VEL_MIN_VALUES:
        survey = replace(DEFAULT_SURVEY, vel_search_min=v_min)
        picks = reliable_picks(pick_stream(stream, survey), survey)
        results[v_min] = {b[0]: b[3] for b in bin_picks(picks, 2.0, min_count=4)}

    offsets = sorted({x for table in results.values() for x in table})
    out = {}
    for offset in offsets:
        values = np.array([results[v].get(offset, np.nan) for v in VEL_MIN_VALUES],
                          dtype=float)
        valid = values[np.isfinite(values)]
        out[offset] = (len(valid) >= 2 and
                       (valid.max() - valid.min()) / valid.mean() <= STABILITY_TOLERANCE)
    return out


def main() -> int:
    parser = build_parser("輸出網站用的 results-data.js")
    parser.add_argument("--web-out", type=Path, required=True,
                        help="網站 seismic-inquiry 目錄")
    args = parser.parse_args()
    prepare(args)

    banner("Step 6 匯出網站資料")
    stream = load_data(args)
    work = bandpass(stream)
    survey = DEFAULT_SURVEY

    snr = stream_snr(work, survey)
    offsets = np.array([tr.stats.utels.abs_offset for tr in work])
    snr_bins = snr_by_offset(work, 4.0, survey)

    picks = pick_stream(work, survey)
    good = reliable_picks(picks, survey)
    tx_bins = bin_picks(good, 2.0, min_count=4)
    stable = stability(work)

    px = np.array([p.abs_offset for p in good])
    pt = np.array([p.time for p in good])
    velocity, intercept, rms = fit_single_line(px, pt)

    pairs = reciprocal_pairs({(p.shot_x, p.receiver_x): p.time for p in good})
    diffs = np.array([p.difference for p in pairs]) * 1000.0

    stable_offsets = [x for x, ok in stable.items() if ok]
    stable_velocities = [b[3] for b in tx_bins if stable.get(b[0], False)]

    payload = {
        "snr": [[float(x), round(float(v), 1)] for x, v in zip(offsets, snr)],
        "snrBins": [[b[0], round(b[1], 1), b[2]] for b in snr_bins],
        "picks": [[float(p.abs_offset), round(p.time * 1000, 1)] for p in good],
        "txBins": [[b[0], round(b[1] * 1000, 1), b[2], round(b[3]),
                    bool(stable.get(b[0], False))] for b in tx_bins],
        "line": [round(velocity), round(intercept * 1000, 1), round(rms * 1000, 1)],
        "recip": {"n": len(pairs), "med": round(float(np.median(diffs)), 1)},
        "nTraces": len(work),
        "nUsable25": int((snr >= 25).sum()),
        "nUsable30": int((snr >= 30).sum()),
        "groundRoll": round(ground_roll_velocity(work)),
        "stableBand": [min(stable_offsets), max(stable_offsets)] if stable_offsets else None,
        "stableVelocity": [round(min(stable_velocities)), round(max(stable_velocities))]
                          if stable_velocities else None,
    }

    header = ("/* 202610_UTELS — 實測資料與分析結果\n"
              "   本檔由 analysis/scripts/06_export_web.py 自動產生，請勿手改。\n"
              "   重跑方式見 analysis/README.md。 */\n")
    shots_js = json.dumps(
        [{"ffid": a, "x": b, "stack": c, "time": d} for a, b, c, d in SHOTS],
        ensure_ascii=False)

    body = [header,
            f"const fieldShots = {shots_js};\n",
            "const measured = {"]
    comments = {
        "snr": "每道訊噪比：[|支距| m, SNR dB]",
        "snrBins": "每 4 m 的 SNR 中位數：[支距中心 m, 中位數 dB, 道數]",
        "picks": "可用初達波挑選：[|支距| m, 到時 ms]，SNR >= 30 dB",
        "txBins": "每 2 m 分組：[支距 m, 中位到時 ms, 道數, 視速度 m/s, 是否對參數穩定]",
        "line": "單一直線擬合：[視速度 m/s, 截距 ms, 殘差 rms ms]",
        "stableBand": "敏感度測試判定可採信的支距區間 [起, 迄] m",
        "stableVelocity": "該區間內的視速度範圍 [低, 高] m/s",
    }
    for key, value in payload.items():
        if key in comments:
            body.append(f"  /* {comments[key]} */")
        body.append(f"  {key}: {json.dumps(value, ensure_ascii=False)},")
    body.append("};")

    target = args.web_out / "results-data.js"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(body) + "\n", encoding="utf-8")

    print(f"\n可用道數 (SNR>=25dB)  {payload['nUsable25']} / {payload['nTraces']}")
    print(f"單線視速度            {payload['line'][0]} m/s，"
          f"殘差 rms {payload['line'][2]} ms")
    print(f"互換時間              {payload['recip']['n']} 組，"
          f"中位差 {payload['recip']['med']} ms")
    print(f"表面波視速度          {payload['groundRoll']} m/s")
    print(f"可採信支距區間        {payload['stableBand']} m")
    print(f"該區間視速度          {payload['stableVelocity']} m/s")
    print("\n  ->", target)
    print("Step 6 完成。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
