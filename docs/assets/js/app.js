const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

const store = {
  get(key, fallback) {
    try {
      const raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch {
      return fallback;
    }
  },
  set(key, value) {
    localStorage.setItem(key, JSON.stringify(value));
  },
};

function pad(n) {
  return String(n).padStart(2, "0");
}

function tickClock() {
  const now = new Date();
  const el = $("#clock");
  if (el) el.textContent = `${pad(now.getHours())}:${pad(now.getMinutes())}`;
}

function setTheme(theme) {
  document.documentElement.dataset.theme = theme;
  store.set("theme", theme);
}

function typesetMath() {
  if (window.renderMathInElement) {
    window.renderMathInElement(document.body, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "\\(", right: "\\)", display: false },
      ],
      throwOnError: false,
    });
  }
}

function showView(id) {
  $$(".view").forEach((v) => v.classList.toggle("active", v.id === `view-${id}`));
  $$(".nav button").forEach((b) => b.setAttribute("aria-current", b.dataset.view === id ? "page" : "false"));
  location.hash = id;
  const view = $(`#view-${id}`);
  if (view) view.scrollIntoView({ block: "start" });
  typesetMath();
}

function setRefracStage(id) {
  $$(".stage-panel").forEach((p) => p.classList.toggle("on", p.dataset.stage === id));
  $$("[data-stage-btn]").forEach((b) => b.classList.toggle("primary", b.dataset.stageBtn === id));
  $$("#model-cycle [data-stage-btn]").forEach((b) => b.classList.toggle("active", b.dataset.stageBtn === id));
  store.set("refrac-stage", id);
}

function currentViewIndex() {
  const id = location.hash.replace("#", "") || "open";
  const i = VIEWS.findIndex((v) => v.id === id);
  return i < 0 ? 0 : i;
}

function moveView(step) {
  const next = (currentViewIndex() + step + VIEWS.length) % VIEWS.length;
  showView(VIEWS[next].id);
}

function renderNav() {
  const nav = $("#nav");
  nav.innerHTML = VIEWS.map((v) => `<button type="button" data-view="${v.id}">${v.label}</button>`).join("");
  nav.addEventListener("click", (e) => {
    const btn = e.target.closest("button");
    if (btn) showView(btn.dataset.view);
  });
}

function renderWeeks() {
  $("#week-grid").innerHTML = WEEKS.map(
    (w) => `<button class="week" type="button" data-week="${w.n}"><b>Week ${w.n}</b>${w.title}<small class="help" style="display:block;margin-top:.35rem">${w.task}</small></button>`
  ).join("");
  $("#week-grid").addEventListener("click", (e) => {
    const btn = e.target.closest(".week");
    if (!btn) return;
    $$(".week").forEach((w) => w.classList.toggle("active", w === btn));
    const w = WEEKS.find((x) => String(x.n) === btn.dataset.week);
    $("#week-detail").innerHTML = `<strong>Week ${w.n}</strong>　${w.title}<br><span class="help">${w.task}</span>`;
  });
}

function renderTasks() {
  const done = store.get("tasks-done", {});
  const nowId = store.get("task-now", "t1");
  $("#task-list").innerHTML = TASKS.map((t) => {
    const checked = done[t.id] ? "checked" : "";
    return `<article class="task ${nowId === t.id ? "now" : ""}" data-id="${t.id}">
      <time>${t.time}</time>
      <div>
        <label><input type="checkbox" data-check="${t.id}" ${checked}> <strong>${t.title}</strong></label>
        <div class="help">${t.note}</div>
      </div>
      <button type="button" class="btn ghost" data-now="${t.id}">現在進行</button>
    </article>`;
  }).join("");
}

function bindTasks() {
  const list = $("#task-list");
  list.addEventListener("click", (e) => {
    const nowBtn = e.target.closest("[data-now]");
    if (!nowBtn) return;
    store.set("task-now", nowBtn.dataset.now);
    renderTasks();
  });
  list.addEventListener("change", (e) => {
    if (!e.target.dataset.check) return;
    const done = store.get("tasks-done", {});
    done[e.target.dataset.check] = e.target.checked;
    store.set("tasks-done", done);
  });
}

function loadCer(key) {
  const ex = CER_EXAMPLES[key] || CER_EXAMPLES.blank;
  $("#cer-q").value = ex.q;
  $("#cer-claim").value = ex.claim;
  $("#cer-evidence").value = ex.evidence;
  $("#cer-reasoning").value = ex.reasoning;
  persistCer();
}

function persistCer() {
  store.set("cer", {
    q: $("#cer-q").value,
    claim: $("#cer-claim").value,
    evidence: $("#cer-evidence").value,
    reasoning: $("#cer-reasoning").value,
  });
}

function restoreCer() {
  const saved = store.get("cer");
  if (!saved) return;
  $("#cer-q").value = saved.q || "課堂即席題";
  $("#cer-claim").value = saved.claim || "";
  $("#cer-evidence").value = saved.evidence || "";
  $("#cer-reasoning").value = saved.reasoning || "";
}

function renderDear() {
  $("#dear-cycle").innerHTML = DEAR.map(
    (d, i) => `<button class="dear-step ${i === 0 ? "active" : ""}" type="button" data-i="${i}">
      <b>${d.key}</b><strong>${d.en}</strong>
      <div>${d.zh}</div>
      <div class="help">${d.q}</div>
    </button>`
  ).join("");
  const saved = store.get("dear-notes", { D: "", E: "", A: "", R: "" });
  $("#dear-note").value = saved.D || "";
  $("#dear-cycle").addEventListener("click", (e) => {
    const btn = e.target.closest(".dear-step");
    if (!btn) return;
    $$(".dear-step").forEach((s) => s.classList.toggle("active", s === btn));
    const d = DEAR[Number(btn.dataset.i)];
    $("#dear-prompt").textContent = `${d.key} — ${d.q}`;
    $("#dear-note").value = store.get("dear-notes", {})[d.key] || "";
    $("#dear-note").dataset.key = d.key;
  });
  $("#dear-note").dataset.key = "D";
  $("#dear-note").addEventListener("input", () => {
    const notes = store.get("dear-notes", {});
    notes[$("#dear-note").dataset.key] = $("#dear-note").value;
    store.set("dear-notes", notes);
  });
}

let clilIndex = 0;

function showClil(i) {
  clilIndex = (i + CLIL_BANK.length) % CLIL_BANK.length;
  const item = CLIL_BANK[clilIndex];
  $("#clil-en").textContent = item.en;
  $("#clil-zh").textContent = item.zh;
  $("#clil-meta").textContent = `Level ${item.lv}　${clilIndex + 1} / ${CLIL_BANK.length}`;
}

function showCore(i) {
  const item = CORE10[i];
  $("#core-en").textContent = item.en;
  $("#core-zh").textContent = item.zh;
  $("#core-n").textContent = `${i + 1} / 10`;
  $$("[data-core]").forEach((b) => b.classList.toggle("primary", Number(b.dataset.core) === i));
}

function renderCoreButtons() {
  $("#core-btns").innerHTML = CORE10.map((_, i) => `<button class="btn" type="button" data-core="${i}">${i + 1}</button>`).join("");
  $("#core-btns").addEventListener("click", (e) => {
    if (e.target.dataset.core) showCore(Number(e.target.dataset.core));
  });
}

function renderPrompts() {
  $("#prompt-list").innerHTML = PROMPTS.map(
    (p, i) => `<article class="card">
      <h3>${p.title}</h3>
      <pre id="prompt-${i}" style="white-space:pre-wrap;font-family:var(--font-sans);background:var(--paper-2);padding:.8rem;border-radius:12px">${p.text}</pre>
      <button class="btn primary" type="button" data-copy="${i}">複製 Prompt</button>
    </article>`
  ).join("");
  $("#prompt-list").addEventListener("click", async (e) => {
    if (!e.target.dataset.copy) return;
    const text = PROMPTS[Number(e.target.dataset.copy)].text;
    await navigator.clipboard.writeText(text);
    e.target.textContent = "已複製";
    setTimeout(() => (e.target.textContent = "複製 Prompt"), 1200);
  });
}

function sixSet(name) {
  const lines = SIX_SETS[name];
  $("#six-box").innerHTML = lines.map((l, i) => `<p><b>${i + 1}.</b> ${l}</p>`).join("");
  $$("[data-six]").forEach((b) => b.classList.toggle("primary", b.dataset.six === name));
}

let timerRemain = 0;
let timerId = null;

function formatRemain(s) {
  return `${pad(Math.floor(s / 60))}:${pad(s % 60)}`;
}

function renderTimer() {
  $("#timer-digits").textContent = formatRemain(timerRemain);
}

function startTimer(seconds) {
  clearInterval(timerId);
  timerRemain = seconds;
  $("#timer-overlay").classList.add("open");
  renderTimer();
  timerId = setInterval(() => {
    timerRemain -= 1;
    renderTimer();
    if (timerRemain <= 0) {
      clearInterval(timerId);
      $("#timer-digits").textContent = "時間到";
    }
  }, 1000);
}

function openChorus(text) {
  $("#chorus-text").textContent = text;
  $("#chorus-overlay").classList.add("open");
}

function exportExit() {
  const data = {
    name: $("#exit-name").value,
    q1: $("#exit-q1").value,
    q2: $("#exit-q2").value,
    q3: $("#exit-q3").value,
  };
  store.set("exit", data);
  const md = `# Week 01 Exit Ticket

- 姓名：${data.name}
- Today I learned that geophysics is ${data.q1}
- One digital tool I used today was ${data.q2}
- One question I still have is ${data.q3}
`;
  const blob = new Blob([md], { type: "text/markdown" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "week01-exit-ticket.md";
  a.click();
}

function restoreExit() {
  const data = store.get("exit", {});
  $("#exit-name").value = data.name || "";
  $("#exit-q1").value = data.q1 || "";
  $("#exit-q2").value = data.q2 || "";
  $("#exit-q3").value = data.q3 || "";
}

function bindGlobal() {
  $("#btn-theme").addEventListener("click", () => {
    const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    setTheme(next);
  });
  $("#btn-full").addEventListener("click", () => {
    if (!document.fullscreenElement) document.documentElement.requestFullscreen();
    else document.exitFullscreen();
  });
  $("#btn-prev").addEventListener("click", () => moveView(-1));
  $("#btn-next").addEventListener("click", () => moveView(1));
  $$("[data-timer]").forEach((b) => b.addEventListener("click", () => startTimer(Number(b.dataset.timer))));
  $("#timer-close").addEventListener("click", () => {
    clearInterval(timerId);
    $("#timer-overlay").classList.remove("open");
  });
  $("#chorus-close").addEventListener("click", () => $("#chorus-overlay").classList.remove("open"));
  $("#btn-chorus-core").addEventListener("click", () => openChorus(`${$("#core-en").textContent}\n${$("#core-zh").textContent}`));
  $("#btn-chorus-clil").addEventListener("click", () => openChorus(`${$("#clil-en").textContent}\n${$("#clil-zh").textContent}`));
  $("#clil-prev").addEventListener("click", () => showClil(clilIndex - 1));
  $("#clil-next").addEventListener("click", () => showClil(clilIndex + 1));
  $("#clil-rand").addEventListener("click", () => showClil(Math.floor(Math.random() * CLIL_BANK.length)));
  $$("[data-cer]").forEach((b) => b.addEventListener("click", () => loadCer(b.dataset.cer)));
  ["cer-q", "cer-claim", "cer-evidence", "cer-reasoning"].forEach((id) => $(`#${id}`).addEventListener("input", persistCer));
  $("#cer-project").addEventListener("click", () => $("#cer-board").classList.toggle("project-mode"));
  $$("[data-six]").forEach((b) => b.addEventListener("click", () => sixSet(b.dataset.six)));
  $("#exit-save").addEventListener("click", exportExit);
  document.addEventListener("click", (e) => {
    const img = e.target.closest("img.concept");
    if (!img) return;
    $("#lightbox-img").src = img.src;
    $("#lightbox").classList.add("open");
  });
  $("#lightbox").addEventListener("click", () => $("#lightbox").classList.remove("open"));
  $$("[data-stage-btn]").forEach((b) => b.addEventListener("click", () => setRefracStage(b.dataset.stageBtn)));
  document.addEventListener("keydown", (e) => {
    if (["INPUT", "TEXTAREA"].includes(e.target.tagName)) return;
    if (e.key === "ArrowRight") moveView(1);
    if (e.key === "ArrowLeft") moveView(-1);
    if (e.key === "Escape") {
      $("#timer-overlay").classList.remove("open");
      $("#chorus-overlay").classList.remove("open");
      $("#lightbox").classList.remove("open");
    }
  });
  window.addEventListener("hashchange", () => {
    const id = location.hash.replace("#", "") || "open";
    if (VIEWS.some((v) => v.id === id)) showView(id);
  });
}

function init() {
  setTheme(store.get("theme", "light"));
  renderNav();
  renderWeeks();
  renderTasks();
  bindTasks();
  renderDear();
  renderCoreButtons();
  showCore(0);
  showClil(0);
  renderPrompts();
  sixSet("plate");
  restoreCer();
  restoreExit();
  bindGlobal();
  setRefracStage(store.get("refrac-stage", "a"));
  tickClock();
  setInterval(tickClock, 1000);
  const start = location.hash.replace("#", "") || "open";
  showView(VIEWS.some((v) => v.id === start) ? start : "open");
  setTimeout(typesetMath, 400);
  const params = new URLSearchParams(location.search);
  const timerQ = Number(params.get("timer"));
  if (timerQ > 0) startTimer(timerQ);
  if (params.get("cer")) loadCer(params.get("cer"));
  if (params.get("chorus") === "1") openChorus(`${$("#core-en").textContent}\n${$("#core-zh").textContent}`);
  if (params.get("stage")) {
    setRefracStage(params.get("stage"));
    showView("refrac");
  }
}

document.addEventListener("DOMContentLoaded", init);
