const state = {
  items: [],
  idx: 0,
  autoAdvanceSec: 0,   // 0 = off
  speak: true,
  sse: null,
};

const el = {
  title: () => document.querySelector(".title"),
  source: () => document.querySelector(".meta .source"),
  time: () => document.querySelector(".meta .time"),
  sentiment: () => document.querySelector(".meta .sent"),
  summary: () => document.querySelector(".summary"),
  link: () => document.querySelector(".readlink"),
  list: () => document.querySelector(".list"),
  pos: () => document.querySelector(".pos"),
  auto: () => document.querySelector("#auto"),
  speak: () => document.querySelector("#speak"),
};

function fmtTime(iso) {
  try { return new Date(iso).toLocaleString(); } catch { return iso; }
}
function fmtSent(s) {
  if (s === null || s === undefined) return "–";
  const sign = s > 0 ? "+" : s < 0 ? "−" : "±";
  return `${sign}${Math.abs(s).toFixed(3)}`;
}

function renderList() {
  const ul = el.list();
  ul.innerHTML = "";
  state.items.forEach((n, i) => {
    const div = document.createElement("div");
    div.className = "item" + (i === state.idx ? " active" : "");
    div.innerHTML = `<div style="font-weight:600">${n.title}</div>
      <div style="font-size:12px;color:#94a3b8">${n.source} • ${fmtTime(n.published_at)} • <span class="sent">${fmtSent(n.sentiment)}</span></div>`;
    div.onclick = () => { state.idx = i; renderMain(); renderList(); maybeSpeak(); };
    ul.appendChild(div);
  });
  el.pos().textContent = `${state.idx + 1}/${state.items.length}`;
}

function renderMain() {
  const n = state.items[state.idx];
  if (!n) return;
  el.title().textContent = n.title;
  el.source().textContent = n.source;
  el.time().textContent = fmtTime(n.published_at);
  el.sentiment().textContent = fmtSent(n.sentiment);
  el.summary().textContent = n.summary || "(no summary)";
  el.link().href = n.link;
}

function speak(text) {
  if (!state.speak) return;
  try {
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.rate = 1.03;
    window.speechSynthesis.speak(u);
  } catch {}
}
function maybeSpeak() {
  const n = state.items[state.idx];
  if (n) speak(`${n.source}. ${n.title}. ${n.summary || ""}`);
}

function next(delta=1) {
  if (!state.items.length) return;
  state.idx = (state.idx + delta + state.items.length) % state.items.length;
  renderMain(); renderList(); maybeSpeak();
}
function setAuto(sec) {
  state.autoAdvanceSec = sec;
  clearInterval(window.__advTimer);
  if (sec > 0) {
    window.__advTimer = setInterval(()=>next(+1), sec*1000);
  }
}

async function loadInitial() {
  const res = await fetch("/api/news?limit=30");
  const data = await res.json();
  state.items = data;
  state.idx = 0;
  renderMain();
  renderList();
  maybeSpeak();
}

function connectSSE() {
  state.sse = new EventSource("/stream");
  state.sse.addEventListener("news", (e) => {
    try {
      const n = JSON.parse(e.data);
      // dedupe by id
      if (!state.items.find(x => x.id === n.id)) {
        state.items.unshift(n);
        // keep list bounded
        if (state.items.length > 100) state.items.pop();
        renderList();
      }
    } catch {}
  });
}

function bindUI() {
  // keyboard
  window.addEventListener("keydown", (e) => {
    if (e.key === "ArrowDown" || e.key === "ArrowRight" || e.key === "j") next(+1);
    if (e.key === "ArrowUp"   || e.key === "ArrowLeft"  || e.key === "k") next(-1);
    if (e.key === " ") { e.preventDefault(); next(+1); }
  });
  // toggles
  el.speak().addEventListener("change", (e)=> {
    state.speak = e.target.checked;
    if (state.speak) maybeSpeak(); else window.speechSynthesis.cancel();
  });
  el.auto().addEventListener("change", (e)=> {
    const sec = Number(e.target.value);
    setAuto(sec);
  });
}

(async function start(){
  bindUI();
  await loadInitial();
  connectSSE();
})();

