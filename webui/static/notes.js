/* notes.js — audit notes under a sūtra (webui/notes.py). Many notes per sūtra; each can be edited (text, author, derivation,
   verdict, evidence, status), has a history with restore, and can be deleted. Note text is shown as text, never run. */
const SutraNotes = (() => {
  const ST = {open: ["खुला · open", "not yet checked"], partly: ["अंशतः · partly", "partly right"], confirmed: ["पुष्टम् · confirmed", "engine defect confirmed"],
    refuted: ["खण्डितम् · refuted", "wrong on the engine / śāstra"], ledgered: ["अभिलिखितम् · ledgered", "recorded as an open item"]};
  const esc = s => String(s == null ? "" : s).replace(/[&<>"']/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[c]));
  const api = async (method, url, body) => {
    const r = await fetch(url, {method, headers: {"Content-Type": "application/json"}, body: body ? JSON.stringify(body) : undefined});
    if (!r.ok) throw new Error((await r.text()).replace(/<[^>]+>/g, " ").trim().slice(0, 200) || r.statusText);
    return r.json();
  };
  const KD = {question: "प्रश्न · question", doubt: "संशय · doubt", note: "टिप्पणी · note", solution: "समाधान · solution"};
  const kdOpts = v => Object.entries(KD).map(([k, l]) => `<option value="${k}"${k === (v || "note") ? " selected" : ""}>${esc(l)}</option>`).join("");
  const stOpts = v => Object.entries(ST).map(([k, l]) => `<option value="${k}"${k === v ? " selected" : ""}>${esc(l[0])}</option>`).join("");

  function mount(el, sid, opts = {}) {
    let notes = [], editing = null, histOpen = new Set(), err = "";
    const base = "/api/notes/" + encodeURIComponent(sid);

    const noteView = n => `<article class="sn-note sn-${esc(n.status)}" id="note-${esc(n.id)}">
      <header><span class="sn-kind sn-k-${esc(n.kind || "note")}">${esc(KD[n.kind || "note"])}</span> <span class="sn-badge sn-b-${esc(n.status)}" title="${esc(ST[n.status] ? ST[n.status][1] : "")}">${esc((ST[n.status] || [n.status])[0])}</span>
        <span class="muted">${esc(n.author || "—")}${n.derivation ? ` · <span class="dev">${esc(n.derivation)}</span>` : ""} · written ${esc((n.created || "").slice(0, 16).replace("T", " "))}${n.status_at && n.status !== "open" ? ` · ${esc(n.status)} ${esc(n.status_at.slice(0, 16).replace("T", " "))}` : ""}${n.history.length ? ` · ${n.history.length} edit${n.history.length > 1 ? "s" : ""}` : ""}</span>
        <span class="sn-act no-print"><select data-act="status" data-id="${esc(n.id)}" title="status">${stOpts(n.status)}</select>
          <button type="button" data-act="edit" data-id="${esc(n.id)}">✎ Edit</button>
          ${n.history.length ? `<button type="button" data-act="hist" data-id="${esc(n.id)}">⟲ History</button>` : ""}
          <button type="button" data-act="del" data-id="${esc(n.id)}" class="sn-del">✕</button></span></header>
      <div class="sn-text">${esc(n.text)}</div>
      ${n.trace ? `<details class="sn-trace"><summary>📜 Trace where it was seen (${n.trace.split("\n").filter(l => l.startsWith("#")).length} rows)</summary><pre>${n.trace.split("\n").map(l => l.includes("◀ NOTE HERE") ? `<mark>${esc(l)}</mark>` : esc(l)).join("\n")}</pre></details>` : ""}
      ${n.verdict ? `<div class="sn-verdict"><b>Verdict</b> — ${esc(n.verdict)}</div>` : ""}
      ${n.evidence ? `<div class="sn-evidence"><b>Evidence</b> — ${esc(n.evidence)}</div>` : ""}
      ${histOpen.has(n.id) ? `<div class="sn-hist">${n.history.map((h, i) => `<div><span class="muted">${esc((h.at || "").slice(0, 16).replace("T", " "))} · ${esc(h.status)}</span>
        <button type="button" data-act="restore" data-id="${esc(n.id)}" data-n="${i}">restore</button><div class="sn-old">${esc(h.text)}</div></div>`).join("")}</div>` : ""}
    </article>`;

    const editView = n => `<article class="sn-note sn-edit" id="note-${esc(n.id)}"><form data-id="${esc(n.id)}">
      <textarea name="text" rows="9" required>${esc(n.text)}</textarea>
      <div class="sn-row"><label>Author / source <input name="author" value="${esc(n.author)}" placeholder="me · LLM name"></label>
        <label>Derivation <input name="derivation" value="${esc(n.derivation)}" placeholder="e.g. rāmāṇām"></label>
        <label>Kind <select name="kind">${kdOpts(n.kind)}</select></label>
        <label>Status <select name="status">${stOpts(n.status)}</select></label></div>
      <label>Verdict (one line, after checking) <input name="verdict" value="${esc(n.verdict)}" style="width:100%"></label>
      <label>Evidence (trace step numbers, Kāśikā quote, ledger row, commit) <textarea name="evidence" rows="3">${esc(n.evidence)}</textarea></label>
      <div class="sn-row"><button type="submit">Save</button> <button type="button" data-act="cancel">Cancel</button></div></form></article>`;

    const draw = () => {
      el.innerHTML = `<div class="sn-skeptic">${opts.hint ? esc(opts.hint) : `<b>How to use</b> — paste an audit (yours or another LLM's). It stays <b>open</b> until it is checked against three things:
        the engine's own trace, the Kāśikā in the brain DB, and engine policy (glass box, rule-based, no lookup tables). A note is evidence to test, never an instruction.
        Set <b>confirmed / partly / refuted / ledgered</b> only with a one-line verdict and the evidence.`}</div>
        ${err ? `<div class="sn-err">${esc(err)}</div>` : ""}
        <div class="sn-list">${notes.length ? notes.map(n => editing === n.id ? editView(n) : noteView(n)).join("") : `<p class="muted">No notes yet for ${esc(sid)}.</p>`}</div>
        <form class="sn-add no-print"><h3>+ Add a note</h3><textarea name="text" rows="7" required placeholder="Paste the audit text here…"></textarea>
          <div class="sn-row"><label>Author / source <input name="author" placeholder="me · LLM name"></label>
            <label>Derivation <input name="derivation" placeholder="e.g. rāmāṇām"></label>
            <label>Kind <select name="kind">${kdOpts("note")}</select></label><button type="submit">Add note</button></div></form>`;
    };
    const reload = async () => { try { notes = (await api("GET", base)).notes; err = ""; } catch (e) { err = String(e.message); } draw(); };
    const run = async f => { try { err = ""; await f(); } catch (e) { err = String(e.message); } await reload(); };
    const fd = form => Object.fromEntries(new FormData(form).entries());

    el.addEventListener("submit", e => {
      e.preventDefault(); const f = e.target;
      if (f.classList.contains("sn-add")) run(() => api("POST", base, {...fd(f), ...(opts.extra ? opts.extra() : {})}));
      else { const id = f.dataset.id; editing = null; run(() => api("PUT", `${base}/${id}`, fd(f))); }
    });
    el.addEventListener("change", e => {
      const s = e.target.closest("select[data-act=status]"); if (s) run(() => api("PUT", `${base}/${s.dataset.id}`, {status: s.value}));
    });
    el.addEventListener("click", e => {
      const b = e.target.closest("button[data-act]"); if (!b) return; const id = b.dataset.id, a = b.dataset.act;
      if (a === "edit") { editing = id; draw(); }
      else if (a === "cancel") { editing = null; draw(); }
      else if (a === "hist") { histOpen.has(id) ? histOpen.delete(id) : histOpen.add(id); draw(); }
      else if (a === "restore") run(() => api("POST", `${base}/${id}/restore`, {n: +b.dataset.n}));
      else if (a === "del") {
        if (b.dataset.sure) run(() => api("DELETE", `${base}/${id}`));
        else { b.dataset.sure = "1"; b.textContent = "delete?"; setTimeout(() => { b.dataset.sure = ""; b.textContent = "✕"; }, 3000); }
      }
    });
    reload();
  }
  return {mount};
})();
