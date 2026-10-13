# -*- coding: utf-8 -*-
"""Step 5：挑選參數的敏感度測試。

自動挑選器用「視速度視窗」限制搜尋範圍。這個視窗在支距很小時會
變得非常窄（支距 2 m、下限 180 m/s 時，視窗只有 0.8 到 11 ms），
因此近支距的挑選結果可能是被**視窗決定的**，而不是被資料決定的。

這個 step 把視窗下限掃過一個合理範圍，看看哪些分組的視速度穩定、
哪些會跟著參數跑。只有穩定的那些才能拿來下結論。

產生：
  - sensitivity.png
  - sensitivity.csv

用法：
    python scripts/05_sensitivity.py
"""
from __future__ import annotations

import csv
from dataclasses import replace

import numpy as np
from matplotlib import pyplot as plt

from _common import banner, build_parser, load_data, prepare

from utels.config import DEFAULT_SURVEY
from utels.inversion import fit_single_line
from utels.picking import bin_picks, pick_stream, reliable_picks
from utels.plotting import save
from utels.preprocess import bandpass
from utels.quality import ground_roll_velocity

# 掃描的視窗下限 (m/s)。必須高於表面波視速度，否則會挑到表面波。
VEL_MIN_VALUES = (160.0, 180.0, 200.0, 220.0, 250.0, 300.0)
# 視速度在不同設定下的變動超過這個比例，就視為不穩定
STABILITY_TOLERANCE = 0.15


def longest_stable_band(stable_offsets, all_offsets):
    """找出最長的「連續」穩定區間，回傳 (起, 迄)，找不到回傳 None。

    只有連續的一段才有意義：若 8、10、12 m 穩定但 16 m 不穩定，
    不能說成「8 m 以上都穩定」。
    """
    stable = set(stable_offsets)
    best = current = None
    for offset in all_offsets:
        if offset in stable:
            current = (current[0], offset) if current else (offset, offset)
            if best is None or (current[1] - current[0]) > (best[1] - best[0]):
                best = current
        else:
            current = None
    return best


def main() -> int:
    parser = build_parser("挑選參數的敏感度測試")
    args = parser.parse_args()
    prepare(args)

    banner("Step 5 敏感度測試")
    stream = load_data(args)
    work = bandpass(stream)

    v_ground = ground_roll_velocity(work)
    print(f"\n表面波視速度約 {v_ground:.0f} m/s")
    print(f"搜尋視窗下限必須高於它，才不會挑到表面波。")

    results: dict[float, list] = {}
    print(f"\n{'視窗下限':>10}{'可用道數':>10}{'單線視速度':>12}{'殘差 rms':>12}")
    for v_min in VEL_MIN_VALUES:
        survey = replace(DEFAULT_SURVEY, vel_search_min=v_min)
        picks = reliable_picks(pick_stream(work, survey), survey)
        offsets = np.array([p.abs_offset for p in picks])
        times = np.array([p.time for p in picks])
        velocity, _, rms = fit_single_line(offsets, times)
        results[v_min] = bin_picks(picks, 2.0, min_count=4)
        print(f"{v_min:>8.0f} m/s{len(picks):>10d}{velocity:>9.0f} m/s"
              f"{rms * 1000:>9.1f} ms")

    # 彙整每個支距分組的視速度，判斷是否穩定
    all_offsets = sorted({b[0] for bins in results.values() for b in bins})
    print(f"\n各支距分組的視速度 (m/s) 隨視窗下限的變化：")
    header = "".join(f"{v:>7.0f}" for v in VEL_MIN_VALUES)
    print(f"{'支距':>6}{header}{'  變動':>8}  判定")

    rows, stable_offsets = [], []
    for offset in all_offsets:
        velocities = []
        for v_min in VEL_MIN_VALUES:
            match = [b[3] for b in results[v_min] if b[0] == offset]
            velocities.append(match[0] if match else np.nan)
        velocities = np.array(velocities, dtype=float)
        valid = velocities[np.isfinite(velocities)]
        if len(valid) < 2:
            continue
        spread = (valid.max() - valid.min()) / valid.mean()
        stable = spread <= STABILITY_TOLERANCE
        if stable:
            stable_offsets.append(offset)
        cells = "".join(f"{v:>7.0f}" for v in velocities)
        print(f"{offset:>4.0f} m{cells}{spread * 100:>7.0f}%"
              f"  {'穩定' if stable else '不穩定 <-- 不可用'}")
        rows.append([offset, *[round(v) if np.isfinite(v) else "" for v in velocities],
                     round(spread * 100)])

    csv_path = args.out / "sensitivity.csv"
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["offset_m", *[f"vmin_{int(v)}" for v in VEL_MIN_VALUES],
                         "spread_percent"])
        writer.writerows(rows)
    print("  ->", csv_path)

    band = longest_stable_band(stable_offsets, all_offsets)
    if band:
        lo, hi = band
        print(f"\n結論：支距 {lo:.0f} - {hi:.0f} m 的視速度對參數穩定，可以採信。")
        print(f"      小於 {lo:.0f} m：搜尋視窗太窄，結果被參數主導 ——")
        print(f"        自動挑選無法決定近支距的直達波速度 V1，該段必須人工判讀。")
        print(f"      大於 {hi:.0f} m：訊噪比已經不足，挑選本身不可靠。")
    else:
        print("\n結論：沒有任何連續區間對參數穩定，這組自動挑選不可採信。")

    # 繪圖
    fig, ax = plt.subplots(figsize=(9, 5.5))
    colours = plt.cm.viridis(np.linspace(0, 0.9, len(VEL_MIN_VALUES)))
    for colour, v_min in zip(colours, VEL_MIN_VALUES):
        bins = results[v_min]
        ax.plot([b[0] for b in bins], [b[3] for b in bins], "o-",
                color=colour, markersize=4, linewidth=1.3,
                label=f"下限 {v_min:.0f} m/s")
    if band:
        ax.axvspan(band[0], band[1], color="#7d9a68", alpha=0.12)
        ax.text((band[0] + band[1]) / 2, ax.get_ylim()[1] * 0.97,
                "此區間對參數穩定", fontsize=10, color="#3f5c4a",
                ha="center", va="top")
    ax.set_xlabel("|支距| |offset| (m)")
    ax.set_ylabel("分組視速度 apparent velocity (m/s)")
    ax.set_title("挑選視窗下限的敏感度：近支距結果被參數主導")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)
    fig.tight_layout()
    print("  ->", save(fig, args.out / "sensitivity.png"))

    print("\nStep 5 完成。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
