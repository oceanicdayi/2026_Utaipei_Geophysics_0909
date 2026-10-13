# -*- coding: utf-8 -*-
"""Step 1：把原始資料畫出來。

產生：
  - gather_FFID.png     每一炮的 wiggle / variable-area 圖
  - gathers_overview.png 12 炮總覽
  - spectrum.png        代表性支距的振幅頻譜
  - gather_raw_vs_filtered.png  濾波前後對照

用法：
    python scripts/01_plot_gathers.py
    python scripts/01_plot_gathers.py --use-seg2        # 改讀 SEG-2 原始檔
    python scripts/01_plot_gathers.py --shots 101 107   # 只畫指定炮
"""
from __future__ import annotations

from _common import banner, build_parser, load_data, prepare

from utels.config import DEFAULT_SURVEY
from utels.loader import ffids, shot_gather
from utels.plotting import (plot_gather_overview, plot_shot_gather,
                            plot_spectrum, save)
from utels.preprocess import bandpass


def main() -> int:
    parser = build_parser("繪製炮集與頻譜")
    parser.add_argument("--shots", type=int, nargs="*", default=None,
                        help="只畫這幾個炮號（預設全部）")
    parser.add_argument("--tmax", type=float, default=0.15,
                        help="圖上顯示的最大時間 (s)")
    parser.add_argument("--no-filter", action="store_true",
                        help="不做帶通濾波，直接畫原始波形")
    args = parser.parse_args()
    prepare(args)

    banner("Step 1 繪製炮集")
    stream = load_data(args)
    print(f"共 {len(stream)} 道，取樣間隔 {stream[0].stats.delta * 1000:.2f} ms，"
          f"每道 {stream[0].stats.npts} 點")

    if args.no_filter:
        work = stream
        print("未做濾波")
    else:
        work = bandpass(stream)
        print(f"帶通濾波 {DEFAULT_SURVEY.bandpass_low:.0f}-"
              f"{DEFAULT_SURVEY.bandpass_high:.0f} Hz（零相位）")

    shots = args.shots if args.shots else ffids(work)

    # 濾波前後對照（只做第一炮，用來說明為什麼要濾波）
    first = shots[0]
    fig = plot_shot_gather(shot_gather(stream, first),
                           title=f"FFID {first}：原始波形（未濾波）",
                           tmax=args.tmax)
    print("  ->", save(fig, args.out / "gather_raw.png"))
    fig = plot_shot_gather(shot_gather(work, first),
                           title=f"FFID {first}：帶通 40-400 Hz + AGC",
                           tmax=args.tmax)
    print("  ->", save(fig, args.out / "gather_filtered.png"))

    # 每一炮各一張
    for ffid in shots:
        gather = shot_gather(work, ffid)
        shot_x = gather[0].stats.utels.shot_x
        fig = plot_shot_gather(
            gather, title=f"FFID {ffid} · 炮點 {shot_x:.0f} m", tmax=args.tmax)
        print("  ->", save(fig, args.out / f"gather_{ffid}.png"))

    # 總覽與頻譜
    fig = plot_gather_overview(work, shots, tmax=args.tmax)
    print("  ->", save(fig, args.out / "gathers_overview.png"))

    fig = plot_spectrum(stream)   # 頻譜要看原始資料，不能看濾波後的
    print("  ->", save(fig, args.out / "spectrum.png"))

    print("\nStep 1 完成。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
