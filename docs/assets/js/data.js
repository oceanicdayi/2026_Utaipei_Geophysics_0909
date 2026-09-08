const COURSE = {
  title: "地球物理通論",
  english: "General Geophysics",
  school: "臺北市立大學　地球環境暨生物資源學系",
  term: "第 115 學年第 1 學期",
  teacher: "陳達毅（Dayi Chen）",
  when: "第一堂課　09:00–12:00",
  audience: "地生系二年級",
};

const VIEWS = [
  { id: "open", label: "開場" },
  { id: "course", label: "這門課" },
  { id: "weeks", label: "18週" },
  { id: "today", label: "今日任務" },
  { id: "geo", label: "地球物理" },
  { id: "intro", label: "導論" },
  { id: "fwdinv", label: "正演反演" },
  { id: "refrac", label: "折射建模" },
  { id: "apps", label: "應用" },
  { id: "cer", label: "CER" },
  { id: "dear", label: "DEAR" },
  { id: "clil", label: "CLIL" },
  { id: "ai", label: "AI 協作" },
  { id: "flow", label: "數位流程" },
  { id: "prompts", label: "Prompts" },
  { id: "work", label: "作業" },
  { id: "exit", label: "Exit Ticket" },
];

const WEEKS = [
  { n: 1, title: "課程說明與系統安裝", task: "建立工具與任務模式" },
  { n: 2, title: "PyGMT 繪製全球地圖", task: "畫出地球表面資料" },
  { n: 3, title: "板塊構造與 3D 列印", task: "從地形建立模型" },
  { n: 4, title: "板塊構造與 3D 列印", task: "修正模型與展示" },
  { n: 5, title: "校園野外實驗：折射探勘", task: "實地量測" },
  { n: 6, title: "折射探勘原理", task: "建立走時模型" },
  { n: 7, title: "折射探勘與期中準備", task: "整合理論與資料" },
  { n: 8, title: "期中考", task: "概念與方法檢核" },
  { n: 9, title: "重力與 Geoid 3D 列印", task: "看見看不見的重力場" },
  { n: 10, title: "重力", task: "解釋地下密度差異" },
  { n: 11, title: "專題演講", task: "連結真實研究與職涯" },
  { n: 12, title: "板塊構造與地熱", task: "能源與地球內部熱" },
  { n: 13, title: "地電與地磁", task: "了解地下電性與磁性" },
  { n: 14, title: "地電與地磁", task: "資料解釋與應用" },
  { n: 15, title: "期末專題發表", task: "第一輪發表" },
  { n: 16, title: "期末專題發表", task: "第二輪發表" },
  { n: 17, title: "實習、參訪", task: "延伸學習" },
  { n: 18, title: "實習、參訪", task: "延伸學習" },
];

const TASKS = [
  { id: "t1", time: "09:00–09:10", title: "教師自我介紹", note: "Question → Evidence → Model → Test → Revision" },
  { id: "t2", time: "09:10–09:30", title: "課程理念與內容", note: "Geo + Physics；三條主線；AI 是 collaborator" },
  { id: "t3", time: "09:30–09:40", title: "上課方式與評量", note: "示範 → 練習 → 探究 → 解釋 → 發表" },
  { id: "t4", time: "09:40–09:50", title: "分組", note: "2–3 人一組，選出組長" },
  { id: "break1", time: "09:50–10:00", title: "休息", note: "See you in ten minutes." },
  { id: "t5", time: "10:00–10:25", title: "AI Agent", note: "Chatbot 答題 vs Agent 完成任務" },
  { id: "t6", time: "10:25–10:50", title: "GitHub", note: "建立 repo 與 README，當成學習歷程" },
  { id: "break2", time: "10:50–11:00", title: "休息", note: "See you in ten minutes." },
  { id: "t7", time: "11:00–11:20", title: "Google Colab", note: "t = d / v；科學筆記本" },
  { id: "t8", time: "11:20–11:40", title: "什麼是地球物理", note: "Observe → Analyze → Infer" },
  { id: "t9", time: "11:40–11:55", title: "Gemini + CER", note: "不要直接要答案；保存 AI 對話" },
  { id: "t10", time: "11:55–12:00", title: "Exit Ticket", note: "三句課後回饋" },
];

const METHODS = [
  { name: "震測", observe: "地震波速度與走時", infer: "地下構造、斷層、地殼厚度" },
  { name: "重力", observe: "重力異常", infer: "地下密度差異、盆地、山根" },
  { name: "地磁", observe: "磁場變化", infer: "岩石磁性、海底擴張、構造" },
  { name: "地電", observe: "電阻率", infer: "地下水、熱液、斷層帶" },
  { name: "地熱", observe: "熱流與溫度", infer: "地熱資源、地球內部熱" },
  { name: "GPS", observe: "地表位移", infer: "板塊運動、斷層滑移" },
];

const CER_EXAMPLES = {
  blank: {
    q: "課堂即席題",
    claim: "",
    evidence: "",
    reasoning: "",
  },
  taiwan: {
    q: "為什麼台灣附近經常發生地震？",
    claim: "Our claim is that earthquake activity around Taiwan is related to plate interactions.",
    evidence: "The earthquake map shows that earthquakes are concentrated in specific regions around Taiwan.",
    reasoning: "If earthquakes are related to plate interactions, their locations should follow tectonic structures rather than being randomly distributed.",
  },
  japan: {
    q: "為什麼日本附近常發生地震？",
    claim: "日本附近可能位在板塊邊界，且有板塊隱沒作用。",
    evidence: "日本東側有深海溝，地震沿海溝呈帶狀分布，且震源深度往內陸方向逐漸增加。",
    reasoning: "如果一個板塊向另一個板塊下方隱沒，地震會沿著傾斜的板塊界面發生，因此會形成由淺到深的地震帶。",
  },
  seismic: {
    q: "走時曲線為什麼有兩段斜率？",
    claim: "The lower layer has a higher seismic velocity.",
    evidence: "The travel-time graph contains two line segments with different slopes.",
    reasoning: "Because the slope of a travel-time line is related to seismic velocity, the different slopes indicate different seismic velocities.",
  },
  gravity: {
    q: "為什麼測區中央重力較高？",
    claim: "A high-density body exists underground.",
    evidence: "A positive gravity anomaly is observed above the study area.",
    reasoning: "A high-density body produces greater gravitational attraction, so the positive anomaly supports the claim.",
  },
};

const DEAR = [
  { key: "D", en: "Design a model", zh: "建立初始模型", q: "我們認為正在發生什麼？" },
  { key: "E", en: "Elaborate the model", zh: "加入新證據與細節", q: "還需要加入什麼？" },
  { key: "A", en: "Apply the model", zh: "用模型預測", q: "我們應該觀察到什麼？" },
  { key: "R", en: "Revise the model", zh: "根據結果修正", q: "哪些地方需要改變？" },
];

const CORE10 = [
  { en: "We observe that ______.", zh: "我們觀察到＿＿＿＿。" },
  { en: "The data show that ______.", zh: "資料顯示＿＿＿＿。" },
  { en: "One possible explanation is ______.", zh: "一個可能的解釋是＿＿＿＿。" },
  { en: "We hypothesize that ______.", zh: "我們假設＿＿＿＿。" },
  { en: "If our hypothesis is correct, we expect ______.", zh: "如果假說正確，我們預期＿＿＿＿。" },
  { en: "The evidence supports our hypothesis because ______.", zh: "證據支持我們的假說，因為＿＿＿＿。" },
  { en: "However, ______ cannot be explained by our model.", zh: "但是＿＿＿＿無法由目前模型解釋。" },
  { en: "Therefore, we revised our model.", zh: "因此我們修改模型。" },
  { en: "We need more data to determine whether ______.", zh: "我們需要更多資料確認是否＿＿＿＿。" },
  { en: "AI suggested ______, but we verified it by ______.", zh: "AI 建議＿＿＿＿，但是我們透過＿＿＿＿進行驗證。" },
];

const SIX_SETS = {
  plate: [
    "We observe that many earthquakes occur around Taiwan.",
    "We want to know why earthquakes are concentrated in these regions.",
    "We hypothesize that the earthquake distribution is related to plate interactions.",
    "If our hypothesis is correct, we expect earthquakes to follow tectonic structures.",
    "The evidence shows that earthquake locations form several clear belts.",
    "Therefore, we support and further revise our model of plate interactions around Taiwan.",
  ],
  seismic: [
    "We observe that travel time increases with distance.",
    "We want to know why the travel-time graph has two different slopes.",
    "We hypothesize that the subsurface contains two layers with different seismic velocities.",
    "If our hypothesis is correct, we expect the refracted wave to become the first arrival at longer distances.",
    "The evidence shows that the distant stations follow a second travel-time line.",
    "Therefore, we support the two-layer model.",
  ],
  gravity: [
    "We observe that gravity is higher in the central part of the study area.",
    "We want to know why this positive gravity anomaly occurs.",
    "We hypothesize that a high-density body exists underground.",
    "If our hypothesis is correct, we expect the highest gravity values above the dense body.",
    "The evidence shows that the observed gravity anomaly matches the predicted pattern.",
    "Therefore, we support the high-density-body model.",
  ],
};

const CLIL_BANK = [
  { lv: 1, en: "We observe that many earthquakes occur around Taiwan.", zh: "我們觀察到台灣周圍發生許多地震。" },
  { lv: 1, en: "The map shows a deep trench east of Taiwan.", zh: "這張地圖顯示台灣東方有一條深海溝。" },
  { lv: 1, en: "The data show that earthquakes are not randomly distributed.", zh: "資料顯示地震並不是隨機分布。" },
  { lv: 2, en: "The Philippine Sea Plate is located to the east of Taiwan.", zh: "菲律賓海板塊位於台灣東方。" },
  { lv: 2, en: "Earthquakes are distributed along plate boundaries.", zh: "地震沿著板塊邊界分布。" },
  { lv: 3, en: "Compared with continental crust, oceanic crust is thinner.", zh: "與大陸地殼相比，海洋地殼較薄。" },
  { lv: 3, en: "The Central Mountain Range is higher than the Western Plain.", zh: "中央山脈比西部平原高。" },
  { lv: 4, en: "Plate movement causes earthquakes.", zh: "板塊運動造成地震。" },
  { lv: 4, en: "Density differences cause gravity anomalies.", zh: "密度差異造成重力異常。" },
  { lv: 5, en: "This evidence supports the idea that the seafloor is spreading.", zh: "這項證據支持海底正在擴張的想法。" },
  { lv: 5, en: "According to the data, most earthquakes occur near plate boundaries.", zh: "根據資料，多數地震發生在板塊邊界附近。" },
  { lv: 6, en: "If our hypothesis is correct, we expect earthquakes to cluster near the plate boundary.", zh: "如果假說正確，我們預期地震會集中在板塊邊界附近。" },
  { lv: 7, en: "We can test this idea by mapping earthquake locations.", zh: "我們可以透過繪製地震位置驗證這個想法。" },
  { lv: 7, en: "The result is consistent with our hypothesis.", zh: "結果與我們的假說一致。" },
  { lv: 8, en: "Based on the new evidence, we revised our model.", zh: "根據新的證據，我們修改了模型。" },
  { lv: 8, en: "However, the model cannot explain all deep earthquakes.", zh: "但是這個模型無法解釋所有深層地震。" },
];

const PROMPTS = [
  {
    title: "Prompt 1｜形成問題",
    text: `我正在修一門地球物理通論課。
今天的問題是：為什麼地震、火山、山脈與海溝常常集中在某些帶狀區域？

請不要直接給我標準答案。
請先用高中到大學一年級程度，幫我提出三個可能假說。
每個假說都要說明：
1. 這個假說如何解釋現象？
2. 需要哪些證據來檢驗？
3. 這個假說可能有什麼限制？`,
  },
  {
    title: "Prompt 2｜轉成 CER",
    text: `請把剛才最可能的假說整理成 CER 格式。

Claim：一句話主張。
Evidence：列出至少三種需要的證據。
Reasoning：說明為什麼這些證據能支持主張。

請使用中文，並在每一段後面附上一句簡單英文句型。`,
  },
  {
    title: "Prompt 3｜反方評論者",
    text: `現在請你扮演一位嚴格的地球物理老師。
請批判我剛才的 CER。

請指出：
1. Claim 是否太快下結論？
2. Evidence 是否足夠？
3. Reasoning 是否有跳躍？
4. 還需要哪些資料？
5. 哪些地方可能是 AI 幻覺或過度簡化？`,
  },
  {
    title: "Prompt 4｜連結 DEAR",
    text: `請把我的探究歷程整理成 DEAR 模型：

D: Design a model，我一開始的模型是什麼？
E: Elaborate the model，加入哪些資料後模型變得更完整？
A: Apply the model，這個模型可以解釋哪些新現象？
R: Revise the model，這個模型有哪些限制，需要如何修正？

請用表格呈現，並加入簡單英文句型。`,
  },
  {
    title: "Prompt 5｜建立作業架構",
    text: `請幫我根據今天的探究，建立一份學習紀錄架構。
我的主題是：地震、火山、山脈與海溝的分布。

請包含：
1. Research Question
2. Initial Hypothesis
3. CER
4. DEAR Model
5. English Keywords
6. Useful English Sentence Patterns
7. What I need to verify next
8. AI Interaction Reflection`,
  },
];
