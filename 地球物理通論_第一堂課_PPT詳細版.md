---
marp: true
theme: default
paginate: true
size: 16:9
footer: 地球物理通論｜第一堂課｜陳達毅
---

# 地球物理通論：第一堂課
## 用任務模式學地球物理、AI Agent、PyGMT、3D建模與科學探究

臺北市立大學 地球環境暨生物資源學系  
第115學年第1學期  
教師：陳達毅

---

# 今日課程定位

今天不是只有「課程介紹」。

今天要讓大家理解：

1. 這門課要學什麼地球物理知識。
2. 這門課為什麼要使用 AI、Google Colab、GitHub 與 3D 列印。
3. 這門課如何用「任務模式」完成學習。
4. 今天就開始建立自己的學習工具與探究紀錄。

---

# 今日三小時總目標

到今天下課前，每位同學應該完成：

1. 知道這門課18週的學習路線。
2. 完成2–3人分組，選出組長。
3. 申請或確認 GitHub 帳號。
4. 能開啟 Google Colab 並執行第一段程式。
5. 初步認識 Gemini、Codex、Antigravity、OpenCode 的角色。
6. 了解什麼是 CER、DEAR、CLIL。
7. 完成一次「用 Gemini 進行地球物理探究」的練習。
8. 知道 AI 對話紀錄為什麼要保存，並知道如何繳交。

---

# 今日時間安排

| 時間 | 任務 | 重點 |
|---|---|---|
| 09:00–09:50 | 課程任務1–3 | 老師介紹、課程內容、上課方式 |
| 09:50–10:00 | 休息 |  |
| 10:00–10:50 | 課程任務4–7 | 分組、GitHub、Colab、AI Agent |
| 10:50–11:00 | 休息 |  |
| 11:00–12:00 | 課程任務8 | 地球物理介紹與 Gemini 探究示範 |

---

# 今日任務地圖

1. 老師自我介紹
2. 課程內容介紹
3. 上課方式介紹
4. 學生分組
5. 安裝／認識 AI Agent
6. 申請 GitHub 帳號
7. 使用 Google Colab
8. 地球物理介紹與 Gemini 探究學習示範

每一個任務都會同時連結：

**Content 科學內容 × Communication 語言表達 × Cognition 思考能力 × Culture 學術／科技文化**

---

# 這門課的核心問題

> 如果我們不知道板塊構造理論，
> 只拿到地形、地震、火山、重力、磁力與熱流資料，
> 我們能不能自己推論出地球內部與表面正在發生什麼事？

這門課不是只背知識。

我們要練習像地球物理學家一樣：

**觀察資料 → 提出模型 → 檢驗模型 → 修正模型 → 說明證據**

---

# 這門課的學習成果會長什麼樣？

期末每組會完成一個公開網頁，部署在 GitHub Pages。

網站要包含：

1. 一個地球物理主題問題。
2. 中英文基本概念說明。
3. PyGMT 或其他程式產生的圖。
4. AI 協助學習與除錯的歷程。
5. CER 論證。
6. DEAR 模型修正歷程。
7. 若主題適合，加入3D建模或列印成果。
8. 最後用中英文進行口頭報告。

---

# 任務1：老師自我介紹
## 我為什麼這樣設計這門課？

我的專業背景包含：

- 地震測報與地震預警
- 地球物理資料分析
- 地震防災應用
- AI 與地球科學學習
- 大學地球物理與地球科學教學
- 生成式 AI 輔助學生製作數位學習成果

我希望這門課不只是讓大家「聽懂地球物理」，而是能實際做出作品。

---

# 我對大家的期許

這門課希望大家成為三種人：

1. **能理解地球的人**  
   能看懂地形、地震、重力、磁力、地熱等資料背後的意義。

2. **能使用工具的人**  
   能使用 AI、Python、Colab、GitHub、PyGMT、3D建模工具解決問題。

3. **能說明自己思考的人**  
   能清楚說明：我問了什麼問題、用了什麼證據、如何形成解釋。

---

# CLIL融入：老師自我介紹

## Content
認識地球物理學家的工作與地球物理課程方向。

## Communication
可以用簡單英文介紹一個人的專業：

- My research focuses on earthquake early warning.
- I use geophysical data to understand the Earth.
- I am interested in using AI to support science learning.

## Cognition
思考：老師的專業如何連結這門課的任務？

## Culture
認識科學家不只是做研究，也需要教學、溝通、跨域合作。

---

# 任務2：課程內容介紹
## 18週學習路線

這門課有三條主線：

1. **地球物理學科知識**
   - 震測
   - 重力
   - 地熱
   - 地電
   - 地磁
   - 板塊構造

2. **英文與CLIL學習**
   - 專有名詞
   - 基本句型
   - 科學說明
   - 中英文報告

3. **資訊與AI能力**
   - GitHub
   - Google Colab
   - PyGMT
   - AI Agent
   - GitHub Pages
   - 3D建模與列印

---

# 18週課程總覽（一）

| 週次 | 主題 | 任務 |
|---|---|---|
| Week 1 | 課程說明與系統安裝 | 建立工具與任務模式 |
| Week 2 | PyGMT 繪製全球地圖 | 畫出地球表面資料 |
| Week 3 | 板塊構造與3D列印 | 從地形建立模型 |
| Week 4 | 板塊構造與3D列印 | 修正模型與展示 |
| Week 5 | 校園野外實驗：折射探勘 | 實地量測 |
| Week 6 | 折射探勘原理 | 建立走時模型 |
| Week 7 | 折射探勘與期中準備 | 整合理論與資料 |
| Week 8 | 期中考 | 概念與方法檢核 |

---

# 18週課程總覽（二）

| 週次 | 主題 | 任務 |
|---|---|---|
| Week 9 | 重力與 Geoid 3D列印 | 看見看不見的重力場 |
| Week 10 | 重力 | 解釋地下密度差異 |
| Week 11 | 專題演講 | 連結真實研究與職涯 |
| Week 12 | 板塊構造與地熱 | 能源與地球內部熱 |
| Week 13 | 地電與地磁 | 了解地下電性與磁性 |
| Week 14 | 地電與地磁 | 資料解釋與應用 |
| Week 15 | 期末專題發表 | 第一輪發表 |
| Week 16 | 期末專題發表 | 第二輪發表 |
| Week 17–18 | 實習、參訪 | 延伸學習 |

---

# 課程評量方式

| 評量項目 | 比例 | 說明 |
|---|---:|---|
| 期中考 | 40% | 地球物理基本概念、原理、方法 |
| 作業 | 50% | Colab、PyGMT、AI紀錄、網頁、報告 |
| 平時成績 | 10% | 出席、參與、討論、提問 |

重要提醒：

**作業不是只看最後結果，而是看你的學習過程。**

---

# 這門課的三大能力

## 1. 地球物理學科知識
知道地球物理方法如何用來理解地球。

## 2. 英文能力
能用簡單英文說明科學內容。

## 3. 資訊能力
能使用 AI、程式與雲端平台完成資料整理、圖像、網頁與報告。

---

# CLIL融入：課程內容介紹

## Content
了解地球物理通論的主題與評量方式。

## Communication
今日英文關鍵句：

- This course focuses on geophysical methods.
- We will use data to build scientific models.
- We will publish our final project on GitHub Pages.

## Cognition
判斷：這門課需要哪些能力？我目前缺哪一項？

## Culture
認識現代科學工作不只靠紙筆，也靠開放資料、程式、協作平台與公開成果。

---

# 任務3：上課方式介紹
## 老師示範 → 學生操作 → 學生報告

這門課會採用三階段模式：

1. **老師示範**
   - 示範如何提問
   - 示範如何使用 AI
   - 示範如何畫圖
   - 示範如何建立網頁
   - 示範如何檢查 AI 是否合理

2. **學生操作**
   - 分組完成任務
   - 保留過程紀錄
   - 遇到問題時先嘗試解決

3. **學生報告**
   - 用資料說明問題
   - 用模型解釋現象
   - 接受老師與同學提問

---

# 為什麼要錄影與示範？

因為這門課的任務包含很多工具：

- GitHub
- Google Colab
- PyGMT
- AI Agent
- Gemini
- 網頁部署
- 3D建模

一次聽完不一定記得。

所以老師會先示範完整流程，並錄影提供大家回看。

你要學的不是「背步驟」，而是理解一個工作流程。

---

# 這門課的任務模式

每個任務都會包含：

1. **輸入**：資料、問題、課本內容或老師示範。
2. **處理**：閱讀、提問、畫圖、寫程式、問 AI、討論。
3. **輸出**：圖、模型、文字、AI紀錄、網頁或口頭報告。
4. **反思**：我學到了什麼？AI 幫了什麼？我如何驗證？

---

# CLIL融入：上課方式

## Content
認識課堂流程與學習任務。

## Communication
任務句型：

- Our task is to ...
- We need to collect evidence from ...
- We used AI to ..., but we checked it by ...

## Cognition
比較：只聽講與任務學習有什麼差異？

## Culture
學術文化重視 evidence、documentation、reproducibility。

---

# 任務4：學生分組

請完成：

1. 2–3人一組。
2. 推選一位組長。
3. 組長負責確認每週任務進度。
4. 每位組員都必須有自己的 AI 對話紀錄。
5. 每組最後要有共同網頁成果。

---

# 分組角色建議

每組可以暫時分成三種角色。

## 1. Data / Code
負責 Colab、PyGMT、資料整理。

## 2. Explanation / CLIL
負責中英文說明、專有名詞、句型整理。

## 3. Design / Web / 3D
負責網頁、圖片、3D模型、簡報設計。

角色可以輪流，不是固定分工。

---

# 今日分組輸出

每組下課前請填寫或記錄：

1. 組別名稱
2. 組員姓名
3. 組長
4. 每位組員 GitHub 帳號
5. 每位組員是否能開啟 Google Colab
6. 今天使用 Gemini 的對話紀錄連結或截圖

---

# CLIL融入：分組

## Content
建立協作學習小組。

## Communication
小組英文句型：

- I can be responsible for coding.
- I can help with the explanation.
- Our group leader is ...
- We will work together to build a webpage.

## Cognition
思考：每個人擅長什麼？小組如何互補？

## Culture
科學研究常以團隊合作完成，需要分工、紀錄與互相檢查。

---

# 任務5：安裝／認識 AI Agent

今天先建立觀念，不要求每個人馬上熟練。

我們會接觸：

1. **Gemini**：學習、提問、整理知識。
2. **Codex**：協助閱讀、修改與產生程式碼。
3. **Antigravity IDE**：以專案為中心管理 AI agent 工作。
4. **OpenCode**：在終端機、IDE或桌面中使用 AI coding agent。

今天的重點是：

**AI 可以協助，但不能取代你的判斷。**

---

# AI Agent 在這門課中的角色

| 工具 | 主要用途 | 你要負責什麼 |
|---|---|---|
| Gemini | 理解課本、提出假說、整理概念 | 判斷回答是否合理 |
| Codex | 幫助寫程式、看錯誤、整理專案 | 檢查程式是否真的能跑 |
| Antigravity | 管理專案、建立工作流程、產出 artifacts | 檢查任務與成果是否符合需求 |
| OpenCode | 終端機或IDE中的程式協作 | 看懂修改內容與差異 |

---

# AI使用原則

AI 可以做：

- 協助解釋概念
- 提出可能假說
- 協助寫程式
- 協助除錯
- 協助整理網頁文字
- 協助翻譯或改寫英文句子

AI 不可以替你做完：

- 判斷答案是否正確
- 決定證據是否足夠
- 解釋為什麼接受某個模型
- 取代你的學習紀錄
- 隱藏錯誤與不理解

---

# AI對話紀錄為什麼要繳交？

因為真正的學習不只看最後答案。

老師要看的是：

1. 你怎麼問問題？
2. AI 給了什麼？
3. 你有沒有懷疑？
4. 你如何查證？
5. 你如何修改下一個問題？
6. 你的模型如何改變？

AI 對話紀錄就是你的探究歷程證據。

---

# AI Interaction Log 格式

| 階段 | 我的Prompt | AI回應摘要 | 我的判斷 | 驗證方式 | 下一步 |
|---|---|---|---|---|---|
| 問題形成 | 我想知道... | AI建議... | 我覺得... | 查課本／畫圖／查資料 | 下一個問題... |
| 假說建立 | 請提出... | AI提出... | 哪些合理？ | 用資料檢查 | 修改假說 |
| 程式協助 | 程式錯誤... | AI建議... | 是否可行？ | 實際執行 | 修正程式 |
| 模型修正 | 根據證據... | AI協助整理 | 我是否接受？ | 回到資料 | 完成說明 |

---

# CLIL融入：AI Agent

## Content
認識 AI agent 在地球物理學習中的用途。

## Communication
英文句型：

- The AI suggested that ...
- I agree with this because ...
- I do not fully agree because ...
- We verified the answer by ...

## Cognition
評估：AI 回答是答案、假說、還是線索？

## Culture
現代科學與工程越來越重視 human-AI collaboration，但也重視責任與驗證。

---

# 任務6：申請 GitHub 帳號

GitHub 是這門課的核心平台。

你會用 GitHub 來：

1. 保存程式碼。
2. 保存資料與圖片。
3. 保存 AI 使用紀錄。
4. 製作 README。
5. 發布 GitHub Pages 網站。
6. 建立可追蹤的學習歷程。

---

# GitHub 今天要完成的事

每位同學完成：

1. 註冊或登入 GitHub。
2. 確認自己的 GitHub username。
3. 建立一個練習 repository。
4. repository 名稱建議：

```text
geophysics-learning-2026
```

5. 建立或確認 README.md。
6. 將組員 GitHub username 交給組長。

---

# README.md 第一版內容

今天可以先寫：

```markdown
# Geophysics Learning Portfolio

## Course
地球物理通論

## Student
姓名：
組別：

## Learning Goals
1. Learn basic geophysical concepts.
2. Use Google Colab and PyGMT to visualize Earth data.
3. Use AI tools to support inquiry and explanation.
4. Build a final webpage on GitHub Pages.
```

---

# GitHub Pages 的概念

GitHub Pages 可以把 repository 中的網頁檔案發布成網站。

這代表你的期末報告不是只有 Word 或 PPT。

你的成果會變成：

- 可以公開瀏覽的作品
- 可以放圖片、地圖、程式結果
- 可以持續修改
- 可以放入履歷或學習歷程

---

# CLIL融入：GitHub

## Content
認識版本控制、公開作品與學習歷程。

## Communication
英文句型：

- This repository stores our project files.
- Our final project will be published on GitHub Pages.
- The README explains the purpose of our project.

## Cognition
思考：公開的數位作品和一次性的作業有什麼不同？

## Culture
開源文化強調 sharing、documentation、collaboration。

---

# 任務7：使用 Google Colab

Google Colab 是這門課的科學筆記本。

它可以：

1. 寫 Python。
2. 執行程式。
3. 畫圖。
4. 記錄文字說明。
5. 儲存學習歷程。
6. 連結到 Google Drive 或 GitHub。

---

# Colab 今天要完成的事

每位同學完成：

1. 開啟 Google Colab。
2. 新增一個 notebook。
3. 更改檔名：

```text
Week01_Geophysics_First_Inquiry.ipynb
```

4. 新增一個文字區塊。
5. 新增一個程式區塊。
6. 執行第一段 Python 程式。

---

# Colab 第一段程式

```python
print("Hello, Geophysics!")
print("I will use data, models, and AI to understand the Earth.")
```

執行後請確認：

1. 有沒有成功輸出文字？
2. 錯誤訊息是什麼？
3. 如果有錯，你如何求助？
4. 你是否能把錯誤訊息貼給 AI 並請它解釋？

---

# Colab 筆記本的基本結構

建議每次作業都包含：

```markdown
# Question
我想研究什麼？

# Hypothesis
我一開始的猜想是什麼？

# Data
我使用什麼資料？

# Code
我如何處理資料？

# Result
我得到什麼圖或結果？

# Interpretation
我如何解釋？

# AI Record
AI 如何協助？我如何判斷？
```

---

# Colab 不是只是寫程式

Colab 在這門課中是：

> Digital Laboratory Notebook  
> 數位實驗筆記本

它要記錄：

- 你的問題
- 你的猜想
- 你的程式
- 你的錯誤
- 你的圖
- 你的解釋
- 你的 AI 對話
- 你的模型修正

---

# CLIL融入：Google Colab

## Content
學會使用科學運算筆記本。

## Communication
英文句型：

- I wrote a Python code to ...
- The output shows that ...
- I got an error message.
- I fixed the problem by ...

## Cognition
分析：程式輸出是否符合預期？錯誤訊息代表什麼？

## Culture
科學研究需要 reproducible workflow：別人能重複你的步驟。

---

# 任務8：地球物理介紹
## 什麼是地球物理？

地球物理學是使用物理方法研究地球的學科。

它關心的問題包含：

- 地球內部長什麼樣？
- 地震波如何傳遞？
- 地球重力場如何反映地下密度？
- 地球磁場如何變化？
- 地下是否有熱能、流體或礦產？
- 板塊為什麼會移動？

---

# 地球物理方法總覽

| 方法 | 觀測什麼 | 可以推論什麼 |
|---|---|---|
| 震測 | 地震波速度與走時 | 地下構造、斷層、地殼厚度 |
| 重力 | 重力異常 | 地下密度差異、盆地、山根 |
| 地磁 | 磁場變化 | 岩石磁性、海底擴張、構造 |
| 地電 | 電阻率 | 地下水、熱液、斷層帶 |
| 地熱 | 熱流與溫度 | 地熱資源、地球內部熱 |
| GPS | 地表位移 | 板塊運動、斷層滑移 |

---

# 地球物理的特徵

地球物理常常無法直接看到地下。

所以我們必須：

1. 從地表觀測資料出發。
2. 建立地下模型。
3. 用模型產生可檢驗的預測。
4. 比較預測與觀測是否一致。
5. 修正模型。

這就是科學建模。

---

# 例子：醫生看X光，地球物理學家看地球

醫生不能直接打開人體。

所以使用：

- X光
- 超音波
- MRI

地球物理學家不能直接打開地球。

所以使用：

- 地震波
- 重力
- 磁力
- 電性
- 熱流

兩者都在做：

**用間接資料推論看不見的內部構造。**

---

# 今日核心探究問題

> 為什麼地震、火山、山脈與海溝常常不是隨機分布，
> 而是集中在某些帶狀區域？

我們暫時不要直接背板塊構造。

我們先想：

1. 這些現象有沒有共同位置？
2. 它們可能代表地下有什麼構造？
3. 需要哪些證據才能支持解釋？

---

# CER：科學論證框架

CER 是：

## Claim 主張
你對問題的回答是什麼？

## Evidence 證據
你用了哪些資料支持你的主張？

## Reasoning 推理
為什麼這些證據可以支持主張？

---

# CER 範例

## Question
為什麼日本附近常發生地震？

## Claim
日本附近可能位在板塊邊界，且有板塊隱沒作用。

## Evidence
日本東側有深海溝，地震沿海溝呈帶狀分布，且震源深度往內陸方向逐漸增加。

## Reasoning
如果一個板塊向另一個板塊下方隱沒，地震會沿著傾斜的板塊界面發生，因此會形成由淺到深的地震帶。

---

# DEAR：科學建模流程

這門課會使用 DEAR 模型歷程：

## D — Design a model
設計一個初始模型。

## E — Elaborate the model
加入更多細節與證據。

## A — Apply the model
用模型解釋或預測新的現象。

## R — Revise the model
根據證據修正模型。

---

# DEAR 範例：板塊構造

## Design
一開始假設地震是隨機發生。

## Elaborate
加入全球地震分布圖後，發現地震集中成帶狀。

## Apply
用「板塊邊界」模型預測火山與海溝也可能在附近。

## Revise
發現有些火山不在邊界上，例如熱點火山，因此模型需要加入 hotspot。

---

# CLIL：用英文幫助科學學習

CLIL = Content and Language Integrated Learning

這門課不是上英文課。

而是：

> 用英文句型幫助我們整理科學思考。

例如：

- The evidence suggests that ...
- This pattern may indicate ...
- Our model explains ... because ...
- However, this model cannot explain ...

---

# 今日英文關鍵詞

| English | 中文 |
|---|---|
| geophysics | 地球物理 |
| plate tectonics | 板塊構造 |
| earthquake | 地震 |
| volcano | 火山 |
| trench | 海溝 |
| mountain belt | 山脈帶 |
| evidence | 證據 |
| model | 模型 |
| hypothesis | 假說 |
| reasoning | 推理 |

---

# 今日英文句型

## 描述觀察
- I observe that ...
- The map shows that ...
- Earthquakes are concentrated along ...

## 提出假說
- My hypothesis is that ...
- This pattern may be caused by ...

## 使用證據
- The evidence supports this claim because ...
- We used the map as evidence.

## 修正模型
- We revised our model because ...
- Our first model could not explain ...

---

# Gemini 探究示範：不要直接要答案

不建議這樣問：

> 什麼是板塊構造？

比較好的問法：

> 我正在研究地震、火山、山脈與海溝的分布。
> 請不要直接給我標準答案。
> 請幫我提出三個可能假說，並告訴我需要哪些證據來檢驗。

---

# Gemini Prompt 1：形成問題

請同學打開 Gemini，輸入：

```text
我正在修一門地球物理通論課。
今天的問題是：為什麼地震、火山、山脈與海溝常常集中在某些帶狀區域？

請不要直接給我標準答案。
請先用高中到大學一年級程度，幫我提出三個可能假說。
每個假說都要說明：
1. 這個假說如何解釋現象？
2. 需要哪些證據來檢驗？
3. 這個假說可能有什麼限制？
```

---

# Gemini Prompt 1 後要做什麼？

不要直接接受 AI 的答案。

請在 Colab 或筆記中記錄：

1. AI 提出哪三個假說？
2. 哪一個你覺得最合理？
3. 哪一個你覺得最可疑？
4. AI 有沒有直接跳到板塊構造？
5. 你還需要什麼資料？

---

# Gemini Prompt 2：轉成 CER

輸入：

```text
請把剛才最可能的假說整理成 CER 格式。

Claim：一句話主張。
Evidence：列出至少三種需要的證據。
Reasoning：說明為什麼這些證據能支持主張。

請使用中文，並在每一段後面附上一句簡單英文句型。
```

---

# Gemini Prompt 3：成為反方評論者

輸入：

```text
現在請你扮演一位嚴格的地球物理老師。
請批判我剛才的 CER。

請指出：
1. Claim 是否太快下結論？
2. Evidence 是否足夠？
3. Reasoning 是否有跳躍？
4. 還需要哪些資料？
5. 哪些地方可能是 AI 幻覺或過度簡化？
```

---

# Gemini Prompt 4：連結 DEAR

輸入：

```text
請把我的探究歷程整理成 DEAR 模型：

D: Design a model，我一開始的模型是什麼？
E: Elaborate the model，加入哪些資料後模型變得更完整？
A: Apply the model，這個模型可以解釋哪些新現象？
R: Revise the model，這個模型有哪些限制，需要如何修正？

請用表格呈現，並加入簡單英文句型。
```

---

# Gemini Prompt 5：建立作業架構

輸入：

```text
請幫我根據今天的探究，建立一份學習紀錄架構。
我的主題是：地震、火山、山脈與海溝的分布。

請包含：
1. Research Question
2. Initial Hypothesis
3. CER
4. DEAR Model
5. English Keywords
6. Useful English Sentence Patterns
7. What I need to verify next
8. AI Interaction Reflection
```

---

# 小組討論問題

完成 Gemini 練習後，小組討論：

1. 你們的 AI 回答一樣嗎？
2. 哪些內容看起來可靠？
3. 哪些內容需要查證？
4. AI 有沒有給出沒有證據的判斷？
5. 如果要用 PyGMT 畫圖驗證，你們想畫什麼？

---

# 教師示範：從問題到資料

研究問題：

> 地震和火山是否真的沿著某些帶狀區域分布？

可能資料：

1. 全球地形資料
2. 全球地震震央
3. 地震深度
4. 全球火山分布
5. 板塊邊界資料
6. 海底年齡或地磁條帶

---

# PyGMT 在這裡的角色

PyGMT 可以幫助我們：

1. 繪製地形圖。
2. 顯示海溝、中洋脊、山脈。
3. 疊加地震與火山資料。
4. 比較資料分布與模型是否一致。
5. 產生可以放進網頁與報告的圖。

下週開始，我們會正式用 PyGMT 畫全球與區域地圖。

---

# 3D建模與列印在這裡的角色

3D列印不是裝飾。

它是另一種模型。

例如：

- 日本海溝地形模型
- 台灣地形模型
- 喜馬拉雅山地形模型
- 中洋脊地形模型
- Geoid 重力場模型

我們會比較：

**地圖模型、概念模型、3D實體模型**各自能解釋什麼、不能解釋什麼。

---

# 科學模型的三種形式

| 模型形式 | 例子 | 優點 | 限制 |
|---|---|---|---|
| Data Model | PyGMT 地圖 | 接近真實資料 | 需要判讀 |
| Conceptual Model | 板塊隱沒示意圖 | 容易解釋機制 | 可能過度簡化 |
| Physical Model | 3D列印地形 | 直觀、可觸摸 | 垂直比例可能誇大 |

---

# 期末專題網站建議架構

```text
project-website/
├── index.html
├── README.md
├── figures/
│   └── pygmt_map.png
├── models/
│   └── terrain_model.stl
├── ai_logs/
│   └── week01_gemini_log.md
├── notebooks/
│   └── pygmt_mapping.ipynb
└── references/
```

---

# 期末網站內容至少包含

1. Research Question
2. Background
3. English Keywords
4. Initial Model
5. Data and Method
6. PyGMT Map
7. CER Explanation
8. DEAR Model Revision
9. AI Interaction Log
10. 3D Model or Visualization
11. Final Explanation
12. Limitations
13. References

---

# 今日作業說明

## 作業一：工具確認

請完成：

1. GitHub 帳號
2. Google Colab notebook
3. Gemini 對話紀錄
4. 小組名單

## 作業二：AI 探究紀錄

主題：

> 為什麼地震、火山、山脈與海溝常常集中在某些帶狀區域？

繳交：

- Gemini 對話紀錄
- CER整理
- DEAR整理
- 100–200字反思

---

# 作業二格式建議

```markdown
# Week 01 AI Inquiry Log

## Research Question

## Gemini Conversation Summary

## CER
### Claim
### Evidence
### Reasoning

## DEAR
### Design a model
### Elaborate the model
### Apply the model
### Revise the model

## English Keywords

## Reflection
AI helped me by ...
I verified the answer by ...
I still need to learn ...
```

---

# 作業評分重點

| 面向 | 重點 |
|---|---|
| 完整性 | 是否包含 Prompt、AI回應、自己的判斷 |
| 科學性 | 是否有主張、證據、推理 |
| 反思性 | 是否指出 AI 的幫助與限制 |
| 語言學習 | 是否整理英文關鍵字與句型 |
| 可追蹤性 | 是否能看出探究歷程 |

---

# 好的 AI 使用範例

不是只貼：

> AI 說板塊構造造成地震。

而是：

> 我問 AI 為什麼地震沿海溝分布。AI 說可能與隱沒作用有關。但我還不能直接相信，所以我接著問：如果是隱沒作用，地震深度應該如何變化？AI 回答應該形成傾斜震源帶。下一步我想用 PyGMT 畫地震深度分布來檢查。

---

# 不好的 AI 使用範例

需要避免：

1. 直接問 AI 答案，沒有追問。
2. 沒有保存 Prompt。
3. 沒有說明自己是否同意。
4. 沒有任何證據。
5. 直接複製 AI 文字當作自己的報告。
6. AI 說什麼就寫什麼。

---

# 課堂規範

請注意：

1. 尊重智慧財產權。
2. 使用正版教材與合法資料來源。
3. 不任意複製、散布未授權內容。
4. 使用 AI 時要標示協助範圍。
5. 小組合作需要公平分工。
6. 課堂討論尊重不同背景與觀點。
7. 不製作違反性別平等或歧視性內容。

---

# 今天最後10分鐘：Exit Ticket

請每位同學用 3 句話回答：

1. 今天我知道地球物理是在研究：＿＿＿＿。
2. 今天我學到 AI 可以幫我：＿＿＿＿，但我必須：＿＿＿＿。
3. 我下週最想學會的工具或概念是：＿＿＿＿。

英文挑戰句：

> I will use evidence to build and revise my model.

---

# 教師收尾

這門課的目標不是讓大家一開始就會所有工具。

而是讓大家逐步建立：

1. 地球物理觀念
2. 資料處理能力
3. AI 協作能力
4. 英文科學表達能力
5. 科學探究與建模能力

真正重要的是：

> 你能不能說清楚：我如何從資料與證據形成解釋？

---

# 下週預告

## PyGMT 繪製全球地圖

下週我們會開始：

1. 使用 Google Colab 安裝 PyGMT。
2. 繪製全球地形圖。
3. 觀察海溝、中洋脊、山脈。
4. 思考地形與板塊構造的關係。
5. 產生第一張可以放到 GitHub Pages 的圖。

請下週帶：

- 可上網筆電
- Google 帳號
- GitHub 帳號
- 今天的 AI 探究紀錄

---

# 附錄A：第一堂課教師口語引導稿

今天這門課，我們不會把地球物理只當成一堆名詞來背。地球物理真正有趣的地方，是我們常常看不到地下，但我們可以從地表觀測到的訊號，例如地震波、重力、磁力、電性與熱流，去推論地球裡面可能長什麼樣子。

這也是為什麼這門課會使用 AI、Python、PyGMT、GitHub 與3D列印。這些工具不是為了炫技，而是為了讓大家可以把抽象的地球物理概念變成看得見、可以討論、可以檢驗的成果。

---

# 附錄B：教師示範用開場問題

請大家先不要急著回答「板塊構造」。

如果你是第一個觀察地球的人，你只看到：

- 有些地方有很深的海溝
- 有些地方有很高的山脈
- 地震常常沿著一條線分布
- 火山也常常集中在某些區域

你會怎麼解釋？

這就是科學探究的開始。

---

# 附錄C：教師示範用 AI 對話評論

當 AI 回答「這是因為板塊構造」時，我們不能馬上停止。

我們要繼續問：

1. 你根據什麼證據這樣說？
2. 還有沒有其他可能？
3. 如果這個解釋是對的，地圖上應該看到什麼？
4. 如果這個解釋是錯的，會出現什麼反例？
5. 我可以用什麼資料檢查？

這樣 AI 才會從答案機變成探究夥伴。

---

# 附錄D：教師板書架構

```text
現象：地震、火山、山脈、海溝呈帶狀分布

問題：為什麼？

假說1：地球表面有大型裂縫或邊界
假說2：地下有熱或物質上升
假說3：地球表面板塊正在移動

需要證據：
- 地形
- 地震位置
- 地震深度
- 火山位置
- 板塊運動方向

CER：
Claim → Evidence → Reasoning

DEAR：
Design → Elaborate → Apply → Revise
```

---

# 附錄E：給學生的英文句型小抄

## Claim
- I claim that ...
- Our claim is that ...

## Evidence
- The evidence shows that ...
- The map indicates that ...
- The data suggest that ...

## Reasoning
- This supports our claim because ...
- This pattern can be explained by ...

## Revision
- We revised our model because ...
- Our previous model could not explain ...

---

# 附錄F：第一堂課後可立即使用的作業公告

## 地球物理通論 Week 01 作業

請完成以下內容，並於下次上課前繳交。

1. GitHub 帳號與練習 repository 連結。
2. Google Colab notebook 連結或截圖。
3. Gemini 探究對話紀錄。
4. CER 整理。
5. DEAR 模型整理。
6. 100–200字學習反思。

反思問題：

- AI 幫助我理解了什麼？
- 我有沒有懷疑 AI 的回答？
- 我下一步想用什麼資料驗證？

---

# 附錄G：教師提醒

第一堂課不要追求所有人立刻熟練工具。

今天真正要建立的是：

1. 任務模式
2. AI紀錄意識
3. GitHub/Colab最低操作能力
4. 科學探究框架
5. CLIL句型使用習慣

只要學生今天能理解：

> AI 的回答需要被判斷，科學主張需要證據支持。

這堂課就成功了。

---

# 附錄H：可放在投影片最後的提醒

## 下週之前請完成

- GitHub 帳號
- Google Colab notebook
- Gemini 對話紀錄
- CER 與 DEAR 作業
- 小組名單

## 下週開始

我們會用 PyGMT 畫出地球。

然後問：

> 地球表面的形狀，是否已經透露了板塊運動的證據？
