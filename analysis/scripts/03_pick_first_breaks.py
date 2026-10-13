# -*- coding: utf-8 -*-
"""Step 3：自動挑選初達波，並輸出可供人工覆核的 CSV。

自動挑選只是**基線**。本測線能量最強的是約 127 m/s 的表面波，
任何只看最大能量的演算法都會挑到它，所以這裡用視速度視窗把
表面波排除在搜尋範圍之外，再用 AIC 在視窗內定位起始點。

產生：
  - first_breaks.csv      每一道的挑選結果（含 SNR 與是否可信）
  - picks_on_gather_*.png 把挑選結果疊在炮集上，供目視檢查

用法：
    python scripts/03_pick_first_breaks.py
    python scripts/03_pick_first_breaks.py --check-shots 101 107 112
"""
from __future__ import annotations

import csv

import numpy as np
from matplotlib import pyplot as plt

from _common import banner, build_parser, load_data, prepare

from utels.config import DEFAULT_SURVEY
from utels.loader import shot_gather
from utels.picking import pick_stream, reliable_picks
from utels.plotting import save
from utels.preprocess import agc, bandpass, normalise, time_axis


def plot_picks_on_gather(gather, picks, tmax: float = 0.15):
    """把挑選結果以紅點疊在炮集上，是最重要的覆核手段。"""
    fig, ax = plt.subplots(figsize=(9, 7))
    spacing = DEFAULT_SURVEY.receiver_spacing
    n_show = int(tmax / gather[0].stats.delta)
    by_channel = {p.channel: p for p in picks}

    for tr in gather:
        t = time_axis(tr)[:n_show] * 1000.0
        data = normalise(agc(tr.data[:n_show].astype(float), 80))
        x = tr.stats.utels.offset
        wave = np.clip(data, -1.3, 1.3) * 1.4 * spacing / 2.0 + x
        ax.plot(wave, t, color="k", linewidth=0.5)
        ax.fill_betweenx(t, x, wave, where=(wave > x), color="k", linewidth=0)

        pick = by_channel.get(tr.stats.utels.channel)
        if pick is not None and pick.time * 1000.0 <= tmax * 1000.0:
            reliable = pick.snr >= DEFAULT_SURVEY.snr_threshold_db
            ax.plot(x, pick.time * 1000.0, "o", markersize=6,
                    color="#d62828" if reliable else "#f6a600",
                    markeredgecolor="white", markeredgewidth=0.8, zorder=5)

    ax.set_xlabel("支距 offset (m)")
    ax.set_ylabel("時間 time (ms)")
    ax.set_ylim(tmax * 1000.0, 0)
    ax.grid(alpha=0.25)
    ax.set_title("紅點 = 可信挑選（SNR 足夠），橘點 = 需人工覆核")
    fig.tight_layout()
    return fig


def main() -> int:
    parser = build_parser("自動挑選初達波")
    parser.add_argument("--check-shots", type=int, nargs="*",
                        default=[101, 107, 112],
                        help="要輸出覆核圖的炮號")
    args = parser.parse_args()
    prepare(args)

    banner("Step 3 初達波自動挑選")
    stream = load_data(args)
    work = bandpass(stream)
    survey = DEFAULT_SURVEY

    print(f"\n搜尋視窗的視速度範圍："
          f"{survey.vel_search_min:.0f} - {survey.vel_search_max:.0f} m/s")
    print("  下限刻意高於表面波（約 127 m/s），把表面波排除在視窗外")

    picks = pick_stream(work, survey)
    good = reliable_picks(picks, survey)
    print(f"\n挑選 {len(picks)} 道，其中 {len(good)} 道 "
          f"SNR >= {survey.snr_threshold_db:.0f} dB 且支距 > 0")

    csv_path = args.out / "first_breaks.csv"
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["ffid", "channel", "shot_x_m", "receiver_x_m",
                         "offset_m", "pick_ms", "apparent_velocity_ms",
                         "snr_db", "reliable"])
        for p in picks:
            velocity = (f"{p.apparent_velocity:.0f}"
                        if np.isfinite(p.apparent_velocity) else "")
            writer.writerow([p.ffid, p.channel, p.shot_x, p.receiver_x,
                             p.offset, round(p.time * 1000, 2), velocity,
                             round(p.snr, 1),
                             "Y" if p.snr >= survey.snr_threshold_db else "N"])
    print("  ->", csv_path)

    for ffid in args.check_shots:
        gather = shot_gather(work, ffid)
        subset = [p for p in picks if p.ffid == ffid]
        fig = plot_picks_on_gather(gather, subset)
        print("  ->", save(fig, args.out / f"picks_on_gather_{ffid}.png"))

    print("\n請務必打開覆核圖，確認紅點真的落在初達波的起跳點上。")
    print("Step 3 完成。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
