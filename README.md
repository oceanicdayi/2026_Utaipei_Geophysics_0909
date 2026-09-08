# 地球物理通論｜第一堂課教材

**臺北市立大學　地球環境暨生物資源學系**  
第 115 學年第 1 學期　｜　教師：陳達毅（Dayi Chen）  
課程名稱：**地球物理通論（General Geophysics）**  
第一堂課時間：09:00–12:00　｜　對象：地生系二年級

> 探索地球　‧　連結科學　‧　面向未來  
> From Earth Systems to a Smarter, More Connected World.

**課堂互動頁（GitHub Pages）：** [https://oceanicdayi.github.io/2026_Utaipei_Geophysics_0909/](https://oceanicdayi.github.io/2026_Utaipei_Geophysics_0909/)

投影機上課、學生筆電同步皆可使用：章節切換、任務勾選、課堂計時、地球物理導論與正演／反演、折射建模逐格揭露、CER 白板、DEAR 循環、CLIL 全班朗讀、Gemini Prompt 一鍵複製、Exit Ticket。

本倉庫整理《地球物理通論》第一堂課的完整教材：互動課堂頁、Marp 簡報原稿、三小時中英文對照講稿、CLIL 句型附錄、PyGMT 示範筆記本、概念圖，以及對應 PDF。這份 README 把上述資料的內容整編成一份可直接閱讀的課程手冊。

---

## 目錄

1. [這門課在學什麼](#這門課在學什麼)
2. [倉庫檔案一覽](#倉庫檔案一覽)
3. [18 週學習路線](#18-週學習路線)
4. [評量方式](#評量方式)
5. [第一堂課三小時任務地圖](#第一堂課三小時任務地圖)
6. [地球物理是什麼](#地球物理是什麼)
7. [科學探究與 CER](#科學探究與-cer)
8. [DEAR 科學建模循環](#dear-科學建模循環)
9. [CLIL：用英文整理科學思考](#clil用英文整理科學思考)
10. [AI 是協作者，不是答案機器](#ai-是協作者不是答案機器)
11. [從問題到 GitHub Pages 的數位工作流程](#從問題到-github-pages-的數位工作流程)
12. [PyGMT 示範筆記本](#pygmt-示範筆記本)
13. [第一堂課作業](#第一堂課作業)
14. [課堂規範與下週預告](#課堂規範與下週預告)
15. [如何使用本倉庫](#如何使用本倉庫)

---

## 這門課在學什麼

這門課不是只背地球物理名詞，也不是把事情全部交給 AI。核心問題是：

> 如果我們不知道板塊構造理論，只拿到地形、地震、火山、重力、磁力與熱流資料，我們能不能自己推論出地球內部與表面正在發生什麼事？

學生要練習像地球物理學家一樣：

**觀察資料 → 提出模型 → 檢驗模型 → 修正模型 → 說明證據**

同時學會三件互相支援的事：

| 主軸 | 英文 | 內容 |
|---|---|---|
| 學科知識 | Geophysics | 震測、重力、地熱、地電、地磁、板塊構造 |
| 雙語學習 | CLIL / Science through English | 單字、句型、科學論述、中英文報告 |
| 資訊與 AI | AI & Digital Literacy | Gemini、AI Agent、Google Colab、GitHub、PyGMT、3D 建模與列印 |

三條主線最後匯聚成同一種能力：

> 用資料與證據理解地球，並能以模型、程式、英文與網頁清楚表達。

![概念圖 1｜這門課到底在學什麼？](ChatGPT%20Image%202026年9月9日%20上午01_51_32%20%281%29.png)

期末每組完成一個公開網頁（GitHub Pages），並用中英文口頭報告。網站至少包含：研究問題、中英文概念、PyGMT 圖、AI 協助歷程、CER 論證、DEAR 模型修正、必要時加入 3D 建模／列印成果。

老師希望學生同時成為三種人：

1. **能理解地球的人**：看懂地形、地震、重力、磁力、地熱等資料背後的意義。
2. **能使用工具的人**：能用 AI、Python、Colab、GitHub、PyGMT、3D 建模解決問題。
3. **能說明自己思考的人**：清楚說明自己問了什麼、用了什麼證據、如何形成解釋。

最重要的三句課堂口號：

| 面向 | English | 中文 |
|---|---|---|
| Science | **How do we know?** | 我們怎麼知道？ |
| Evidence | **What evidence supports this idea?** | 什麼證據支持這個想法？ |
| AI Literacy | **AI can generate an answer, but understanding the answer is your responsibility.** | AI 可以產生答案，但是理解答案是你的責任。 |

---

## 倉庫檔案一覽

| 檔案 | 類型 | 說明 |
|---|---|---|
| `docs/` | 課堂互動網站 | GitHub Pages 來源。`index.html` 為單頁課堂工具，含 CSS／JS、概念圖、地球物理導論圖與折射建模逐格揭露。 |
| `.github/workflows/pages.yml` | GitHub Actions | 推送到 `main` 後自動部署 GitHub Pages。 |
| `Geophysics_day1_完整文字與圖片.md` | 導論原稿 | 自 Hugging Face Space `oceanicdayi/Geophysics_day1` 擷取的地球物理介紹、正演／反演、約束、應用與資料環境。 |
| `what_is_geophysics.md` | 短定義 | 地質學看景觀、地球物理學是地質與物理的跨領域。 |
| `地球物理通論_第一堂課_PPT詳細版.md` | Marp 簡報（16:9） | 第一堂課完整投影片原稿，含 18 週路線、任務設計、CER／DEAR、Gemini prompts、作業與附錄。可用 [Marp](https://marp.app/) 匯出投影片。 |
| `地球物理通論第一堂課｜3小時中英文對照完整講稿.md` | 講稿 | 09:00–12:00 對照講稿，含板書、CLIL 活動、Colab 示範程式與 Exit Ticket。 |
| `地球物理通論第一堂課｜3小時中英文對照完整講稿.pdf` | PDF | 上述講稿的匯出成品。 |
| `地球物理通論第一堂課｜CLIL句型與三例擴充附錄.md` | 句型庫 | 八層 CLIL 句型（每句三例）、CER／DEAR 句型、AI Prompt、小組討論與課堂管理英文。 |
| `地球物理通論第一堂課｜CLIL句型與三例擴充附錄.pdf` | PDF | 上述附錄的匯出成品。 |
| `pygmt_plot_plate_boundary.ipynb` | Jupyter / Colab | 在 Google Colab 安裝 PyGMT 0.17，繪製全球地形與台灣區域地形圖。 |
| `ChatGPT Image … (1).png` | 概念圖 1 | 這門課到底在學什麼：學科知識 × CLIL × AI／資訊能力。 |
| `ChatGPT Image … (3).png` | 概念圖 2 | 科學探究六步驟與 CER。 |
| `ChatGPT Image … (4).png` | 概念圖 3 | DEAR 科學建模循環。 |
| `ChatGPT Image … (5).png` | 概念圖 4 | AI 是協作者，不是答案機器。 |
| `ChatGPT Image … (6).png` | 概念圖 5 | 從問題到 GitHub Pages 的數位工作流程。 |
| `ChatGPT Image … (2).png` | 概念圖 6 | 板塊構造：如何用多重證據建立模型。 |
| `修正紀錄.md` | 維護紀錄 | 本倉庫每次修正的整理。 |
| `README.md` | 本檔 | 課程內容總覽與教材索引。 |

檔名中的 `ChatGPT Image 2026年9月9日 上午01_51_3x (n).png` 是概念圖原始檔名；編號與概念圖序號不完全相同，請以上表對照。

---

## 18 週學習路線

### 前半（Week 1–8）

| 週次 | 主題 | 任務 |
|---|---|---|
| Week 1 | 課程說明與系統安裝 | 建立工具與任務模式 |
| Week 2 | PyGMT 繪製全球地圖 | 畫出地球表面資料 |
| Week 3 | 板塊構造與 3D 列印 | 從地形建立模型 |
| Week 4 | 板塊構造與 3D 列印 | 修正模型與展示 |
| Week 5 | 校園野外實驗：折射探勘 | 實地量測 |
| Week 6 | 折射探勘原理 | 建立走時模型 |
| Week 7 | 折射探勘與期中準備 | 整合理論與資料 |
| Week 8 | 期中考 | 概念與方法檢核 |

### 後半（Week 9–18）

| 週次 | 主題 | 任務 |
|---|---|---|
| Week 9 | 重力與 Geoid 3D 列印 | 看見看不見的重力場 |
| Week 10 | 重力 | 解釋地下密度差異 |
| Week 11 | 專題演講 | 連結真實研究與職涯 |
| Week 12 | 板塊構造與地熱 | 能源與地球內部熱 |
| Week 13 | 地電與地磁 | 了解地下電性與磁性 |
| Week 14 | 地電與地磁 | 資料解釋與應用 |
| Week 15 | 期末專題發表 | 第一輪發表 |
| Week 16 | 期末專題發表 | 第二輪發表 |
| Week 17–18 | 實習、參訪 | 延伸學習 |

學科方法對應：震測／地震學、重力、地熱、地電、地磁、板塊構造。工具線則貫穿 PyGMT、Google Colab、3D 建模（地形 → 數值地形 → 3D 模型 → STL → 3D 列印）、Gemini／Codex／Antigravity／OpenCode／Hermes Agent，以及 GitHub Pages。

---

## 評量方式

| 項目 | 比例 | 說明 |
|---:|---:|---|
| 期中考 | 40% | 地球物理基本概念、原理、方法 |
| 作業 | 50% | Colab、PyGMT、AI 紀錄、網頁、報告 |
| 平時成績 | 10% | 出席、參與、討論、提問 |

作業看的是 **process（過程）**，不是只有最後答案。老師會看：你怎麼問問題、AI 給了什麼、你有沒有懷疑、如何查證、模型如何改變。

作業評分面向：完整性（Prompt、AI 回應、自己的判斷）、科學性（主張／證據／推理）、反思性（AI 的幫助與限制）、語言學習（英文關鍵字與句型）、可追蹤性（能否看出探究歷程）。

---

## 第一堂課三小時任務地圖

今日不是只有課程介紹。下課前每位同學應完成：

1. 知道 18 週學習路線。
2. 完成 2–3 人分組並選出組長。
3. 申請或確認 GitHub 帳號。
4. 能開啟 Google Colab 並執行第一段程式。
5. 初步認識 Gemini、Codex、Antigravity、OpenCode 的角色。
6. 了解 CER、DEAR、CLIL。
7. 完成一次「用 Gemini 進行地球物理探究」的練習。
8. 知道 AI 對話紀錄為什麼要保存，以及如何繳交。

每一個任務同時連結 CLIL 的 4C：**Content 科學內容 × Communication 語言表達 × Cognition 思考能力 × Culture 學術／科技文化**。

### 時間表

講稿與簡報的任務編號略有差異，實際進行以現場節奏為準。下列依三小時講稿排列，並標出簡報中的對應任務。

| 時間 | 任務 | 重點 |
|---|---|---|
| 09:00–09:10 | Task 1 教師自我介紹 | 科學思考流程：Question → Evidence → Explanation／Model → Test → Revision |
| 09:10–09:30 | Task 2 課程理念與內容 | Geo + Physics；18 週三條主線；AI 是 collaborator |
| 09:30–09:40 | Task 3 上課方式與評量 | 示範 → 練習 → 探究 → 解釋 → 發表；成績架構 |
| 09:40–09:50 | Task 4 分組 | 2–3 人一組；組長／資料程式／紀錄網頁，但每個人都要理解全貌 |
| 09:50–10:00 | 休息 | See you in ten minutes. |
| 10:00–10:25 | Task 5 AI Agent | Chatbot 答題 vs Agent 完成任務；安裝或進入工具環境 |
| 10:25–10:50 | Task 6 GitHub | 學習歷程 portfolio；建立 repo 與 README |
| 10:50–11:00 | 休息 |  |
| 11:00–11:20 | Task 7 Google Colab | 科學筆記本；走時 \(t = d / v\) |
| 11:20–11:40 | Task 8 地球物理是什麼 | 看不到的內部如何研究；observe → analyze → infer |
| 11:40–11:55 | Gemini + CER 探究示範 | 不要直接要答案；保存 AI 對話 |
| 11:55–12:00 | Exit ticket 與下週任務 | 三句課後回饋 |

上課流程固定為：

```text
Teacher demonstrates
        ↓
Students practice
        ↓
Students investigate
        ↓
Students explain
        ↓
Students present
```

每個任務都包含輸入、處理、輸出、反思。重要操作會留下錄影、程式、範例、網頁與 GitHub repository，方便 replay and practice。

### Task 1｜教師自我介紹

教師背景：地震測報與地震預警、地球物理資料分析、地震防災、AI 與地球科學學習、大學教學、生成式 AI 輔助數位學習成果。

這門課不要變成「老師知道答案、學生抄答案」。希望學生做的是：

> Ask a question. Collect evidence. Build an explanation. Test the explanation. Revise the model.

CLIL 開場三句：

- I observe that ______.　我觀察到＿＿＿＿。
- I think ______ because ______.　我認為＿＿＿＿，因為＿＿＿＿。
- The evidence shows that ______.　證據顯示＿＿＿＿。

這三句看起來簡單，但許多科學論證都是這三種句子的延伸。

### Task 2｜這學期要做什麼

Geophysics = Geo（Earth）+ Physics（Physical principles）= **Using physics to understand the Earth.**

如果把台灣地形做成 3D 模型，可能看見：Central Mountain Range、Coastal Range、Western Plain、Longitudinal Valley。

> Taiwan has a high mountain range in the center.  
> The eastern part of Taiwan is very steep.  
> The Longitudinal Valley is located in eastern Taiwan.

AI 可以 provide ideas、explain concepts、write code、find possible errors、suggest hypotheses，但：

```text
AI ≠ replacement for thinking
AI = collaborator
```

**You are responsible for the final decision.**

### Task 4｜分組

2–3 人一組，推選 group leader。角色可輪流，不是固定分工：

| 角色 | 負責 |
|---|---|
| Group leader | 確認每週任務進度 |
| Data / Code | Colab、PyGMT、資料整理 |
| Explanation / CLIL | 中英文說明、專有名詞、句型 |
| Design / Web / 3D | 網頁、圖片、3D 模型、簡報 |

下課前每組記錄：組別名稱、組員、組長、GitHub 帳號、能否開啟 Colab、今日 Gemini 對話連結或截圖。每位組員都必須有自己的 AI 對話紀錄；每組最後要有共同網頁成果。

小組英文：Who wants to be the group leader? / I can work on the code. / I can organize the information. / What do you think? / I agree. / I have a different idea.

### Task 5｜從 Chatbot 到 AI Agent

一般 chatbot：

```text
Question → AI → Answer
```

AI agent 則是：

```text
Goal → Plan → Use tools → Read files → Modify files → Run code → Check results
```

今天第一堂課的目標不是熟練，而是 **成功安裝或成功進入工具環境**。Mission 1：請 agent 回答 `What files are in this folder?`，若能讀到資料夾即完成。

使用 agent 時不要只問 Did it work?，還要問：它改了什麼？為什麼？我要怎麼確認？

### Task 6｜GitHub = Digital Learning Portfolio

GitHub 用來保存 code、figures、data、notes、AI logs、webpages，並可經 GitHub Pages 變成 scientific webpage。建議練習 repository 名稱：`geophysics-2026` 或 `geophysics-learning-2026`。

README 第一版可寫：

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

未來期末成果架構：Research Question → Background → Hypothesis → Data → Analysis → Evidence → Model → AI Interaction → Reflection。

### Task 7｜Google Colab = Scientific Notebook

Colab 在這門課是 **Digital Laboratory Notebook（數位實驗筆記本）**，不是只寫程式。建議檔名：`geophysics_week01.ipynb` 或 `Week01_Geophysics_First_Inquiry.ipynb`。

示範程式：

```python
print("Hello Geophysics")

earth_radius = 6371   # Earth's average radius (km)
print(earth_radius)

distance = 100        # km
velocity = 5          # km/s
time = distance / velocity
print(time)
```

核心句型：**Travel time is equal to distance divided by velocity.**（走時等於距離除以速度。）

\[
t = \frac{d}{v}
\]

這是之後折射震測會反覆出現的概念。

每次 notebook 建議包含：Question、Hypothesis、Data、Code、Result、Interpretation、AI Assistance／AI Record、Verification。老師要看的不只是 code runs successfully，而是 **Do you understand the result?**

### Task 8｜What is Geophysics?

核心問題：**How can we study something we cannot directly see?**

地球物理是 inverse problem。敲桌子聽聲音、醫院用 X-ray／ultrasound／MRI，都是用間接資料推論看不見的內部。地球物理學家測量 seismic waves、gravity、magnetic field、electric properties、heat，再推測地下。

```text
Observe → Analyze → Infer
```

請記住這句：

> We measure seismic waves to infer underground structures.  
> 我們量測地震波，以推論地下構造。

### 11:40–11:55｜Gemini + CER 示範

情境：**Why do earthquakes occur frequently around Taiwan?**

不要輸入「Why are there many earthquakes in Taiwan?」就停在板塊碰撞的現成答案。改成：

1. 不要直接給最後答案，先提出三個可用資料驗證的可能解釋。
2. 什麼證據可以支持每一個解釋？（地震分布、深度、地形、GPS、板塊邊界）
3. 哪些證據可以畫在地圖上？→ 自然連到 PyGMT。

AI 的角色從 answer machine 變成 **hypothesis generator**。從今天開始：**AI conversation is part of your learning record.**

### Exit Ticket

離開前完成三句（講稿版）：

1. Today I learned that geophysics is ______.
2. One digital tool I used today was ______.
3. One question I still have is ______.

簡報另有三句挑戰版：今天我知道地球物理是在研究＿＿＿＿；AI 可以幫我＿＿＿＿，但我必須＿＿＿＿；下週最想學會的是＿＿＿＿。英文挑戰句：*I will use evidence to build and revise my model.*

---

## 地球物理是什麼

地球物理學使用物理方法研究地球，關心：地球內部長什麼樣、地震波如何傳遞、重力場如何反映地下密度、磁場如何變化、地下是否有熱能／流體／礦產、板塊為什麼會移動。

| 方法 | 觀測什麼 | 可以推論什麼 |
|---|---|---|
| 震測 | 地震波速度與走時 | 地下構造、斷層、地殼厚度 |
| 重力 | 重力異常 | 地下密度差異、盆地、山根 |
| 地磁 | 磁場變化 | 岩石磁性、海底擴張、構造 |
| 地電 | 電阻率 | 地下水、熱液、斷層帶 |
| 地熱 | 熱流與溫度 | 地熱資源、地球內部熱 |
| GPS | 地表位移 | 板塊運動、斷層滑移 |

因為常常無法直接看到地下，必須：從地表觀測出發 → 建立地下模型 → 用模型產生可檢驗預測 → 比較預測與觀測 → 修正模型。這就是科學建模。

今日核心探究問題（先不要直接背板塊構造）：

> 為什麼地震、火山、山脈與海溝常常不是隨機分布，而是集中在某些帶狀區域？

可先想：這些現象有沒有共同位置？可能代表地下有什麼構造？需要哪些證據才能支持解釋？

![概念圖 6｜板塊構造：如何用多重證據建立模型？](ChatGPT%20Image%202026年9月9日%20上午01_51_33%20%282%29.png)

板塊構造模型用來解釋地球表面的動態變化。單一證據通常不夠；多種獨立觀測若指向同一模型，解釋力更強：

| 證據線 | 資料 |
|---|---|
| 地形 Topography | 山脈、海溝、洋脊 |
| 地震 Earthquakes | 位置、深度 |
| 火山 Volcanoes | 分布 |
| GPS Plate Motion | 移動方向與速率 |
| 海洋地球物理 Seafloor | 年齡、磁條帶 |

科學模型有三種形式，各有優點與限制：

| 模型形式 | 例子 | 優點 | 限制 |
|---|---|---|---|
| Data Model | PyGMT 地圖 | 接近真實資料 | 需要判讀 |
| Conceptual Model | 板塊隱沒示意圖 | 容易解釋機制 | 可能過度簡化 |
| Physical Model | 3D 列印地形 | 直觀、可觸摸 | 垂直比例可能誇大 |

3D 列印不是裝飾，而是另一種模型，例如日本海溝、台灣地形、喜馬拉雅山、中洋脊、Geoid 重力場。要比較地圖模型、概念模型、3D 實體模型各自能解釋什麼、不能解釋什麼。

---

## 科學探究與 CER

CER = **Claim（主張）+ Evidence（證據）+ Reasoning（推理）**

不是只回答「是什麼」，而是回答「為什麼相信這個答案？」

探究六步驟：

1. **Phenomenon 現象**：觀察自然或生活中的現象。
2. **Question 問題**：提出可探究的問題。
3. **Hypothesis 假設**（對應 Claim）：提出可檢驗的主張。
4. **Evidence 證據**：透過觀察、實驗或資料收集證據。
5. **Reasoning 推理**：用科學原理把證據連回主張。
6. **Conclusion 結論**：形成結論，並思考意涵與後續問題。

![概念圖 2｜科學探究與 CER](ChatGPT%20Image%202026年9月9日%20上午01_51_33%20%283%29.png)

### CER 句型

**Claim**

- Our claim is that ______.　我們的主張是＿＿＿＿。
- We think that ______.　我們認為＿＿＿＿。
- We propose that ______.　我們提出＿＿＿＿。

**Evidence**

- The evidence shows ______.　證據顯示＿＿＿＿。
- We observed ______.　我們觀察到＿＿＿＿。
- According to the data, ______.　根據資料＿＿＿＿。

**Reasoning**

- This evidence supports our claim because ______.　這項證據支持我們的主張，因為＿＿＿＿。
- If ______ is true, we would expect ______.　如果＿＿＿＿是真的，我們應該預期＿＿＿＿。
- The observed pattern is consistent with ______.　觀察到的型態與＿＿＿＿一致。

### 完整示例

**台灣地震**

- Claim: Our claim is that earthquake activity around Taiwan is related to plate interactions.
- Evidence: The earthquake map shows that earthquakes are concentrated in specific regions around Taiwan.
- Reasoning: If earthquakes are related to plate interactions, their locations should follow tectonic structures rather than being randomly distributed.

**日本附近地震（簡報範例）**

- Claim: 日本附近可能位在板塊邊界，且有板塊隱沒作用。
- Evidence: 日本東側有深海溝，地震沿海溝呈帶狀分布，且震源深度往內陸方向逐漸增加。
- Reasoning: 如果一個板塊向另一個板塊下方隱沒，地震會沿著傾斜的板塊界面發生，因此會形成由淺到深的地震帶。

**折射震測**

- Claim: The lower layer has a higher seismic velocity.
- Evidence: The travel-time graph contains two line segments with different slopes.
- Reasoning: Because the slope of a travel-time line is related to seismic velocity, the different slopes indicate different seismic velocities.

**重力**

- Claim: A high-density body exists underground.
- Evidence: A positive gravity anomaly is observed above the study area.
- Reasoning: A high-density body produces greater gravitational attraction, so the positive anomaly supports the claim.

---

## DEAR 科學建模循環

模型不是最後答案。模型 = 可被測試、修正的解釋工具。

| 階段 | 英文 | 中文 | 關鍵問題 |
|---|---|---|---|
| D | Design a model | 建立初始模型 | 我們認為正在發生什麼？ What do we think is happening? |
| E | Elaborate the model | 加入新證據與細節 | 還需要加入什麼？ What else must be included? |
| A | Apply the model | 用模型預測 | 我們應該觀察到什麼？ What should we observe? |
| R | Revise the model | 根據結果修正 | 哪些地方需要改變？ What needs to change? |

循環是連續的：Design → Elaborate → Apply → Revise → 再回到 Design。

![概念圖 3｜DEAR 科學建模循環](ChatGPT%20Image%202026年9月9日%20上午01_51_33%20%284%29.png)

### DEAR 句型

- Our initial model is ______.　我們最初的模型是＿＿＿＿。
- We think the system works like this: ______.　我們認為這個系統可能如此運作：＿＿＿＿。
- We added ______ to the model.　我們在模型中加入＿＿＿＿。
- The model now includes ______.　目前模型包括＿＿＿＿。
- We use the model to predict ______.　我們使用模型預測＿＿＿＿。
- According to the model, we expect ______.　根據模型，我們預期＿＿＿＿。
- The evidence does not fully support our original model.　證據並未完全支持原來的模型。
- Therefore, we revised the model.　因此我們修改了模型。
- Our revised model suggests ______.　修改後的模型認為＿＿＿＿。

### DEAR 範例：板塊構造

1. **Design**：一開始假設地震是隨機發生。
2. **Elaborate**：加入全球地震分布圖後，發現地震集中成帶狀。
3. **Apply**：用「板塊邊界」模型預測火山與海溝也可能在附近。
4. **Revise**：發現有些火山不在邊界上（例如熱點火山），因此模型需要加入 hotspot。

教師板書可用：

```text
現象：地震、火山、山脈、海溝呈帶狀分布
問題：為什麼？
假說1：地球表面有大型裂縫或邊界
假說2：地下有熱或物質上升
假說3：地球表面板塊正在移動

需要證據：地形、地震位置、地震深度、火山位置、板塊運動方向

CER：  Claim → Evidence → Reasoning
DEAR： Design → Elaborate → Apply → Revise
```

---

## CLIL：用英文整理科學思考

CLIL = **Content and Language Integrated Learning**。這門課不是上英文課，而是用英文句型幫助整理科學思考。完整三例擴充見 `地球物理通論第一堂課｜CLIL句型與三例擴充附錄.md`。

### 八層核心句型（每層取代表句）

**Level 1｜描述現象**

- We observe that ______.　我們觀察到＿＿＿＿。
- The map shows ______.　這張地圖顯示＿＿＿＿。
- The data show that ______.　資料顯示＿＿＿＿。
- There is / There are ______.　有＿＿＿＿。

例：We observe that many earthquakes occur around Taiwan.／The data show that earthquakes are not randomly distributed.

**Level 2｜描述位置**

- ______ is located in / near / to the east of ______.
- ______ is distributed along ______.　＿＿＿＿沿著＿＿＿＿分布。

例：The Philippine Sea Plate is located to the east of Taiwan.／Earthquakes are distributed along plate boundaries.

**Level 3｜比較**

- A is higher / deeper / larger than B.
- Compared with A, B is ______.

例：Compared with continental crust, oceanic crust is thinner.

**Level 4｜因果關係**

- ______ causes ______.／______ is caused by ______.
- Because ______, ______.／Therefore, ______.

例：Plate movement causes earthquakes.／Density differences cause gravity anomalies.

**Level 5｜科學證據**

- The evidence shows that ______.
- According to the data, ______.
- This result suggests that ______.
- This evidence supports the idea that ______.

**Level 6｜提出假說**

- One possible explanation is ______.
- We hypothesize that ______.
- If our hypothesis is correct, we expect ______.

**Level 7｜測試與驗證**

- We can test this idea by ______.
- We need more data to determine whether ______.
- The result is consistent with our hypothesis.
- The result does not support our hypothesis.

**Level 8｜科學模型**

- Our initial model suggests that ______.
- Based on the new evidence, we revised our model.
- The revised model explains ______ better.
- However, the model cannot explain ______.

### 整學期反覆使用的 10 個核心句型

建議固定出現在 PPT、學習單、Colab、GitHub Pages、作業評量規準與小組報告，讓語言成為科學思考工具。

1. We observe that ______.
2. The data show that ______.
3. One possible explanation is ______.
4. We hypothesize that ______.
5. If our hypothesis is correct, we expect ______.
6. The evidence supports our hypothesis because ______.
7. However, ______ cannot be explained by our model.
8. Therefore, we revised our model.
9. We need more data to determine whether ______.
10. AI suggested ______, but we verified it by ______.

第 10 句三例：

- AI suggested that the earthquake pattern is related to plate subduction, but we verified it by comparing earthquake depth with the plate boundary.
- AI suggested that my PyGMT code was incorrect, but we verified it by checking the official documentation and running the revised code.
- AI suggested that the second arrival was a refracted wave, but we verified it by comparing the observed travel time with the theoretical prediction.

### 科學論述六句組

英文程度有限時，先固定使用這六句就能完成基本探究報告：

1. Observation: We observe that ______.
2. Question: We want to know why ______.
3. Hypothesis: We hypothesize that ______.
4. Prediction: If our hypothesis is correct, we expect ______.
5. Evidence: The evidence shows that ______.
6. Conclusion / Revision: Therefore, we support / revise our model.

**板塊構造六句範例**

> We observe that many earthquakes occur around Taiwan.  
> We want to know why earthquakes are concentrated in these regions.  
> We hypothesize that the earthquake distribution is related to plate interactions.  
> If our hypothesis is correct, we expect earthquakes to follow tectonic structures.  
> The evidence shows that earthquake locations form several clear belts.  
> Therefore, we support and further revise our model of plate interactions around Taiwan.

**折射震測六句範例**

> We observe that travel time increases with distance.  
> We want to know why the travel-time graph has two different slopes.  
> We hypothesize that the subsurface contains two layers with different seismic velocities.  
> If our hypothesis is correct, we expect the refracted wave to become the first arrival at longer distances.  
> The evidence shows that the distant stations follow a second travel-time line.  
> Therefore, we support the two-layer model.

**重力探勘六句範例**

> We observe that gravity is higher in the central part of the study area.  
> We want to know why this positive gravity anomaly occurs.  
> We hypothesize that a high-density body exists underground.  
> If our hypothesis is correct, we expect the highest gravity values above the dense body.  
> The evidence shows that the observed gravity anomaly matches the predicted pattern.  
> Therefore, we support the high-density-body model.

### 小組討論與課堂管理英文

討論：What do you think?／Why do you think so?／What is your evidence?／I agree because ______.／I disagree because ______.／Can you explain that again?／Let's compare the two ideas.／Let's ask AI, but we need to verify the answer.／Let's check the data.／I found a different result.／Which explanation is better supported by the evidence?

管理：Please work in groups of two or three.／Choose one group leader.／Please open your laptop.／Please follow my demonstration.／You have ten minutes to complete this task.／Stop here for a moment.／Don't worry if you make a mistake.／Please show me your screen.／Raise your hand if you need help.／Please save your work.／Please keep your AI conversation.／Please upload your work before you leave.

### 第一堂課核心單字（節錄）

**地球物理**：geophysics, Earth's interior, seismic wave, earthquake, gravity, magnetic field, geothermal, plate tectonics, crust, mantle, core, topography, mountain range, trench, fault, seismic survey。

**科學探究**：hypothesis, claim, evidence, reasoning, model, pattern, prediction, test, verify, infer, support, reject, limitation, uncertainty。

**AI 與工具**：generative AI, AI agent, prompt, chatbot, repository, GitHub Pages, notebook, Python, debug, deploy, interaction log。

完整中英對照表見講稿附錄一。

---

## AI 是協作者，不是答案機器

這門課學 AI，不是訓練「把事情全部交給 AI」。若輸入「幫我完成板塊構造報告」再整份貼上，那不叫學習。真正要練習的是：

> Can you evaluate the answer?  
> Can you explain the answer?  
> Can you find evidence to support the answer?  
> Can you identify a mistake?

![概念圖 4｜AI 是協作者，不是答案機器](ChatGPT%20Image%202026年9月9日%20上午01_51_34%20%285%29.png)

人機協作六步：

1. **My Question 學生問題**：提出好奇、定義問題、釐清目標。
2. **AI Suggestion AI 建議**：獲得想法、多元觀點、初步解答。
3. **Evaluation 我的判斷**：思考比較、判斷品質、選擇有用內容。
4. **Evidence 找證據**：查找可靠資料、引用來源、核對事實。
5. **Verification 驗證**：檢查正確性、確認合理性、評估限制。
6. **Revision 修正**：調整想法、完善答案、持續改進。

**AI 對話紀錄 = 學習證據。** 重點不是「AI 幫我做了多少」，而是「我如何判斷、驗證與修正」。流程可記成：Prompt → AI response → My evaluation → Evidence → Revision。

| 工具 | 主要用途 | 你要負責什麼 |
|---|---|---|
| Gemini | 理解課本、提出假說、整理概念 | 判斷回答是否合理 |
| Codex | 寫程式、看錯誤、整理專案 | 檢查程式是否真的能跑 |
| Antigravity | 管理專案、工作流程、artifacts | 檢查任務與成果是否符合需求 |
| OpenCode | 終端機或 IDE 中的程式協作 | 看懂修改內容與差異 |

AI 可以：解釋概念、提出假說、寫程式、除錯、整理網頁文字、翻譯或改寫英文。AI 不可以替你：判斷答案是否正確、決定證據是否足夠、解釋為什麼接受某個模型、取代學習紀錄、隱藏錯誤與不理解。

### 建議保存的 AI Interaction Log

至少保存：Your prompt、AI response、Your evaluation、Evidence、Revision。

```markdown
# AI Interaction Log

## Question
## My Initial Idea
## Prompt 1
## AI Response
## My Evaluation
## Evidence
## Prompt 2
## What Changed?
## Final Reflection
```

表格版可用：階段｜我的 Prompt｜AI 回應摘要｜我的判斷｜驗證方式｜下一步。階段可分成問題形成、假說建立、程式協助、模型修正。

### 好的／不好的 AI 使用

好的例子：

> 我問 AI 為什麼地震沿海溝分布。AI 說可能與隱沒作用有關。但我還不能直接相信，所以我接著問：如果是隱沒作用，地震深度應該如何變化？AI 回答應該形成傾斜震源帶。下一步我想用 PyGMT 畫地震深度分布來檢查。

需要避免：直接問答案沒有追問、沒有保存 Prompt、沒有說明自己是否同意、沒有任何證據、直接複製 AI 文字當報告、AI 說什麼就寫什麼。

當 AI 回答「這是因為板塊構造」時不要立刻停止，繼續問：根據什麼證據？還有沒有其他可能？如果解釋是對的，地圖上應該看到什麼？如果是錯的會出現什麼反例？我可以用什麼資料檢查？這樣 AI 才會從答案機變成探究夥伴。

### Gemini 探究示範 Prompts（第一堂課）

主題：為什麼地震、火山、山脈與海溝常常集中在某些帶狀區域？

**Prompt 1｜形成問題**

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

之後在 Colab 或筆記記錄：AI 提出哪三個假說、哪個最合理、哪個最可疑、AI 有沒有直接跳到板塊構造、還需要什麼資料。

**Prompt 2｜轉成 CER**：把最可能的假說整理成 Claim／Evidence／Reasoning，中文並在每段後附一句簡單英文。

**Prompt 3｜反方評論者**：扮演嚴格的地球物理老師，批判 CER 是否下結論太快、證據是否足夠、推理是否跳躍、還需要哪些資料、哪些可能是幻覺或過度簡化。

**Prompt 4｜連結 DEAR**：把探究歷程整理成 Design／Elaborate／Apply／Revise 表格，並加入簡單英文句型。

**Prompt 5｜建立作業架構**：Research Question、Initial Hypothesis、CER、DEAR Model、English Keywords、Useful English Sentence Patterns、What I need to verify next、AI Interaction Reflection。

小組接著討論：你們的 AI 回答一樣嗎？哪些可靠、哪些要查證？AI 有沒有給出沒有證據的判斷？如果要用 PyGMT 驗證，想畫什麼？

### AI Prompt 常用句型

- Do not give me the final answer directly.　不要直接告訴我最後答案。
- Ask me questions that can help me think about this problem.
- Suggest three possible explanations.
- What evidence would support / contradict this explanation?
- Check my reasoning. Do not rewrite my answer.
- What is the weakest part of my explanation?
- If this model is correct, what should we observe?

---

## 從問題到 GitHub Pages 的數位工作流程

![概念圖 5｜從問題到 GitHub Pages 的數位工作流程](ChatGPT%20Image%202026年9月9日%20上午01_51_34%20%286%29.png)

| 步驟 | 工具 | 做什麼 |
|---|---|---|
| 1 | Gemini | 提出問題、釐清概念、發想研究方向 |
| 2 | Google Colab（Python／PyGMT） | 取得資料、撰寫程式、分析與繪圖 |
| 3 | AI Agent（Codex／Antigravity／OpenCode） | 生成、除錯、優化程式 |
| 4 | GitHub | 管理版本、分享成果、協作與備份 |
| 5 | GitHub Pages | 製作網頁、展示成果、對外分享 |
| 6 | Peer Sharing | 交流討論、回饋建議、持續改進 |

可重現的數位學習歷程：

```text
Question → Data → Code → Figure → Interpretation → AI Log → Webpage
```

每一步都能留下紀錄、被檢查、被修改。學術文化重視 evidence、documentation、reproducibility。

### 期末專題網站建議架構

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

網站內容至少包含：Research Question、Background、English Keywords、Initial Model、Data and Method、PyGMT Map、CER Explanation、DEAR Model Revision、AI Interaction Log、3D Model or Visualization、Final Explanation、Limitations、References。

---

## PyGMT 示範筆記本

檔案：[`pygmt_plot_plate_boundary.ipynb`](pygmt_plot_plate_boundary.ipynb)

可在 Colab 開啟（原始連結指向 `oceanicdayi/plot_plate_boundary_pygmt`）：

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/oceanicdayi/plot_plate_boundary_pygmt/blob/main/pygmt_plot_plate_boundary.ipynb)

### 環境說明

Google Colab 目前 Python 約為 3.12，conda／mamba 解析可能暫時不相容。筆記本因此先安裝相容的 condacolab／Miniforge，再安裝 **PyGMT 0.17**（搭配 GMT 6.5.0）。核心會自動重啟一次，屬正常現象。接著以 mamba 安裝 `pygmt` 與 `obspy`。

### 筆記本做了什麼

1. **全球地形＋熱點**  
   讀取 `load_earth_relief(resolution='01d')`（SRTM15 Earth Relief v2.7），使用正交投影 `G330/-30/12c`，疊加岸線與 `@hotspots.txt`（紅色圓點），並加上 colorbar。
2. **台灣海岸線示意**  
   區域 `119/123/21/26`，Mercator 投影 `M15c`，陸地灰色、海域藍色。
3. **台灣地形圖**  
   同一區域改用 `resolution='05m'` 的 Earth relief，`cmap='geo'` 加陰影與高解析岸線。

檔名含 plate boundary，但目前儲存的輸出以全球／台灣地形為主，板塊邊界疊圖會在後續週次（Week 2 起）正式進入課堂。PyGMT 在這門課的角色是：繪製地形、顯示海溝／中洋脊／山脈、疊加地震與火山、比較資料分布與模型、產生可放進網頁與報告的圖。

下週會開始：在 Colab 安裝 PyGMT、繪製全球地形圖、觀察海溝／中洋脊／山脈、思考地形與板塊構造的關係，並產生第一張可放到 GitHub Pages 的圖。要問的問題包括：Are mountains / trenches / earthquakes randomly distributed?

---

## 第一堂課作業

### 作業一：工具確認

1. GitHub 帳號與練習 repository 連結。
2. Google Colab notebook 連結或截圖。
3. Gemini 對話紀錄。
4. 小組名單。

### 作業二：AI 探究紀錄

主題：

> 為什麼地震、火山、山脈與海溝常常集中在某些帶狀區域？

繳交：Gemini 對話紀錄、CER 整理、DEAR 整理、100–200 字反思。

建議格式：

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

反思問題：AI 幫助我理解了什麼？我有沒有懷疑 AI 的回答？我下一步想用什麼資料驗證？

---

## 課堂規範與下週預告

請注意：尊重智慧財產權；使用正版教材與合法資料來源；不任意複製、散布未授權內容；使用 AI 時標示協助範圍；小組合作公平分工；課堂討論尊重不同背景與觀點；不製作違反性別平等或歧視性內容。

**下週之前請完成**：GitHub 帳號、Google Colab notebook、Gemini 對話紀錄、CER 與 DEAR 作業、小組名單。

**下週請帶**：可上網筆電、Google 帳號、GitHub 帳號、今天的 AI 探究紀錄。

**下週主題：PyGMT — Visualizing the Earth**

不是只看教科書裡已經畫好的圖，而是自己用資料把地球畫出來。然後問：

> 地球表面的形狀，是否已經透露了板塊運動的證據？

教師收尾要記住的三問：

> **What do we know?**　我們知道什麼？  
> **How do we know?**　我們怎麼知道？  
> **How can we test it?**　我們如何驗證？

第一堂課不追求所有人立刻熟練工具。今天真正要建立的是：任務模式、AI 紀錄意識、GitHub／Colab 最低操作能力、科學探究框架、CLIL 句型使用習慣。只要理解「AI 的回答需要被判斷，科學主張需要證據支持」，這堂課就成功了。

---

## 如何使用本倉庫

1. 課堂投影請開 [互動課堂頁](https://oceanicdayi.github.io/2026_Utaipei_Geophysics_0909/)：← → 換頁、上方計時、導論／正演反演／折射建模、CER／DEAR／CLIL 可即席操作。折射建模可用 `?stage=a#refrac` 只顯示 a 圖。
2. 先讀本 README，掌握課程定位、18 週路線與第一堂課任務。
3. 上課投影片請用 `地球物理通論_第一堂課_PPT詳細版.md`（Marp）；口語節奏請對照三小時講稿。
4. 句型練習、CER／DEAR 擴充三例、AI Prompt 與課堂英文，請用 CLIL 附錄。
5. Colab／PyGMT 操作從 `pygmt_plot_plate_boundary.ipynb` 開始。
6. 概念圖可直接插入簡報或網頁；檔名與概念圖序號對照見上方檔案一覽。
7. 修正與新增教材時，請同步更新本 README、課堂頁與 `修正紀錄.md`。重新輸出 PDF 時請保持 Markdown 與 PDF 檔名對應。

### 課堂頁本機預覽

```bash
python3 -m http.server 8080 --directory docs
```

瀏覽器開啟 `http://localhost:8080`。GitHub Pages 由 `.github/workflows/pages.yml` 在 `main` 分支推送後部署。若網站尚未出現，請到倉庫 **Settings → Pages**，Source 選 **GitHub Actions**（只需設定一次）。workflow 已設定 `enablement: true`，合併後會嘗試自動開啟 Pages。

### 給教師的提醒（簡報附錄）

地球物理真正有趣的地方，是常常看不到地下，但可以從地表觀測到的訊號（地震波、重力、磁力、電性與熱流）去推論地球裡面可能長什麼樣子。AI、Python、PyGMT、GitHub 與 3D 列印不是為了炫技，而是讓抽象概念變成看得見、可以討論、可以檢驗的成果。

請學生先不要急著回答「板塊構造」。如果你是第一個觀察地球的人，只看到深海溝、高山脈、地震沿一條線分布、火山集中在某些區域——你會怎麼解釋？這就是科學探究的開始。
