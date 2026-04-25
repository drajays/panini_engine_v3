/* ─────────────────────────────────────────────────────────────────
   trace.js — render derivation trace + sūtra-detail sidebar.
   ───────────────────────────────────────────────────────────────── */

let _currentTrace = [];

function escapeHtml(s) {
  if (s === null || s === undefined) return "";
  return String(s)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

function statusClass(step) {
  if (step._is_structural) return "structural";
  const s = step.status || "APPLIED";
  return s.toLowerCase();
}

function statusIcon(step) {
  if (step._is_structural) return "◈";
  switch (step.status) {
    case "APPLIED" : return "✓";
    case "APPLIED_VACUOUS" : return "○";
    case "AUDIT"  : return "⟡";
    case "BLOCKED" : return "✗";
    case "SKIPPED" : return "·";
    default        : return "?";
  }
}

function renderTrace(trace) {
  _currentTrace = trace;
  applyTraceFilter();

  // Filter listeners.
  document.querySelectorAll("#trace-filter input").forEach(cb => {
    cb.onchange = applyTraceFilter;
  });
}

function _traceStepInFilter(step, active) {
  if (step._is_structural) {
    return active.has("STRUCTURAL");
  }
  const st = step.status || "APPLIED";
  if (st === "APPLIED_VACUOUS") {
    return active.has("APPLIED");
  }
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
    if (!_traceStepInFilter(step, active)) {
      return;
    }
    ol.appendChild(renderStep(step, idx));
  });
}

function renderStep(step, idx) {
  const li = document.createElement("li");
  li.className = "trace-step " + statusClass(step);
  li.dataset.idx = idx;

  const sid    = step.sutra_id || "";
  const textDev = step._sutra_text_dev || "";
  const before = escapeHtml(step.form_before || "");
  const after  = escapeHtml(step.form_after  || "");

  // For BLOCKED, show the gate reason. For SKIPPED, the skip_reason.
  let extraLine = "";
  if (step.status === "BLOCKED" && step.gate_reason) {
    extraLine = `<div class="muted" style="font-size:11px;margin-left:24px;">
                    gate: ${escapeHtml(step.gate_reason)}
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

function selectStep(idx) {
  document.querySelectorAll(".trace-step.selected")
          .forEach(el => el.classList.remove("selected"));
  const step = _currentTrace[idx];
  if (!step) return;

  const el = document.querySelector(`.trace-step[data-idx="${idx}"]`);
  if (el) el.classList.add("selected");

  renderSutraDetail(step);
}

function renderSutraDetail(step) {
  const panel = document.getElementById("sutra-detail");
  if (step._is_structural) {
    panel.innerHTML = `
      <h2>Structural Step</h2>
      <div class="kv"><strong>ID</strong> ${escapeHtml(step.sutra_id)}</div>
      <div class="kv"><strong>Type</strong> ${escapeHtml(step.sutra_type || "")}</div>
      <div class="why dev">${escapeHtml(step.why_dev || "")}</div>
      <div class="muted" style="font-size:11px;margin-top:12px;">
        Structural steps are bookkeeping events — pada-merge, phase
        transitions, fixed-point convergence — not sūtras.
      </div>
    `;
    return;
  }

  const anuv = (step._anuvritti_from || []).join(", ");
  const isBlocked = step.status === "BLOCKED";
  const isSkipped = step.status === "SKIPPED";

  panel.innerHTML = `
    <h2>
      <span class="sid">${escapeHtml(step.sutra_id)}</span>
      <span class="type-badge">${escapeHtml(step.sutra_type || "")}</span>
    </h2>
    <div class="text-dev dev">${escapeHtml(step._sutra_text_dev || "")}</div>
    <div class="padaccheda dev">${escapeHtml(step._padaccheda_dev || "")}</div>

    <div class="why dev">${escapeHtml(step.why_dev || "")}</div>

    <div class="kv"><strong>Status</strong>
      <span style="color:${isBlocked ? 'var(--danger)'
                         : isSkipped ? 'var(--ink-faint)'
                         : 'var(--success)'};">
        ${escapeHtml(step.status)}
      </span>
    </div>

    ${isBlocked ? `<div class="kv"><strong>Gate</strong>
                    <span class="mono">${escapeHtml(step.gate_reason || "")}</span>
                   </div>` : ""}
    ${isSkipped ? `<div class="kv"><strong>Reason</strong>
                    <span class="mono">${escapeHtml(step.skip_reason || "")}</span>
                   </div>` : ""}

    <div class="kv"><strong>Form before</strong>
      <span class="mono">${escapeHtml(step.form_before || "")}</span></div>
    <div class="kv"><strong>Form after</strong>
      <span class="mono">${escapeHtml(step.form_after  || "")}</span></div>

    ${anuv ? `<div class="kv"><strong>Anuvṛtti</strong> ${escapeHtml(anuv)}</div>` : ""}

    <div style="margin-top:16px;">
      <a href="/sutra/${encodeURIComponent(step.sutra_id)}"
         class="muted" style="font-size:11px;">→ open sūtra page</a>
    </div>
  `;
}
