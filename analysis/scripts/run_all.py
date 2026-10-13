# -*- coding: utf-8 -*-
"""一次跑完 Step 1 到 Step 4。

只接受四個 step 共通的參數；各 step 專屬的選項（例如 01 的 --shots）
請直接執行該 step。

用法：
    python scripts/run_all.py
    python scripts/run_all.py --use-seg2            # 改用 SEG-2 原始檔
    python scripts/run_all.py --out my_figures      # 換輸出目錄
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import build_parser  # noqa: E402

SCRIPTS = [
    ("01_plot_gathers.py", "繪製炮集與頻譜"),
    ("02_data_quality.py", "資料品質檢核"),
    ("03_pick_first_breaks.py", "初達波自動挑選"),
    ("04_travel_time.py", "走時分析與反演"),
    ("05_sensitivity.py", "挑選參數敏感度測試"),
]


def common_arguments(args) -> list[str]:
    """把共通參數還原成命令列字串，轉交給各個 step。"""
    out = ["--segy", str(args.segy), "--geom", str(args.geom),
           "--seg2", str(args.seg2), "--out", str(args.out)]
    if args.use_seg2:
        out.append("--use-seg2")
    return out


def main() -> int:
    args = build_parser("依序執行全部四個分析步驟").parse_args()
    here = Path(__file__).resolve().parent
    passthrough = common_arguments(args)

    for filename, description in SCRIPTS:
        print(f"\n{'#' * 68}\n# {filename} — {description}\n{'#' * 68}")
        result = subprocess.run(
            [sys.executable, str(here / filename), *passthrough],
            cwd=here.parent)
        if result.returncode != 0:
            print(f"\n[失敗] {filename} 回傳 {result.returncode}，中止後續步驟。")
            return result.returncode

    print(f"\n{'=' * 68}")
    print(f"全部完成。圖檔與 CSV 在 {args.out}")
    print("=" * 68)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
