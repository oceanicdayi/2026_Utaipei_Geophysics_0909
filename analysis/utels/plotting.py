# -*- coding: utf-8 -*-
"""繪圖：炮集、頻譜、訊噪比、走時曲線、互換時間。

所有函式都回傳 matplotlib Figure，由呼叫端決定要存檔還是顯示。
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
import numpy as np
from matplotlib import font_manager
from matplotlib import pyplot as plt
from obspy import Stream

from .config import DEFAULT_SURVEY, Survey
from .preprocess import agc, normalise, time_axis

# 中文字型：依序嘗試常見的系統字型，找不到就退回預設
# （圖仍然可用，只是中文會變成方框）
_CJK_CANDIDATES = [
    "Microsoft JhengHei", "Microsoft YaHei", "PingFang TC",
    "Noto Sans CJK TC", "Noto Sans TC", "SimHei", "Arial Unicode MS",
]


def setup_fonts():
    """設定可顯示中文的字型，回傳實際採用的字型名稱（找不到回傳 None）。"""
    available = {f.name for f in font_manager.fontManager.ttflist}
    for name in _CJK_CANDIDATES:
        if name in available:
            # 後備字型很重要：中文字型通常沒有 U+2212（數學減號），
            # 對數軸刻度 10^-1 之類的 mathtext 會因此畫成空白方框。
            matplotlib.rcParams["font.family"] = [name, "DejaVu Sans"]
            matplotlib.rcParams["axes.unicode_minus"] = False
            matplotlib.rcParams["mathtext.fontset"] = "dejavusans"
            return name
    return None


def plot_shot_gather(gather: Stream, title=None, tmax: float = 0.15,
                     use_agc: bool = False, gain: float = 1.4,
                     fill: bool = True):
    """單炮的 wiggle / variable-area 圖：橫軸支距、縱軸時間（向下）。

    use_agc=True 會對每一道做自動增益。遠支距的振幅只有近支距的
    幾十分之一，不做 AGC 的話遠道在圖上幾乎是一條直線。
    """
    if len(gather) == 0:
        raise ValueError("gather 是空的")

    fig, ax = plt.subplots(figsize=(9, 7))
    spacing = DEFAULT_SURVEY.receiver_spacing
    n_show = int(tmax / gather[0].stats.delta)

    for tr in gather:
        t = time_axis(tr)[:n_show] * 1000.0
        data = tr.data[:n_show].astype(float)
        data = agc(data, 80) if use_agc else data
        data = normalise(data)
        x = tr.stats.utels.offset
        wave = np.clip(data, -1.3, 1.3) * gain * spacing / 2.0 + x
        ax.plot(wave, t, color="k", linewidth=0.5)
        if fill:
            ax.fill_betweenx(t, x, wave, where=(wave > x), color="k",
                             linewidth=0)

    ax.set_xlabel("支距 offset (m)")
    ax.set_ylabel("時間 time (ms)")
    ax.set_ylim(tmax * 1000.0, 0)
    ax.grid(alpha=0.25)
    if title:
        ax.set_title(title)
    fig.tight_layout()
    return fig


def plot_gather_overview(stream: Stream, ffid_list, tmax: float = 0.15,
                         ncols: int = 4):
    """把所有炮集排成一張總覽圖。"""
    from .loader import shot_gather

    nrows = int(np.ceil(len(ffid_list) / ncols))
    fig, axes = plt.subplots(nrows, ncols, figsize=(4.0 * ncols, 3.4 * nrows),
                             sharex=True, sharey=True)
    axes = np.atleast_1d(axes).ravel()
    n_show = int(tmax / stream[0].stats.delta)

    for ax, ffid in zip(axes, ffid_list):
        gather = shot_gather(stream, ffid)
        for tr in gather:
            t = time_axis(tr)[:n_show] * 1000.0
            data = normalise(agc(tr.data[:n_show].astype(float), 80))
            ax.plot(np.clip(data, -1.3, 1.3) * 1.3 + tr.stats.utels.offset,
                    t, color="k", linewidth=0.35)
        shot_x = gather[0].stats.utels.shot_x
        ax.set_title("FFID %d . 炮點 %.0f m" % (ffid, shot_x), fontsize=10)
        ax.set_ylim(tmax * 1000.0, 0)
        ax.grid(alpha=0.25)

    for ax in axes[len(ffid_list):]:
        ax.set_visible(False)

    fig.supxlabel("支距 offset (m)")
    fig.supylabel("時間 time (ms)")
    fig.tight_layout()
    return fig


def plot_spectrum(stream: Stream, offsets=(2, 10, 20, 30), tmax: float = 0.2):
    """幾個代表性支距的振幅頻譜，用來決定帶通頻帶。"""
    fig, ax = plt.subplots(figsize=(9, 5))
    n_show = int(tmax / stream[0].stats.delta)

    for target in offsets:
        candidates = [tr for tr in stream
                      if abs(tr.stats.utels.abs_offset - target) < 1e-6]
        if not candidates:
            continue
        tr = candidates[0]
        data = tr.data[:n_show].astype(float)
        data = data - data.mean()
        spectrum = np.abs(np.fft.rfft(data * np.hanning(len(data))))
        freq = np.fft.rfftfreq(len(data), tr.stats.delta)
        peak = spectrum.max()
        if peak > 0:
            # 以 dB 表示（而非對數座標軸）：震測慣用，且避免對數刻度
            # 需要 mathtext 繪製 10^-1，中文字型缺少該字元會畫成方框
            decibel = 20.0 * np.log10(np.maximum(spectrum / peak, 1e-6))
            ax.plot(freq, decibel, linewidth=1.2, label="支距 %.0f m" % target)

    ax.set_xlim(0, 500)
    ax.set_ylim(-70, 2)
    ax.set_xlabel("頻率 frequency (Hz)")
    ax.set_ylabel("相對振幅 relative amplitude (dB)")
    ax.set_title("振幅頻譜：低頻為表面波，初達 P 波能量集中在較高頻")
    ax.grid(alpha=0.3, which="both")
    ax.legend()
    fig.tight_layout()
    return fig


def plot_snr(stream: Stream, bins, survey: Survey = DEFAULT_SURVEY):
    """訊噪比隨支距的變化。"""
    from .quality import stream_snr

    snr = stream_snr(stream, survey)
    offsets = np.array([tr.stats.utels.abs_offset for tr in stream])

    fig, ax = plt.subplots(figsize=(9, 5.5))
    good = snr >= survey.usable_threshold_db
    ax.scatter(offsets[good], snr[good], s=16, alpha=0.5, color="#557a69",
               label="SNR >= %.0f dB" % survey.usable_threshold_db)
    ax.scatter(offsets[~good], snr[~good], s=16, alpha=0.5, color="#c2653f",
               label="SNR < %.0f dB" % survey.usable_threshold_db)
    if bins:
        ax.plot([b[0] for b in bins], [b[1] for b in bins], "o-",
                color="#1d2c26", linewidth=2.2, markersize=5,
                label="每 4 m 中位數")
    ax.axhline(12, linestyle="--", color="#9aa39e", linewidth=1.4)
    ax.text(ax.get_xlim()[1], 12.8, "12 dB 可用門檻 ", ha="right",
            fontsize=9, color="#6a716e")

    ax.set_xlabel("|支距| |offset| (m)")
    ax.set_ylabel("訊噪比 SNR (dB)")
    ax.set_title("訊噪比隨支距衰減：鐵鎚震源的能量極限")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    return fig


def plot_travel_time(picks, bins=None, model=None, xmax: float = 26.0,
                     tmax: float = 60.0, min_count: int = 10):
    """t-x 走時圖：散點為個別挑選，粗線為分組中位數。"""
    fig, ax = plt.subplots(figsize=(9, 6))

    x = np.array([p.abs_offset for p in picks])
    t = np.array([p.time for p in picks]) * 1000.0
    ax.scatter(x, t, s=18, alpha=0.5, color="#7d9a68", label="自動挑選（個別道）")

    for velocity, colour in [(300, "#c2653f"), (600, "#557a69")]:
        x_end = min(xmax, tmax / 1000.0 * velocity)
        ax.plot([0, x_end], [0, x_end / velocity * 1000.0], "--",
                color=colour, linewidth=1.3, alpha=0.8,
                label="%d m/s 參考線" % velocity)

    if bins:
        solid = [b for b in bins if b[2] >= min_count and b[0] <= xmax]
        weak = [b for b in bins if b[2] < min_count and b[0] <= xmax]
        if solid:
            ax.plot([b[0] for b in solid], [b[1] * 1000.0 for b in solid],
                    "o-", color="#1d2c26", linewidth=2.5, markersize=6,
                    label="分組中位數（>=%d 道）" % min_count)
            for b in solid:
                ax.annotate("%.0f" % b[3], (b[0], b[1] * 1000.0),
                            textcoords="offset points", xytext=(0, 9),
                            ha="center", fontsize=8, color="#1d2c26")
        if weak:
            ax.plot([b[0] for b in weak], [b[1] * 1000.0 for b in weak], "o",
                    markerfacecolor="none", markeredgecolor="#9aa39e",
                    markersize=7, label="資料不足（<%d 道）" % min_count)

    if model is not None:
        xs = np.linspace(0, xmax, 100)
        ax.plot(xs, xs / model.v1 * 1000.0, "-", color="#557a69",
                linewidth=1.6, alpha=0.9, label="擬合：直達波")
        ax.plot(xs, (model.intercept + xs / model.v2) * 1000.0, "-",
                color="#d69a49", linewidth=1.6, alpha=0.9, label="擬合：折射波")
        ax.axvline(model.crossover, color="#c9c9c2", linestyle=":",
                   linewidth=1.5)

    ax.set_xlim(0, xmax)
    ax.set_ylim(0, tmax)
    ax.set_xlabel("|支距| |offset| (m)")
    ax.set_ylabel("初達波到時 first-arrival time (ms)")
    ax.set_title("t-x 走時曲線（數字為該分組的視速度 m/s）")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)
    fig.tight_layout()
    return fig


def plot_travel_time_by_shot(picks):
    """每一炮各畫一條走時曲線，用來目視檢查一致性。"""
    fig, ax = plt.subplots(figsize=(10, 6))
    shots = sorted({p.ffid for p in picks})
    colours = plt.cm.turbo(np.linspace(0, 1, len(shots)))

    for colour, ffid in zip(colours, shots):
        subset = sorted([p for p in picks if p.ffid == ffid],
                        key=lambda p: p.receiver_x)
        if not subset:
            continue
        ax.plot([p.receiver_x for p in subset],
                [p.time * 1000.0 for p in subset], "o-", markersize=3.5,
                linewidth=0.9, color=colour, label="FFID %d" % ffid)
        ax.axvline(subset[0].shot_x, color=colour, alpha=0.25, linewidth=1,
                   linestyle=":")

    ax.set_xlabel("受波器位置 receiver x (m)")
    ax.set_ylabel("到時 time (ms)")
    ax.set_title("逐炮走時曲線（虛線為各自的炮點位置）")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=7, ncol=2)
    fig.tight_layout()
    return fig


def plot_reciprocity(pairs):
    """互換時間檢核圖：理論上所有點都應落在 1:1 線上。"""
    fig, ax = plt.subplots(figsize=(6.4, 6))
    if pairs:
        a = np.array([p.t_ab for p in pairs]) * 1000.0
        b = np.array([p.t_ba for p in pairs]) * 1000.0
        limit = max(a.max(), b.max()) * 1.1
        ax.plot([0, limit], [0, limit], "--", color="#9aa39e", linewidth=1.3,
                label="1:1（理論上應相等）")
        ax.scatter(a, b, s=36, alpha=0.75, color="#557a69")
        ax.set_xlim(0, limit)
        ax.set_ylim(0, limit)
        median = np.median(np.abs(a - b))
        ax.set_title("互換時間檢核：%d 組配對，中位差 %.1f ms"
                     % (len(pairs), median))
    else:
        ax.set_title("互換時間檢核：沒有可用的配對")

    ax.set_xlabel("A 打 B 的到時 (ms)")
    ax.set_ylabel("B 打 A 的到時 (ms)")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    return fig


def save(fig, path, dpi: int = 130):
    """存圖並關閉 Figure，回傳實際路徑。"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    return path
