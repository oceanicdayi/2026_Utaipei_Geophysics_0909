# 地球物理概論
> 來源：Hugging Face Space `oceanicdayi/Geophysics_day1`  
> 擷取日期：2026-09-09  
> 原頁面：https://huggingface.co/spaces/oceanicdayi/Geophysics_day1

一個探索我們星球內在奧秘的互動式指南

---

## 地球物理是什麼？

地球物理學是應用物理學原理來研究地球的科學。它結合了地質學的觀察與物理學的量化分析，讓我們能夠「看見」地表之下的世界。

---

## 使用哪些方法？

地球物理技術通過測量地表的物理性質來推斷地下的結構。主要可分為地震、位能場與熱流三大類方法。

| 技術分類 | 主要方法 | 測量性質 | 研究性質 |
|---|---|---|---|
| 地震方法 (SEISMIC) | 天然/人工震源 | 地震動 | 波速(V), 衰減(Q), 密度(ρ) |
|  |  |  | 利用震波傳播特性繪製地下結構，最為直接。 |
| 位能場方法 (POTENTIAL) | 重力法 / 磁力法 | 重力加速度(g) / 磁場(F) | 密度(ρ) / 磁化率(χ) |
|  |  |  | 測量地球天然場的微小變化，適合大範圍普查。 |
| 熱流方法 (HEAT FLOW) | 地溫測量 | 地溫梯度(∂T/∂z) | 熱導率(k), 熱流(q) |
|  |  |  | 研究地球內部熱量的傳導與分布。 |

---

## 如何解譯地球物理資料？

從觀測數據到地下地質模型，我們主要使用兩種互補的解譯方法：正演模擬與反演。

### 正演模擬 (Forward Modeling)

**問：「如果地下長這樣，我會測到什麼？」**

正演是基於一個假設的地下模型，計算其理論響應，並與實際觀測數據比較。解譯者反覆調整模型，直到理論與觀測匹配為止。

![圖 1.7 正演模擬範例](https://huggingface.co/spaces/oceanicdayi/Geophysics_day1/resolve/main/1000029378.jpg)

**圖 1.7 正演模擬範例：** (a) 觀測重力異常。(b) 根據初始模型預測異常。(c) 調整模型直到預測曲線與觀測曲線吻合。

### 反演 (Inversion)

**問：「我測到了這些數據，造成它的地下結構是什麼？」**

反演是將觀測數據作為輸入，通過數學演算法直接求解，從而產生一個能夠解釋這些數據的地下模型。

![圖 1.6 反演範例](https://huggingface.co/spaces/oceanicdayi/Geophysics_day1/resolve/main/1000029377.jpg)

**圖 1.6 反演範例：** (a) 觀測原始地震數據。(b) 建立走時圖。(c) 套入反演公式。(d) 獲得最終的地層速度與厚度模型。

---

## 解譯的黃金法則：約束 (Constraints)

地球物理是一種間接觀測，因此單一數據可能有多種解釋。為了得到最可靠的結論，我們必須使用**約束條件**來縮小解釋的可能性。這些約束可分為三個層級：

#### 第一級：硬約束 (Firm Constraints)

可以直接觸摸和測量的證據，是解譯的基石。例如：地表岩石露頭樣本、鑽井岩芯。

#### 第二級：軟約束 (Softer Constraints)

基於直接證據的合理推斷。例如：根據有限的鑽井繪製的地質圖、其他種類的地球物理數據（如用震測剖面來約束重力模型）。

#### 第三級：合理解釋 (Reasonable Assumptions)

基於地質邏輯和常識的理論假設。例如：此地區的地質構造是否合理？

---

## 綜合範例：一個重力模型的誕生

下面這個例子完美展示了如何整合所有資訊，建立一個可靠的地球物理模型。

![綜合範例圖解](https://huggingface.co/spaces/oceanicdayi/Geophysics_day1/resolve/main/1000029379.jpg)

### a) 收集約束條件

首先，我們收集所有可用的數據。圖(a)顯示了觀測到的重力異常曲線，以及各種約束條件：地表露頭、鑽井資料（提供了地下的直接資訊）、地形，甚至還有震測反射剖面（提供了地層の形態）。這些都是我們建立模型時必須尊重的「規則」。

### b) 建立與驗證模型

接著，我們利用正演或反演方法，建立一個符合所有約束條件的地下地質模型（圖 b 下半部）。這個模型為不同地層賦予了合理的密度值(ρ)。最後一步是驗證：我們計算這個模型會產生的理論重力異常（圖 b 上半部的虛線），並發現它與實際觀測到的曲線（實線）高度吻合。這代表我們成功建立了一個受到良好約束、高度可靠的地質解譯。

---

## 在各領域的工程上有何應用？

地球物理方法以其非破壞性、高效率和覆蓋範圍廣的優勢，在多個工程領域中扮演著不可缺的角色。

### 大地與土木工程

**核心目標：** 評估工址的穩定性，探測地基狀況與地質弱帶。

**常用方法：** 地震折射/反射、透地雷達(GPR)、電阻率層析成像(ERT)。

- **案例1：** 在進行隧道開挖前，使用**地震折射法**測定岩盤的深度與完整性，避開破碎帶。
- **案例2：** 在都市區進行管線工程時，利用**透地雷達(GPR)**精確標定現有地下管線的位置，防止誤挖。

範例連結：台20線嘉寶隧道損壞之檢測調查 (PDF)  
http://www.ciche.org.tw/wordpress/wp-content/uploads/2018/03/DB4201-P054-%E5%B1%B1%E5%8D%80%E9%9A%A7%E9%81%93.pdf

### 環境工程

**核心目標：** 調查與監測地下污染物的分布範圍，評估場址的環境風險。

**常用方法：** 電阻率層析成像(ERT)、電磁法(EM)、誘導極化法(IP)。

- **案例1：** 利用**電阻率法(ERT)**圈繪垃圾掩埋場滲出水所造成的地下水污染羽的範圍。
- **案例2：** 使用**電磁法(EM)**快速探測工廠區地下是否有廢棄金屬儲槽或管線洩漏。

範例連結：台中市110年各掩埋場地下水質檢測計畫 (PDF)  
https://www.epb.taichung.gov.tw/

### 水利工程與水文地質

**核心目標：** 尋找地下水資源，描繪含水層的分布與厚度，評估水庫壩基的滲漏風險。

**常用方法：** 電阻率層析成像(ERT)、瞬變電磁法(TEM)、地震折射法。

- **案例1：** 在乾旱地區，使用**瞬變電磁法(TEM)**進行大範圍的地下水普查，快速找到富含地下水的區域。
- **案例2：** 在水庫大壩底部施作**電阻率法(ERT)**監測，以偵測是否有潛在的滲漏通道。

範例連結：新世代水利智慧探勘技術 (水利署)  
https://www.wra.gov.tw/epaper/Article_Detail.aspx?s=9034&n=0

### 考古學

**核心目標：** 以非破壞性的方式探測地下的古代遺址、墓葬、城牆等結構。

**常用方法：** 透地雷達(GPR)、磁力法、電磁法(EM)。

- **案例：** 在古羅馬城市遺址，考古學家利用**磁力法**大範圍掃描，成功發現了因人類活動（如火燒）而留下磁性異常的房舍與街道分布，指導了後續的精準開挖。

範例連結：透地雷達應用於基隆和平島古堡遺址探測 (PDF)  
https://homepage.ntu.edu.tw/~borao/2Profesores/San%20Salvador.pdf

### 資源探勘

**核心目標：** 探測深部的礦產資源與油氣儲庫。

**常用方法：** 反射震測法、重力法、磁力法、誘導極化法(IP)。

- **石油探勘：** 大規模的**反射震測法**是尋找儲油構造（如背斜）最核心的技術，重力和磁力法則用於輔助判斷盆地的整體結構。
- **礦產探勘：** 針對具有導電性的金屬硫化物礦床，**誘導極化法(IP)**是非常有效的探測工具。

範例連結：油氣探採：敲敲地球透視地層 (科技大觀園)  
https://scitechvista.nat.gov.tw/Article/c000008/detail?ID=1b869bec-194a-4e15-890d-e84fb780f1c3

---

## 專題探討：地熱探勘

地熱探勘為了降低鑽井前的高風險與不確定性，會綜合運用多種地球物理方法，如同為地球進行「健康檢查」，以非侵入性的方式描繪地下的熱源、儲集層構造與熱水通道。

以下是幾種關鍵的地球物理探勘方法及其原理：

### 1. 電磁法 (Electromagnetic Methods)

電磁法是地熱探勘中最核心且有效的方法之一，其基本原理是探測地下岩層的「電阻率」（Resistivity）。地熱系統中的熱水通常富含溶解的礦物質（鹽類），使其導電性極佳，呈現出「低電阻」的特性。因此，在地表下找到大規模的低電阻異常區，往往就意味著找到了潛在的熱水儲集層。

#### 大地電磁法 (Magnetotellurics, MT)

這是一種被動式的探測技術。它利用源自太陽風與全球閃電活動等自然現象產生的天然電磁波作為場源。當這些電磁波傳入地下，會因不同岩層的電阻率而產生衰減和相位變化。科學家在地表同步測量電場與磁場的微弱變化，就能反推出從淺至深數公里範圍內的電阻率分布結構，進而描繪出低電標示誌熱水儲集層的影像。

### 2. 磁力法 (Magnetic Method)

磁力法的原理是測量地表磁場的細微變化，這些變化主要由地下岩石的磁性差異引起。在地熱探勘中，其最重要的應用是「居禮點深度 (Curie Point Depth, CPD)」分析。

**原理與應用：** 居禮點是指磁性礦物會失去其鐵磁性的臨界溫度(約攝氏580度)。透過航空磁力測量數據，科學家可以估算出居禮點的深度。在地熱活躍區，因有深部熱源，居禮點深度會異常地淺。因此，尋找淺層居禮點異常是判斷區域熱流高低、尋找潛在地熱熱源的有效工具。

### 3. 震測法 (Seismic Methods)

震測法利用震波在不同地質介質中傳播速度和路徑的特性來描繪地下結構，主要分為主動式與被動式兩種。

#### 反射震測法 (Reflection Seismology)

此方法如同為地層拍攝超音波。使用人工震源在地表激發震波，當震波遇到不同岩層的交界面時，一部分能量會反射回地表，被檢波器記錄下來。透過分析震波的旅行時間，就可以精確繪製出地下的斷層等構造，而這些斷層往往是控制地熱流體上升的關鍵通道。

### 4. 重力法 (Gravity Method)

重力法的原理是利用精密儀器在地表測量重力值的微小差異。這些差異主要由地下不同岩石的密度變化所造成。

**原理與應用：** 在地熱區，深部的岩漿庫或高溫熱源通常密度較低。因此，重力測勘可以幫助定位與地熱活動相關的深部構造、岩漿侵入體（熱源）或大型斷裂帶。重力異常圖可以提供地下地質結構的宏觀圖像，常與其他方法結合使用。

---

**總結來說**，地熱探勘是一項系統工程，通常會結合上述多種地球物理方法，彼此驗證、互補不足，以最少的成本和風險，逐步鎖定最有開發潛力的鑽井目標。

---

## 地球物理資料處理

在開始處理地球物理資料之前，我們需要建置一個合適的科學計算環境。以下提供了兩種主要路徑：**(A) 本機環境安裝**，適合希望深入了解環境配置的學習者；**(B) 雲端 Codespaces 環境**，推薦給所有學生，尤其是初學者，可以跳過繁瑣的安裝步驟，直接開始學習。

### A. 本機環境安裝 (Local Installation)

#### 1. 基礎軟體安裝

請先至官方網站下載並安裝以下兩個基本軟體：

- **程式碼編輯器:** Notepad++ (建議下載 `npp.8.7.Installer.x64.exe` 或更新版本)
- **Python 環境管理器:** Miniconda (建議下載 `Miniconda3-latest-Windows-x86_64.exe`)

#### 2. Conda 環境與套件安裝流程

安裝 Miniconda 後，請從開始功能表開啟「Miniconda Prompt」(或 Anaconda Prompt)，並依照順序複製、貼上並執行以下指令。這將會建立一個名為 `pygmt` 的獨立 Python 環境，並安裝所有核心套件。

```bash
# --- 步驟 1: 設定 Conda 優先頻道 (建議執行) ---
conda config --prepend channels conda-forge

# --- 步驟 2: 建立名為 pygmt 的新環境 ---
conda create --name pygmt python=3.9 numpy pandas xarray netcdf4 packaging gmt

# --- 步驟 3: 啟動 (Activate) 新建立的環境 ---
conda activate pygmt

# --- 步驟 4: 在 pygmt 環境中安裝主要套件 ---
conda install pygmt
conda install obspy
conda install jupyter

# --- 步驟 5: 使用 pip 安裝額外套件 ---
pip install streamlit matplotlib
```

#### 3. Jupyter Notebook 使用教學

安裝好環境後，Jupyter Notebook 是進行資料分析、程式編寫與製作報告的絕佳工具。請在已啟動 `pygmt` 環境的終端機中，輸入 `jupyter notebook` 來啟動。

---

### B. 雲端環境 (GitHub Codespaces) - 推薦

GitHub Codespaces 提供了一個強大的雲端開發環境，讓學生無需在本地電腦安裝複雜的軟體，就能直接在瀏覽器中進行課程實驗與作業，大幅降低了入門門檻。

#### 1. 為什麼用 Codespaces？

- **免安裝：** 學生不用在自己的電腦上掙扎於安裝 Python、ObsPy、PyGMT 等大型套件。
- **環境一致：** 每位學生打開的都是完全相同的雲端環境，避免了「老師的電腦可以跑，我的電腦卻出錯」的常見問題。
- **整合雲端 VSCode：** 直接在瀏覽器中提供功能齊全的 VSCode 編輯器，完美支援程式撰寫、Jupyter Notebook 互動操作與終端機指令。
- **即時協作：** 老師或助教可以透過連結直接進入學生的 Codespace 環境，即時進行指導與除錯。

#### 2. 教學設計與協作流程

##### (A) 老師的準備工作：建立課程模板

老師需要在 GitHub 上建立一個公開 (Public) 的課程專用 Repository，例如 `https://github.com/cwbdayi638/geophysics-class-2025`。這個 Repo 將作為所有學生的課程模板，其中包含：

```text
geophysics-class-2025/
├── .devcontainer/
│   └── devcontainer.json  # Codespaces 環境設定檔
├── data/                  # 存放地震資料 (miniSEED, CSV 等)
├── notebooks/             # 存放 Jupyter Notebook 範例
└── hw/                    # 存放作業說明與範例
```

最重要的部分是 `.devcontainer/devcontainer.json` 檔案，它定義了 Codespace 啟動時的環境配置。老師可以在此指定所需的 Python 版本、要自動安裝的套件，以及推薦安裝的 VSCode 擴充功能。

##### (B) 🧭 學生的操作流程：Fork 與 Pull Request

這套流程非常適合大班課程，老師只需維護一個公開 Repo，學生即可透過 Fork 功能建立個人副本來完成作業。

1. **Fork 課程 Repo：** 進入老師提供的課程 Repo 網址 `https://github.com/cwbdayi638/geophysics-class-2025`，點擊右上角的 **Fork** 按鈕，在自己的帳號下生成一份完全相同的副本。
2. **建立 Codespace：** 進入自己帳號下的 Fork Repo，點擊綠色的 **<> Code** 按鈕 → **Create codespace on main**，等待約 1-2 分鐘讓雲端環境自動安裝完成。
3. **完成作業：** 在 Codespace 中，打開 `notebooks/` 或 `hw/` 資料夾，編寫程式碼與 Notebook。完成後，使用終端機儲存並推送 (push) 變更到自己的 Fork Repo。

```bash
git add .
git commit -m "完成 HW1"
git push
```

4. **繳交作業 (建立 Pull Request)：**
   - 回到 GitHub 上自己的 Fork Repo 頁面，會看到一個 "This branch is 1 commit ahead of..." 的提示，點擊右側的 **Contribute → Open pull request**。
   - 確認 Base Repository 是老師的 Repo，而 Head Repository 是自己的 Fork Repo。
   - 仔細填寫 PR 的標題與內容，說明作業目的、方法、附上結果圖，並寫下自己的觀察與討論。
   - 點擊 **Create pull request**，即可將作業繳交給老師。
5. **接收批改與回饋：** 老師會在 PR 頁面中直接留言、批准作業 (Approve) 或要求修改 (Request changes)。如果需要修改，只需在 Codespace 中更新程式碼並再次 Push，PR 的內容就會自動更新。

##### ✅ 學生流程總結

1. **Fork** 老師的 Repo
2. 在自己的 **Fork Repo** 開 **Codespace** 完成作業
3. **Commit & Push** 到自己的 Fork Repo
4. 建立 **Pull Request (PR)** 把作業交到老師的 Repo
5. 在 PR 中接受老師的 **Review**

#### 3. 課程應用範例

##### 1. 地震波形處理

學生可以直接在 Notebook 中執行 ObsPy 程式碼來讀取和繪製地震波形，並進行濾波、震相辨識等練習。

```python
from obspy import read
st = read("./data/earthquake.mseed") # 讀取老師準備好的資料
st.plot()
```

##### 2. 地圖與震央定位

使用 PyGMT 繪製台灣地圖，並將地震震央位置標示出來。

```python
import pygmt
fig = pygmt.Figure()
fig.coast(region=[119, 123, 21.5, 25.5], projection="M12c", shorelines=True, frame=True)
fig.plot(x=[121.6], y=[24.0], style="c0.3c", color="red")
fig.show()
```

#### 4. 延伸應用

- **自動化作業分發：** 老師可以使用 GitHub Classroom，讓每位學生點擊連結後，都能自動建立一個含有 Codespaces 配置的個人作業 Repo。
- **期末專案協作：** 小組成員可以共用同一個 Codespace 環境，進行數據分析、模型建立與繪圖。
- **互動式報告展示：** 學生可以在 Codespace 中使用 Streamlit 或 Gradio 建立一個互動式網頁應用，並在課堂上直接啟動服務進行展示。

👉 **總結：** Codespaces 對地球物理課程的最大價值是「降低環境安裝門檻，確保每位學生都能專注在數據分析與科學探索」，而不是卡在軟體安裝與環境配置的技術問題上。

---

內容分析自: Whole Earth Geophysics, Robert J. Lillie (1999) 及網路公開資料

由 Gemini 為您生成 | 最後更新時間: 2025年9月3日

---

# 圖片資源清單

## 目前 `index.html` 實際使用的 3 張圖片

1. `1000029378.jpg` — 正演模擬範例  
   https://huggingface.co/spaces/oceanicdayi/Geophysics_day1/resolve/main/1000029378.jpg

2. `1000029377.jpg` — 反演範例  
   https://huggingface.co/spaces/oceanicdayi/Geophysics_day1/resolve/main/1000029377.jpg

3. `1000029379.jpg` — 重力模型綜合範例  
   https://huggingface.co/spaces/oceanicdayi/Geophysics_day1/resolve/main/1000029379.jpg

## Repo 內全部 8 張 JPG

- https://huggingface.co/spaces/oceanicdayi/Geophysics_day1/resolve/main/1000029372.jpg
- https://huggingface.co/spaces/oceanicdayi/Geophysics_day1/resolve/main/1000029373.jpg
- https://huggingface.co/spaces/oceanicdayi/Geophysics_day1/resolve/main/1000029374.jpg
- https://huggingface.co/spaces/oceanicdayi/Geophysics_day1/resolve/main/1000029375.jpg
- https://huggingface.co/spaces/oceanicdayi/Geophysics_day1/resolve/main/1000029376.jpg
- https://huggingface.co/spaces/oceanicdayi/Geophysics_day1/resolve/main/1000029377.jpg
- https://huggingface.co/spaces/oceanicdayi/Geophysics_day1/resolve/main/1000029378.jpg
- https://huggingface.co/spaces/oceanicdayi/Geophysics_day1/resolve/main/1000029379.jpg

> 註：Repo 中 `1000029372.jpg`～`1000029376.jpg` 目前存在於檔案庫，但在現行 `index.html` 中未被引用。
