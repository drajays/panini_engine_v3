/* ─────────────────────────────────────────────────────────────────
   trace.js — प्रक्रिया-प्रस्तुतिः तथा सूत्र-विवरण-पट्टिका।
   सर्वाः संज्ञाः देवनागर्याम्।
   ───────────────────────────────────────────────────────────────── */

let _currentTrace = [];

/* ── सहायक-कार्याणि ─────────────────────────────────────────── */

function escapeHtml(s) {
  if (s === null || s === undefined) return "";
  return String(s)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

/* सूत्रप्रकार-देवनागरी-नाम-सारणी */
const _SUTRA_TYPE_DEV = {
  "VIDHI"       : "विधिः",
  "PARIBHASHA"  : "परिभाषा",
  "SAMJNA"      : "संज्ञा",
  "ADHIKARA"    : "अधिकारः",
  "ANUVADA"     : "अनुवादः",
  "NIYAMA"      : "नियमः",
  "ATIDESA"     : "अतिदेशः",
  "PRATISHEDHA" : "प्रतिषेधः",
  "UTSARGA"     : "उत्सर्गः",
  "APAVADA"     : "अपवादः",
};

/* स्थिति-देवनागरी-नाम-सारणी */
const _STATUS_DEV = {
  "APPLIED"         : "प्रयुक्तम्",
  "APPLIED_VACUOUS" : "शून्यप्रयुक्तम्",
  "AUDIT"           : "निरीक्षितम्",
  "BLOCKED"         : "निवारितम्",
  "SKIPPED"         : "अतिक्रान्तम्",
};

function sutraTypeDev(t) { return _SUTRA_TYPE_DEV[t] || t || ""; }
function statusDev(s)    { return _STATUS_DEV[s]    || s || ""; }

/* ── वर्ण-प्रकार-चिह्नम् ───────────────────────────────────── */

function statusClass(step) {
  if (step._is_structural) return "structural";
  const s = step.status || "APPLIED";
  return s.toLowerCase();
}

function statusIcon(step) {
  if (step._is_structural) return "◈";
  switch (step.status) {
    case "APPLIED"         : return "✓";
    case "APPLIED_VACUOUS" : return "○";
    case "AUDIT"           : return "⟡";
    case "BLOCKED"         : return "✗";
    case "SKIPPED"         : return "·";
    default                : return "?";
  }
}

/* ── प्रक्रिया-प्रदर्शनम् ──────────────────────────────────── */

function renderTrace(trace) {
  _currentTrace = trace;
  applyTraceFilter();
  document.querySelectorAll("#trace-filter input").forEach(cb => {
    cb.onchange = applyTraceFilter;
  });
}

function _traceStepInFilter(step, active) {
  if (step._is_structural) return active.has("STRUCTURAL");
  const st = step.status || "APPLIED";
  if (st === "APPLIED_VACUOUS") return active.has("APPLIED");
  return active.has(st);
}

function applyTraceFilter() {
  const active = new Set(
    Array.from(document.querySelectorAll("#trace-filter input:checked"))
         .map(c => c.value)
  );
  const ol = document.getElementById("trace");
  ol.innerHTML = "";
  _currentTrace.forEach((step, idx) => {
    if (_traceStepInFilter(step, active)) ol.appendChild(renderStep(step, idx));
  });
}

function renderStep(step, idx) {
  const li = document.createElement("li");
  li.className = "trace-step " + statusClass(step);
  li.dataset.idx = idx;

  const sid     = step.sutra_id || "";
  const textDev = step._sutra_text_dev || "";
  const before  = escapeHtml(step.form_before || "");
  const after   = escapeHtml(step.form_after  || "");

  let extraLine = "";
  if (step.status === "BLOCKED" && step.gate_reason) {
    extraLine = `<div class="muted" style="font-size:11px;margin-left:24px;">
                   द्वारम्: ${escapeHtml(step.gate_reason)}
                 </div>`;
  } else if (step.status === "SKIPPED" && step.skip_reason) {
    extraLine = `<div class="muted" style="font-size:11px;margin-left:24px;">
                   ${escapeHtml(step.skip_reason)}
                 </div>`;
  }

  li.innerHTML = `
    <div class="ts-head">
      <span class="ts-icon">${statusIcon(step)}</span>
      <span class="ts-id">${escapeHtml(sid)}</span>
      <span class="ts-dev dev">${escapeHtml(textDev || step.why_dev || "")}</span>
      <span class="ts-form">${before}<span class="arrow">→</span>${after}</span>
    </div>
    ${extraLine}
  `;
  li.addEventListener("click", () => selectStep(idx));
  return li;
}

/* ── चरण-चयनम् ─────────────────────────────────────────────── */

function selectStep(idx) {
  document.querySelectorAll(".trace-step.selected")
          .forEach(el => el.classList.remove("selected"));
  const step = _currentTrace[idx];
  if (!step) return;
  const el = document.querySelector(`.trace-step[data-idx="${idx}"]`);
  if (el) el.classList.add("selected");
  renderSutraDetail(step);
}

/* ── सूत्र-विवरण-पट्टिका ─────────────────────────────────── */

function renderSutraDetail(step) {
  const panel = document.getElementById("sutra-detail");

  if (step._is_structural) {
    panel.innerHTML = `
      <h2>संरचना-चरणम्</h2>
      <div class="kv"><strong>संख्या</strong> <span class="mono">${escapeHtml(step.sutra_id)}</span></div>
      <div class="kv"><strong>प्रकारः</strong> ${escapeHtml(step.sutra_type || "")}</div>
      <div class="why dev">${escapeHtml(step.why_dev || "")}</div>
      <div class="muted" style="font-size:11px;margin-top:12px;">
        संरचना-चरणाः व्युत्पत्ति-सहायकाः सन्ति — पद-सन्धानम्, अवस्था-परिवर्तनम्,
        स्थिर-बिन्दु-अभिसरणम् — एते सूत्राणि न सन्ति।
      </div>
    `;
    return;
  }

  const anuv      = (step._anuvritti_from || []).join(", ");
  const isBlocked = step.status === "BLOCKED";
  const isSkipped = step.status === "SKIPPED";
  const typeLabel = sutraTypeDev(step.sutra_type);
  const stLabel   = statusDev(step.status);

  const stColor = isBlocked ? "var(--danger)"
                : isSkipped ? "var(--ink-faint)"
                : "var(--success)";

  /* उपदेश / प्रकृति / प्रत्यय / आगम / आदेश — प्रकार-चिह्नम् */
  const kindRaw   = (step.term_kind || "").toLowerCase();
  const kindLabel = {
    prakriti : "प्रकृतिः",
    pratyaya : "प्रत्ययः",
    agama    : "आगमः",
    upasarga : "उपसर्गः",
    nipata   : "निपातः",
    adesha   : "आदेशः",
  }[kindRaw] || "";

  panel.innerHTML = `
    <h2>
      <span class="sid">${escapeHtml(step.sutra_id)}</span>
      <span class="type-badge">${escapeHtml(typeLabel)}</span>
    </h2>

    <div class="text-dev dev">${escapeHtml(step._sutra_text_dev || "")}</div>
    <div class="padaccheda dev">${escapeHtml(step._padaccheda_dev || "")}</div>
    <div class="why dev">${escapeHtml(step.why_dev || "")}</div>

    <div class="kv"><strong>स्थितिः</strong>
      <span style="color:${stColor};">${escapeHtml(stLabel)}</span>
    </div>

    ${isBlocked ? `<div class="kv"><strong>द्वारम्</strong>
                    <span class="mono">${escapeHtml(step.gate_reason || "")}</span>
                   </div>` : ""}
    ${isSkipped ? `<div class="kv"><strong>कारणम्</strong>
                    <span class="mono">${escapeHtml(step.skip_reason || "")}</span>
                   </div>` : ""}

    ${kindLabel ? `<div class="kv"><strong>पद-प्रकारः</strong>
                     <span class="dev">${escapeHtml(kindLabel)}</span>
                   </div>` : ""}

    <div class="kv"><strong>पूर्वरूपम्</strong>
      <span class="mono">${escapeHtml(step.form_before || "")}</span></div>
    <div class="kv"><strong>उत्तररूपम्</strong>
      <span class="mono">${escapeHtml(step.form_after  || "")}</span></div>

    ${anuv ? `<div class="kv"><strong>अनुवृत्तिः</strong>
                <span class="mono">${escapeHtml(anuv)}</span></div>` : ""}

    <div style="margin-top:16px;">
      <a href="/sutra/${encodeURIComponent(step.sutra_id)}"
         class="muted" style="font-size:11px;">→ सूत्र-पृष्ठं पश्यतु</a>
    </div>
  `;
}
