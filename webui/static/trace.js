/* trace.js — thin shim: every page that calls renderTrace(trace) now gets the shared derivation view (prakriya.js). */
function renderTrace(trace, container, title) {
  let host = container || document.getElementById("trace");
  if (!host) return;
  if (host.tagName === "OL") { const d = document.createElement("div"); d.id = host.id; host.replaceWith(d); host = d; }
  const last = (trace || []).slice(-1)[0] || {};
  Prakriya.mount(host, {trace: trace || [], title: title || "", surface: last.form_after ? {slp1: last.form_after, dev: last.form_after_dev} : null});
}

/* pages still call this for their own result headers */
function escapeHtml(s) { return String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
