# -*- coding: utf-8 -*-
"""讀取 SEG-Y / SEG-2 檔案，並把正確的觀測幾何掛到每一道上。

重點：`seg2/*.dat` 的檔頭幾何是**儀器預設值**（受波器間距寫成 1 m、
震源位置每個檔都寫 4.00），不是現場幾何。因此讀 SEG-2 時一定要
用 `.geom` 檔或 `Survey` 覆蓋，否則算出來的速度會錯。
SEG-Y 的檔頭則已經套入正確幾何，可以直接使用。
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from obspy import Stream, read
from obspy.core import AttribDict
from obspy.io.segy.core import _read_segy

from .config import DEFAULT_SURVEY, Survey


@dataclass(frozen=True)
class Geometry:
    """單一道的觀測幾何。"""

    ffid: int          # 原始炮號（101-112）
    channel: int       # 道號（1-24）
    shot_x: float      # 炮點座標 (m)
    receiver_x: float  # 受波器座標 (m)

    @property
    def offset(self) -> float:
        """帶正負號的支距：受波器座標減炮點座標 (m)。"""
        return self.receiver_x - self.shot_x

    @property
    def abs_offset(self) -> float:
        return abs(self.offset)


def _attach(stream: Stream, geoms: list[Geometry]) -> Stream:
    """把幾何掛到 `tr.stats.utels`，回傳同一個 Stream。"""
    if len(stream) != len(geoms):
        raise ValueError(
            f"道數與幾何筆數不符：stream={len(stream)}, geometry={len(geoms)}")
    for tr, g in zip(stream, geoms):
        tr.stats.utels = AttribDict(
            ffid=g.ffid, channel=g.channel, shot_x=g.shot_x,
            receiver_x=g.receiver_x, offset=g.offset, abs_offset=g.abs_offset)
    return stream


def parse_geom(path: str | Path) -> dict[int, float]:
    """解析 `.geom` 檔，回傳 {炮號: 炮點座標 (m)}。

    檔案格式（202610_UTELS.geom）::

        24 2.0                      <- 通道數、測站間距 (m)
        101    0    0  23  .0 .0 .0 <- 炮號、炮點測站編號、起訖測站、保留欄
        ...

    炮點座標 = 炮點測站編號 x 測站間距。
    """
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"找不到幾何檔：{path}")

    lines = [ln.strip() for ln in path.read_text(encoding="ascii").splitlines()]
    lines = [ln for ln in lines if ln and not ln.startswith("*")]
    if not lines:
        raise ValueError(f"幾何檔沒有內容：{path}")

    header = lines[0].split()
    if len(header) < 2:
        raise ValueError(f"幾何檔首行格式不符（應為『通道數 間距』）：{lines[0]!r}")
    spacing = float(header[1])

    shots: dict[int, float] = {}
    for ln in lines[1:]:
        parts = ln.split()
        if len(parts) < 2:
            continue
        shots[int(parts[0])] = float(parts[1]) * spacing
    if not shots:
        raise ValueError(f"幾何檔中沒有任何炮點紀錄：{path}")
    return shots


def load_segy(path: str | Path) -> Stream:
    """讀 SEG-Y，幾何直接取自道檔頭（本測線的 SEG-Y 已套好幾何）。"""
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"找不到 SEG-Y 檔：{path}")

    stream = _read_segy(str(path), unpack_trace_headers=True)
    geoms = []
    for tr in stream:
        h = tr.stats.segy.trace_header
        geoms.append(Geometry(
            ffid=int(h.original_field_record_number),
            channel=int(h.trace_number_within_the_original_field_record),
            shot_x=float(h.source_coordinate_x),
            receiver_x=float(h.group_coordinate_x)))
    return _attach(stream, geoms)


def load_seg2(path: str | Path, shot_x: float | None = None,
              geom: dict[int, float] | None = None,
              survey: Survey = DEFAULT_SURVEY) -> Stream:
    """讀單一 SEG-2 檔，並以正確幾何覆蓋檔頭中的預設值。

    炮點座標的取得順序：明確給定的 `shot_x` > `geom` 字典 > 由炮號推算。
    受波器座標一律由 `survey` 重建（檔頭的 1 m 間距是錯的）。
    """
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"找不到 SEG-2 檔：{path}")

    stream = read(str(path), format="SEG2")
    ffid = int(stream[0].stats.seg2.get("SHOT_SEQUENCE_NUMBER", path.stem))

    if shot_x is None:
        if geom is not None and ffid in geom:
            shot_x = geom[ffid]
        else:
            index = ffid - survey.first_ffid
            if not 0 <= index < survey.n_shots:
                raise ValueError(
                    f"炮號 {ffid} 超出預期範圍，請改用 shot_x 或 geom 指定炮點位置")
            shot_x = index * survey.shot_spacing

    xs = survey.receiver_x
    if len(stream) != len(xs):
        raise ValueError(
            f"{path.name} 有 {len(stream)} 道，但 Survey 設定為 {len(xs)} 道")

    geoms = [Geometry(ffid=ffid, channel=i + 1, shot_x=float(shot_x),
                      receiver_x=x) for i, x in enumerate(xs)]
    return _attach(stream, geoms)


def load_seg2_dir(directory: str | Path, geom_path: str | Path | None = None,
                  survey: Survey = DEFAULT_SURVEY) -> Stream:
    """讀整個 seg2 目錄（101.dat ... 112.dat），合併成一個 Stream。"""
    directory = Path(directory)
    files = sorted(directory.glob("*.dat"))
    if not files:
        raise FileNotFoundError(f"{directory} 裡沒有任何 .dat 檔")

    geom = parse_geom(geom_path) if geom_path else None
    out = Stream()
    for f in files:
        out += load_seg2(f, geom=geom, survey=survey)
    return out


def shot_gather(stream: Stream, ffid: int) -> Stream:
    """取出單一炮的紀錄，依支距由小到大排序。"""
    traces = [tr for tr in stream if tr.stats.utels.ffid == ffid]
    if not traces:
        raise ValueError(f"Stream 中沒有炮號 {ffid} 的資料")
    return Stream(sorted(traces, key=lambda t: t.stats.utels.offset))


def ffids(stream: Stream) -> list[int]:
    """回傳 Stream 中所有炮號（已排序、去重）。"""
    return sorted({tr.stats.utels.ffid for tr in stream})
