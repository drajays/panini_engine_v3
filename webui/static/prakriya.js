/* prakriya.js — ONE derivation view for every page (display only; reads an enriched trace, never feeds the engine).
   Prakriya.mount(el, {trace, surface, title}) draws controls + steps.
   Student: only steps that change the word, each with a plain gloss.  Scholar: every row — checked, blocked (why), anuvṛtti, citations.
   Script: dev / slp1 / iast.  Gloss: sa / hi / en.  Each step has a permalink (#s-N) and the whole view prints / exports. */
const Prakriya = (() => {
  const K = "panini-pk", esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
  const load = () => { try { return JSON.parse(localStorage.getItem(K)) || {}; } catch (e) { return {}; } };
  const pref = Object.assign({mode: "student", script: "dev", gloss: "hi"}, load());
  const save = () => { try { localStorage.setItem(K, JSON.stringify(pref)); } catch (e) {} };
  const TYPE_EN = {SAMJNA: "definition", PARIBHASHA: "interpretive rule", VIDHI: "operation", NIYAMA: "restriction", ATIDESHA: "extension",
    ADHIKARA: "heading", PRATISHEDHA: "prohibition", ANUVADA: "restatement", VIBHASHA: "optional rule", NIPATANA: "irregular form"};
  const STATUS = {APPLIED: ["प्रयुक्तम्", "applied"], APPLIED_VACUOUS: ["शून्यप्रयुक्तम्", "applied, no change"], AUDIT: ["निरीक्षितम्", "checked"],
    BLOCKED: ["निवारितम्", "blocked"], SKIPPED: ["अतिक्रान्तम्", "not applicable"], DEFINED: ["परिभाषितम्", "defined"], VACUOUS: ["शून्यम्", "no effect"]};
  const fmt = (slp, dev) => pref.script === "slp1" ? slp : pref.script === "iast" ? Transliterate.fromSLP1(slp, "iast") : (dev || Transliterate.fromSLP1(slp, "devanagari"));
  const changes = s => s.form_before !== s.form_after;
  const real = s => /^APPLIED/.test(s.status) && !(s._is_structural && !changes(s));
  const visible = (t) => pref.mode === "scholar" ? t : t.filter(s => /^APPLIED$/.test(s.status) && (changes(s) || s._is_structural));

  function gloss(s) {
    const a = fmt(s.form_before, s.form_before_dev), b = fmt(s.form_after, s.form_after_dev);
    if (pref.gloss === "sa") return s.why_now_dev || s.why_dev || "";
    if (pref.gloss === "hi") return s._hint_hi || s.why_now_dev || s.why_dev || "";
    const k = TYPE_EN[s.sutra_type] || "rule";
    return s._is_structural ? "" : changes(s) ? `Sūtra ${s.sutra_id} (${k}) rewrites ${a} as ${b}.` : `Sūtra ${s.sutra_id} (${k}) applies; the form stays ${a}.`;
  }

  function row(s, i) {
    const st = STATUS[s.status] || [s.status, s.status], id = "s-" + (i + 1);
    const why = s.status === "BLOCKED" ? s.gate_reason : s.status === "SKIPPED" ? s.skip_reason : "";
    const sch = pref.mode === "scholar" ? `
      <div class="pk-sch">${s._sutra_text_dev ? `<span class="dev">${esc(s._sutra_text_dev)}</span>` : ""}
        ${s._padaccheda_dev ? `<span class="muted dev"> · ${esc(s._padaccheda_dev)}</span>` : ""}
        ${(s._anuvritti_from || []).length ? `<div class="muted">अनुवृत्तिः ← ${s._anuvritti_from.map(x => `<a href="/sutra/${esc(x)}">${esc(x)}</a>`).join(", ")}</div>` : ""}
        ${why ? `<div class="pk-why">${esc(why)}</div>` : ""}
        ${(s._lsk || []).length ? `<div class="muted">LSK pp. ${esc([...new Set(s._lsk.map(x => x.page))].slice(0, 6).join(", "))}${s._lsk.length > 6 ? "…" : ""}</div>` : ""}</div>` : "";
    return `<li class="pk-step pk-${(s.status || "").toLowerCase()}" id="${id}">
      <a class="pk-no" href="#${id}" title="permalink to this step">${i + 1}</a>
      <div class="pk-main"><div><a class="pk-sid" href="/sutra/${esc(s.sutra_id)}">${esc(s.sutra_id)}</a>
        <span class="pk-tag">${esc(pref.gloss === "en" ? st[1] : st[0])}</span>
        <span class="pk-form dev">${esc(fmt(s.form_before, s.form_before_dev))} → <b>${esc(fmt(s.form_after, s.form_after_dev))}</b></span></div>
        <div class="pk-gloss">${esc(gloss(s))}</div>${sch}</div></li>`;
  }

  function mount(el, d) {
    const t = d.trace || [];
    const sel = (id, opts, v) => `<select id="${id}">${opts.map(([k, l]) => `<option value="${k}"${k === v ? " selected" : ""}>${l}</option>`).join("")}</select>`;
    el.innerHTML = `<div class="pk-bar no-print">
      <label>दर्शनम् ${sel("pk-mode", [["student", "छात्रः · Student"], ["scholar", "विद्वान् · Scholar"]], pref.mode)}</label>
      <label>लिपिः ${sel("pk-script", [["dev", "देवनागरी"], ["slp1", "SLP1"], ["iast", "IAST"]], pref.script)}</label>
      <label>व्याख्या ${sel("pk-gloss", [["hi", "हिन्दी"], ["en", "English"], ["sa", "संस्कृतम्"]], pref.gloss)}</label>
      <button type="button" id="pk-print">Print</button><button type="button" id="pk-json">Export JSON</button></div>
      <h2 class="pk-result dev">${esc(d.title || "")} ${d.surface ? `→ <b>${esc(fmt(d.surface.slp1, d.surface.dev))}</b>` : ""}</h2>
      <p class="muted pk-count"></p><ol class="pk-list"></ol>`;
    const paint = () => {
      const v = visible(t), all = t.map((s, i) => [s, i]).filter(([s]) => v.includes(s));
      el.querySelector(".pk-list").innerHTML = all.map(([s, i]) => row(s, i)).join("") || "<li class='muted'>—</li>";
      el.querySelector(".pk-count").textContent = pref.mode === "student"
        ? `${v.length} steps change the word (of ${t.length} rule checks). Switch to Scholar to see every check and each block.`
        : `${t.length} rows: ${t.filter(real).length} applied.`;
      el.querySelector(".pk-result").innerHTML = `${esc(d.title || "")} ${d.surface ? `→ <b>${esc(fmt(d.surface.slp1, d.surface.dev))}</b>` : ""}`;
      if (location.hash.startsWith("#s-")) { const n = document.getElementById(location.hash.slice(1)); if (n) { n.classList.add("pk-hit"); n.scrollIntoView({block: "center"}); } }
    };
    [["pk-mode", "mode"], ["pk-script", "script"], ["pk-gloss", "gloss"]].forEach(([id, k]) =>
      el.querySelector("#" + id).addEventListener("change", e => { pref[k] = e.target.value; save(); paint(); }));
    el.querySelector("#pk-print").onclick = () => window.print();
    el.querySelector("#pk-json").onclick = () => {
      const a = document.createElement("a");
      a.href = URL.createObjectURL(new Blob([JSON.stringify(d, null, 1)], {type: "application/json"}));
      a.download = "prakriya.json"; a.click();
    };
    paint();
  }
  return {mount, pref};
})();
