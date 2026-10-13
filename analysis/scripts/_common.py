# -*- coding: utf-8 -*-
"""各 script 共用的路徑處理與命令列參數。"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# 讓 scripts/ 底下的檔案可以 import 上一層的 utels 套件
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utels.config import use_utf8_console  # noqa: E402
from utels.plotting import setup_fonts     # noqa: E402

# 專案根目錄：analysis/scripts/ -> analysis/ -> 專案根
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# 資料可能放在兩種位置：直接放在專案根目錄，或放在教學網站的 data/ 目錄下。
# 依序尋找，找不到就回傳第一個候選，讓錯誤訊息指出預期的位置。
_DATA_DIRS = (PROJECT_ROOT,
              PROJECT_ROOT / "docs" / "seismic-inquiry" / "data")


def _find(name: str) -> Path:
    candidates = [directory / name for directory in _DATA_DIRS]
    return next((c for c in candidates if c.exists()), candidates[0])


DEFAULT_SEGY = _find("202610_UTELS.sgy")
DEFAULT_GEOM = _find("202610_UTELS.geom")
DEFAULT_SEG2 = _find("seg2")
DEFAULT_OUT = PROJECT_ROOT / "analysis" / "figures"


def build_parser(description: str) -> argparse.ArgumentParser:
    """建立所有 script 共用的命令列參數。"""
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--segy", type=Path, default=DEFAULT_SEGY,
                        help="SEG-Y 檔路徑")
    parser.add_argument("--geom", type=Path, default=DEFAULT_GEOM,
                        help="幾何檔路徑（讀 SEG-2 時才需要）")
    parser.add_argument("--seg2", type=Path, default=DEFAULT_SEG2,
                        help="SEG-2 目錄（加上 --use-seg2 才會使用）")
    parser.add_argument("--use-seg2", action="store_true",
                        help="改讀 SEG-2 原始檔，並以 --geom 覆蓋檔頭幾何")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT,
                        help="圖檔與結果的輸出目錄")
    return parser


def prepare(args) -> None:
    """統一的初始化：UTF-8 輸出、中文字型、建立輸出目錄。"""
    use_utf8_console()
    font = setup_fonts()
    if font is None:
        print("[提醒] 找不到中文字型，圖上的中文會顯示為方框。")
    args.out.mkdir(parents=True, exist_ok=True)


def load_data(args):
    """依參數載入資料，回傳 ObsPy Stream。"""
    from utels.loader import load_segy, load_seg2_dir

    if args.use_seg2:
        print(f"讀取 SEG-2 目錄：{args.seg2}")
        print(f"  幾何以 {args.geom.name} 覆蓋（SEG-2 檔頭的幾何是儀器預設值）")
        return load_seg2_dir(args.seg2, args.geom)

    print(f"讀取 SEG-Y：{args.segy}")
    return load_segy(args.segy)


def banner(title: str) -> None:
    print()
    print("=" * 68)
    print(title)
    print("=" * 68)
