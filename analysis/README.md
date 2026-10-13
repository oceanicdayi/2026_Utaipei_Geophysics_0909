# 202610_UTELS 折射震測資料分析

以 **ObsPy** 為基礎的淺層折射震測分析程式：讀檔、繪圖、資料品質檢核、初達波自動挑選、走時分析與兩層模型反演。

資料來源：2026-10-07 臺北市立大學圖書館後方折射震測實習（12 炮 × 24 道 = 288 道）。

---

## 目錄

1. [環境安裝](#1-環境安裝)
2. [快速開始](#2-快速開始)
3. [五個分析步驟](#3-五個分析步驟)
4. [程式架構說明](#4-程式架構說明)
5. [關鍵設計決策](#5-關鍵設計決策)
6. [自己寫分析程式](#6-自己寫分析程式)
7. [測試](#7-測試)
8. [疑難排解](#8-疑難排解)

---

## 1. 環境安裝

需要 **Python 3.9 以上**。三種方式擇一。

### 方式 A：conda（最推薦）

ObsPy 依賴不少編譯好的科學套件，用 conda 安裝最不容易出問題。

```bash
# 1. 安裝 Miniconda（已安裝可跳過）
#    https://docs.conda.io/en/latest/miniconda.html

# 2. 建立環境
conda env create -f environment.yml

# 3. 啟用
conda activate utels

# 4. 確認
python -c "import obspy; print('ObsPy', obspy.__version__)"
```

### 方式 B：pip + 虛擬環境

```bash
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 方式 C：直接裝在系統 Python（不建議，但最快）

```bash
pip install obspy numpy scipy matplotlib
```

### 安裝驗證

```bash
python -c "import obspy, numpy, scipy, matplotlib; print('全部就緒')"
```

### 中文字型

圖上的標籤是中文。程式會自動尋找系統中可用的中文字型：

| 作業系統 | 通常已內建 |
|---|---|
| Windows | Microsoft JhengHei（微軟正黑體） |
| macOS | PingFang TC |
| Linux | 多半要自行安裝 |

Linux 安裝字型：

```bash
sudo apt install fonts-noto-cjk          # Debian / Ubuntu
rm -rf ~/.cache/matplotlib               # 清掉 matplotlib 的字型快取
```

找不到字型時程式會印出提醒，圖仍然會產生，只是中文變成方框。

---

## 2. 快速開始

```bash
cd analysis
python scripts/run_all.py
```

約一分鐘跑完，所有圖檔與 CSV 會輸出到 `figures/`。

預設讀取專案根目錄的 `202610_UTELS.sgy`。檔案放別處時：

```bash
python scripts/run_all.py --segy /path/to/202610_UTELS.sgy --out /path/to/output
```

改用 SEG-2 原始檔（需要 `.geom` 提供正確幾何）：

```bash
python scripts/run_all.py --use-seg2 --seg2 ../seg2 --geom ../202610_UTELS.geom
```

---

## 3. 五個分析步驟

這五步是有順序的。**先確認資料品質，再決定能做什麼分析**——這是整套流程最重要的觀念。

### Step 1 — 把資料畫出來

```bash
python scripts/01_plot_gathers.py                   # 全部 12 炮
python scripts/01_plot_gathers.py --shots 101 107   # 只畫指定炮
python scripts/01_plot_gathers.py --no-filter       # 不濾波
python scripts/01_plot_gathers.py --tmax 0.3        # 看更長的時間
```

產出：

| 檔案 | 內容 |
|---|---|
| `gather_101.png` … `gather_112.png` | 每一炮的 wiggle／variable-area 圖 |
| `gather_raw.png` / `gather_filtered.png` | 濾波前後對照 |
| `gathers_overview.png` | 12 炮總覽 |
| `spectrum.png` | 代表性支距的振幅頻譜 |

**怎麼看**：橫軸是支距、縱軸是時間（向下增加）。從左下往右上展開的強能量扇形就是**表面波（ground roll）**，視速度只有約 127 m/s。初達波在它的上方（更早），振幅小很多。

### Step 2 — 資料品質檢核

```bash
python scripts/02_data_quality.py
```

計算每一道的訊噪比，並找出可信的支距上限。這一步會告訴你：

```
  SNR >= 25 dB：206 道 (72%)
  中位訊噪比從 32 m 起低於 12 dB，超過此距離的初達波已埋在雜訊中。
```

產出 `snr_vs_offset.png` 與 `snr_table.csv`。

### Step 3 — 初達波自動挑選

```bash
python scripts/03_pick_first_breaks.py
python scripts/03_pick_first_breaks.py --check-shots 101 104 107 110
```

產出 `first_breaks.csv`（每道的到時、視速度、SNR、是否可信）與 `picks_on_gather_*.png`。

> **一定要打開 `picks_on_gather_*.png`。** 紅點代表 SNR 足夠的挑選，橘點代表需要人工覆核。你會看到有些紅點明顯落在錯的位置——這就是為什麼自動挑選只能當基線。

### Step 4 — 走時分析與反演

```bash
python scripts/04_travel_time.py
```

做三件事：

1. **互換時間檢核** — A 打 B 與 B 打 A 的走時理論上必須相等。這是折射震測最重要的自我檢核。
2. **分組統計** — 每 2 m 取中位到時與視速度。
3. **擬合比較** — 同時做單一直線與兩段擬合，比較殘差。

目前這組自動挑選的輸出是：

```
單一直線擬合：視速度 470 m/s，截距 1.4 ms，殘差 rms 11.1 ms
兩段擬合：找不到滿足物理門檻的解（V2 需比 V1 快 5% 以上，截距需 >= 0.1 ms）。
  => 這組自動挑選結果不足以支撐兩層模型。
     必須人工逐道判讀初達波後再重做。
```

**這是誠實的結果，不是程式壞了。** 程式刻意不會在資料撐不住時硬湊一個 V₁／V₂／深度出來。個別道的離散太大，不足以定出可靠的斜率。要得到可辯護的模型，必須人工逐道判讀。

哪些分組可以採信、哪些不行，由 Step 5 回答。

### Step 5 — 挑選參數的敏感度測試

```bash
python scripts/05_sensitivity.py
```

這一步回答一個容易被忽略、但會毀掉整個結論的問題：**我得到的數字，是資料給的，還是我的參數給的？**

挑選器用視速度視窗限制搜尋範圍。支距愈小，這個視窗愈窄——支距 2 m、下限 180 m/s 時，視窗只有 0.8 到 11 ms。近支距的「挑選結果」很可能只是視窗本身的位置。

程式把視窗下限掃過 160–300 m/s，看每個支距分組的視速度變動多少：

```
    支距    160    180    200    220    250    300      變動  判定
   2 m    286    320    333    348    381    533     67%  不穩定 <-- 不可用
   4 m    296    311    381    451    508    525     55%  不穩定 <-- 不可用
   6 m    333    358    414    353    774    774     88%  不穩定 <-- 不可用
   8 m    547    547    547    533    547    557      4%  穩定
  10 m    533    533    533    556    556    556      4%  穩定
  12 m    578    578    589    589    589    589      2%  穩定
  14 m    569    571    571    593    602    619      9%  穩定
  16 m    587    587    587    634    634    688     16%  不穩定 <-- 不可用
```

結論：

- **支距 8–14 m**：視速度穩定在 **約 530–620 m/s**，不隨參數變動，可以採信。
- **支距 < 8 m**：完全被參數主導。**自動挑選無法決定近支距的直達波速度 V₁**——而 V₁ 正是兩層模型的一半答案。這一段只能人工判讀。
- **支距 > 14 m**：訊噪比已經不足（見 Step 2），挑選本身不可靠。

這就是為什麼本套程式不輸出 V₁／V₂／深度：**自動挑選只拿得到折射段的一部分，拿不到直達波段。**

---

## 4. 程式架構說明

```
analysis/
├── utels/                  核心套件（可被其他程式 import）
│   ├── config.py           觀測參數與分析預設值
│   ├── loader.py           讀 SEG-Y / SEG-2，掛上正確幾何
│   ├── preprocess.py       去趨勢、帶通、AGC、正規化
│   ├── picking.py          初達波挑選（AIC、STA/LTA）
│   ├── quality.py          訊噪比、互換時間
│   ├── inversion.py        截距時間法兩層反演
│   └── plotting.py         所有繪圖
├── scripts/                可直接執行的五個步驟
├── tests/                  單元測試
└── figures/                產出（執行後才會出現）
```

### 各模組重點

**`config.py`** — `Survey` 是一個 frozen dataclass，把所有觀測參數集中在一處。想改分析參數，改這裡，不要散落到各處。

```python
from utels import Survey
s = Survey()
s.spread            # (0.0, 46.0) — 受波器展距
s.shot_x            # [0, 4, 8, ..., 44] — 炮點位置
s.bandpass_low      # 40.0 Hz
```

**`loader.py`** — 讀檔後把幾何掛在 `tr.stats.utels`：

```python
tr.stats.utels.ffid         # 炮號 101-112
tr.stats.utels.shot_x       # 炮點座標 (m)
tr.stats.utels.receiver_x   # 受波器座標 (m)
tr.stats.utels.offset       # 帶正負號的支距 (m)
tr.stats.utels.abs_offset   # |支距| (m)
```

**`picking.py`** — `Pick` 是 frozen dataclass，含到時、SNR 與衍生的視速度。

**`inversion.py`** — `fit_two_layer()` 在資料不支援兩層模型時回傳 `None`，而不是硬給一組數字。

---

## 5. 關鍵設計決策

這幾個決定直接影響結果，值得理解。

### 為什麼帶通是 40–400 Hz？

原始資料未經任何儀器端濾波，含有：

- **2–16 Hz**：低頻漂移，振幅極大，會淹沒一切
- **20–40 Hz**：表面波主頻
- **較高頻**：初達 P 波

40 Hz 高通可同時壓掉漂移與大部分表面波能量。打開 `spectrum.png` 可以自己確認這些頻帶。

濾波使用**零相位**（`zerophase=True`）。單向濾波會讓波形整體延遲，直接污染到時判讀——這會讓你算出來的速度系統性偏慢。

### 為什麼挑選器要限制視速度範圍？

本測線能量最強的是約 127 m/s 的表面波。任何「找最大能量」的演算法（包括常見的 STA/LTA）都會挑到它，而不是初達波。

解法是在時間軸上開一個視窗，只搜尋視速度介於 **180–2500 m/s** 的範圍。180 m/s 刻意高於表面波的 127 m/s，等於把表面波排除在搜尋範圍之外。

```python
# utels/config.py
vel_search_max: float = 2500.0
vel_search_min: float = 180.0
```

### 為什麼用 AIC 而不是 STA/LTA？

AIC 找的是「雜訊段與訊號段統計性質差異最大」的分割點，對振幅變化平緩的弱初達波較穩健。STA/LTA 需要調門檻，且對本資料容易誤觸發。`picking.sta_lta()` 仍保留，可自行比較。

### 為什麼炮集圖預設不做 AGC？

AGC 會連初達波之前的雜訊一起放大，起跳點反而消失。預設只對每道除以自身最大振幅。想比較的話：

```python
plot_shot_gather(gather, use_agc=True)
```

### 為什麼讀 SEG-2 一定要給 `.geom`？

`seg2/*.dat` 的檔頭幾何是**儀器預設值**，不是現場幾何：

| 檔頭欄位 | 檔案裡寫的 | 實際現場 |
|---|---|---|
| `RECEIVER_LOCATION` | 0–23（間距 1 m） | 0–46 m（間距 **2 m**） |
| `SOURCE_LOCATION` | 每個檔都是 `4.00` | 0, 4, 8, …, 44 m |

直接信任檔頭會讓所有距離差兩倍，速度也跟著錯兩倍。`load_seg2()` 一律用 `Survey` 重建受波器座標，炮點則取自 `.geom`。SEG-Y 的檔頭已經套好正確幾何，可直接使用。

---

## 6. 自己寫分析程式

`utels` 是一般的 Python 套件，可以直接 import 來做自己的分析。

```python
import sys
sys.path.insert(0, "analysis")        # 或把 analysis/ 加進 PYTHONPATH

from utels import load_segy, bandpass, pick_stream, fit_two_layer
from utels.loader import shot_gather
from utels.plotting import setup_fonts, plot_shot_gather, save

setup_fonts()

# 讀檔 + 濾波
stream = load_segy("202610_UTELS.sgy")
work = bandpass(stream, freqmin=50, freqmax=300)   # 自己調頻帶

# 畫第 7 炮
fig = plot_shot_gather(shot_gather(work, 107), title="FFID 107", tmax=0.12)
save(fig, "my_gather.png")

# 挑初達波
picks = pick_stream(work)
good = [p for p in picks if p.snr >= 35]           # 自己調門檻
print(f"可用 {len(good)} 道")

# 反演
import numpy as np
model = fit_two_layer(np.array([p.abs_offset for p in good]),
                      np.array([p.time for p in good]))
print(model.describe() if model else "資料不支援兩層模型")
```

### 用自己人工挑的到時做反演

這才是真正該做的事。把你的到時整理成兩個陣列即可：

```python
import numpy as np
from utels.inversion import fit_two_layer, fit_single_line

offsets = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])        # m
times = np.array([7, 13, 18, 21, 24, 27, 30, 33, 36, 39]) / 1000  # s

model = fit_two_layer(offsets, times)
if model:
    print(model.describe())
    print(f"界面深度 {model.depth:.2f} m")
else:
    print("這組資料不支援兩層模型")
```

也可以直接讀 Step 3 產生的 CSV 回來改：

```python
import csv
with open("figures/first_breaks.csv", encoding="utf-8-sig") as fh:
    rows = [r for r in csv.DictReader(fh) if r["reliable"] == "Y"]
offsets = np.array([abs(float(r["offset_m"])) for r in rows])
times = np.array([float(r["pick_ms"]) for r in rows]) / 1000
```

---

## 7. 測試

```bash
pip install -r requirements-dev.txt
pytest                                      # 全部測試
pytest --cov=utels --cov-report=term-missing   # 含覆蓋率
```

測試涵蓋：截距時間法公式（與手算對照）、以合成資料驗證反演能否還原已知模型、單層資料必須回傳 `None`、AIC 挑選器、互換時間配對、前處理的邊界情況（全零道、過短視窗）。

---

## 8. 疑難排解

### `ModuleNotFoundError: No module named 'obspy'`

虛擬環境沒啟用，或裝到別的 Python。確認：

```bash
python -c "import sys; print(sys.executable)"
pip install -r requirements.txt
```

### `ModuleNotFoundError: No module named 'utels'`

從 `analysis/` 目錄執行腳本：

```bash
cd analysis
python scripts/01_plot_gathers.py
```

`scripts/_common.py` 會自動把上一層加進 `sys.path`。

### 圖上的中文變成方框

系統缺中文字型。見 [中文字型](#中文字型)。

### Windows 終端機出現 `UnicodeEncodeError`

Windows 預設 cp950 編碼。程式已呼叫 `use_utf8_console()` 處理，若仍發生：

```powershell
$env:PYTHONIOENCODING = "utf-8"
python scripts/run_all.py
```

### `FileNotFoundError: 找不到 SEG-Y 檔`

用 `--segy` 指定實際路徑：

```bash
python scripts/run_all.py --segy "D:\path\to\202610_UTELS.sgy"
```

### 算出來的速度差兩倍

幾乎可以確定是讀了 SEG-2 卻沒給 `.geom`。見[為什麼讀 SEG-2 一定要給 `.geom`](#為什麼讀-seg-2-一定要給-geom)。

### 兩段擬合一直回傳 `None`

這通常不是程式問題，而是挑選結果離散太大。依序檢查：

1. 打開 `picks_on_gather_*.png`，確認紅點真的在初達波上
2. 看 `reciprocity.png`，離 1:1 線很遠的點代表該組挑錯了
3. 看 `sensitivity.png`，確認你要用的支距範圍對參數穩定
4. 提高 `Survey.snr_threshold_db`，只留最可信的道
5. 人工重挑近支距的直達波段——這一段自動挑選做不到

---

## 參考

- ObsPy 文件：<https://docs.obspy.org/>
- 資料與觀測參數說明：專案根目錄的 `README.md`
- 當天的探究歷程：<https://oceanicdayi.github.io/2026_Utaipei_Geophysics_0909/seismic-inquiry/>
