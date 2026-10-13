# -*- coding: utf-8 -*-
"""Step 4：走時分析、互換時間檢核與兩層模型反演。

這一步會誠實地回答一個問題：這組挑選結果**撐不撐得起**兩層模型？
程式會同時做單一直線擬合與兩段擬合，比較兩者的殘差。
如果兩者差不多，就代表資料無法分辨兩層與單層，不應該宣稱看到界面。

產生：
  - travel_time.png            t-x 走時圖
  - travel_time_by_shot.png    逐炮走時曲線
  - reciprocity.png            互換時間檢核
  - travel_time_bins.csv       分組統計

用法：
    python scripts/04_travel_time.py
"""
from __future__ import annotations

import csv

import numpy as np

from _common import banner, build_parser, load_data, prepare

from utels.config import DEFAULT_SURVEY
from utels.inversion import (MIN_INTERCEPT, MIN_VELOCITY_CONTRAST,
                             fit_single_line, fit_two_layer)
from utels.picking import bin_picks, pick_stream, reliable_picks
from utels.plotting import (plot_reciprocity, plot_travel_time,
                            plot_travel_time_by_shot, save)
from utels.preprocess import bandpass
from utels.quality import reciprocal_pairs


def main() -> int:
    parser = build_parser("走時分析與兩層模型反演")
    parser.add_argument("--bin-width", type=float, default=2.0,
                        help="走時分組的支距寬度 (m)")
    parser.add_argument("--xmax", type=float, default=26.0,
                        help="走時圖的最大支距 (m)")
    args = parser.parse_args()
    prepare(args)

    banner("Step 4 走時分析")
    stream = load_data(args)
    work = bandpass(stream)
    survey = DEFAULT_SURVEY

    picks = pick_stream(work, survey)
    good = reliable_picks(picks, survey)
    print(f"\n可用挑選 {len(good)} / {len(picks)} 道 "
          f"(SNR >= {survey.snr_threshold_db:.0f} dB)")

    # --- 互換時間檢核 ---
    table = {(p.shot_x, p.receiver_x): p.time for p in good}
    pairs = reciprocal_pairs(table)
    if pairs:
        diffs = np.array([p.difference for p in pairs]) * 1000.0
        print(f"\n互換時間：{len(pairs)} 組配對")
        print(f"  中位差 {np.median(diffs):.1f} ms，"
              f"平均 {diffs.mean():.1f} ms，最大 {diffs.max():.1f} ms")
        print("  （理論上應為 0；差太多代表該組到時挑錯或幾何有誤）")
    else:
        print("\n找不到互換配對。")
    print("  ->", save(plot_reciprocity(pairs), args.out / "reciprocity.png"))

    # --- 分組統計 ---
    bins = bin_picks(good, args.bin_width, min_count=4)
    print(f"\n每 {args.bin_width:.0f} m 分組的中位到時與視速度：")
    print(f"  {'支距':>6}{'道數':>6}{'中位到時':>12}{'視速度':>12}")
    for x, t, count, velocity in bins:
        print(f"  {x:>4.0f} m{count:>6d}{t * 1000:>10.1f} ms"
              f"{velocity:>9.0f} m/s")

    csv_path = args.out / "travel_time_bins.csv"
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["offset_m", "median_time_ms", "n_traces",
                         "apparent_velocity_ms"])
        for x, t, count, velocity in bins:
            writer.writerow([x, round(t * 1000, 2), count, round(velocity)])
    print("  ->", csv_path)

    # --- 擬合：單線 vs 兩段 ---
    offsets = np.array([p.abs_offset for p in good])
    times = np.array([p.time for p in good])

    velocity, intercept, rms_single = fit_single_line(offsets, times)
    print(f"\n單一直線擬合：視速度 {velocity:.0f} m/s，"
          f"截距 {intercept * 1000:.1f} ms，殘差 rms {rms_single * 1000:.1f} ms")

    model = fit_two_layer(offsets, times)
    if model is None:
        print(f"\n兩段擬合：找不到滿足物理門檻的解"
              f"（V2 需比 V1 快 {(MIN_VELOCITY_CONTRAST - 1) * 100:.0f}% 以上，"
              f"截距需 >= {MIN_INTERCEPT * 1000:.1f} ms）。")
        print("  => 這組自動挑選結果不足以支撐兩層模型。")
        print("     必須人工逐道判讀初達波後再重做。")
    else:
        print(f"\n兩段擬合：{model.describe()}")
        improvement = (rms_single - model.rms) / rms_single * 100
        print(f"  相對單線模型，殘差減少 {improvement:.0f}%")
        if improvement < 15:
            print("  => 改善幅度太小，資料無法分辨兩層與單層。")
            print("     不應該宣稱已經看到速度界面。")

    print("  ->", save(plot_travel_time(good, bins, model, xmax=args.xmax),
                       args.out / "travel_time.png"))
    print("  ->", save(plot_travel_time_by_shot(good),
                       args.out / "travel_time_by_shot.png"))

    print("\nStep 4 完成。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
