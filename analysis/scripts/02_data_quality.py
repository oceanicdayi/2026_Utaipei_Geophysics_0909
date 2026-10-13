# -*- coding: utf-8 -*-
"""Step 2：資料品質檢核。

先問「這筆資料能回答什麼問題」，再決定要不要做反演。
這一步會算出每一道的訊噪比，並找出可信的支距上限。

產生：
  - snr_vs_offset.png
  - snr_table.csv

用法：
    python scripts/02_data_quality.py
"""
from __future__ import annotations

import csv

import numpy as np

from _common import banner, build_parser, load_data, prepare

from utels.config import DEFAULT_SURVEY
from utels.plotting import plot_snr, save
from utels.preprocess import bandpass
from utels.quality import snr_by_offset, stream_snr


def main() -> int:
    parser = build_parser("計算訊噪比並評估可用支距範圍")
    parser.add_argument("--bin-width", type=float, default=4.0,
                        help="統計分組的支距寬度 (m)")
    args = parser.parse_args()
    prepare(args)

    banner("Step 2 資料品質檢核")
    stream = load_data(args)
    work = bandpass(stream)
    survey = DEFAULT_SURVEY

    snr = stream_snr(work, survey)
    offsets = np.array([tr.stats.utels.abs_offset for tr in work])

    print(f"\n訊號視窗 {survey.signal_window} s，"
          f"雜訊視窗 {survey.noise_window} s")
    print(f"總道數 {len(work)}")
    for threshold in (25.0, 30.0):
        count = int((snr >= threshold).sum())
        print(f"  SNR >= {threshold:.0f} dB：{count} 道 "
              f"({count / len(work) * 100:.0f}%)")

    bins = snr_by_offset(work, args.bin_width, survey)
    print(f"\n每 {args.bin_width:.0f} m 分組的訊噪比中位數：")
    print(f"  {'支距範圍':<14}{'道數':>6}{'中位 SNR':>12}")
    limit = None
    for centre, median, count in bins:
        lo = centre - args.bin_width / 2
        print(f"  {lo:>4.0f} - {lo + args.bin_width:<7.0f}{count:>6d}"
              f"{median:>10.1f} dB")
        if limit is None and median < 12.0:
            limit = lo
    if limit is not None:
        print(f"\n中位訊噪比從 {limit:.0f} m 起低於 12 dB，"
              f"超過此距離的初達波已埋在雜訊中。")
    else:
        print("\n所有分組的中位訊噪比都在 12 dB 以上。")

    csv_path = args.out / "snr_table.csv"
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["ffid", "channel", "shot_x_m", "receiver_x_m",
                         "offset_m", "snr_db"])
        for tr, value in zip(work, snr):
            g = tr.stats.utels
            writer.writerow([g.ffid, g.channel, g.shot_x, g.receiver_x,
                             g.offset, round(float(value), 2)])
    print("  ->", csv_path)

    fig = plot_snr(work, bins, survey)
    print("  ->", save(fig, args.out / "snr_vs_offset.png"))

    print("\nStep 2 完成。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
