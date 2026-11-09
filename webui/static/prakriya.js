/* prakriya.js — ONE derivation view for every page (display only; reads an enriched trace, never feeds the engine).
   Prakriya.mount(el, {trace, surface, title, letters}) draws controls, the letters of the word, the steps and a rule inspector.
   Depth:  Beginner   — only the milestones that build the word (affix added, sandhi, stem change; Aṣṭādhyāyī 3–8, form changes).
           Kaumudī    — every applied sūtra, it-saṃjñā 1.3.2–1.3.9 collapsed into one row, Laghukaumudī sūtras marked ★.
           Śāstrīya   — everything: checked, skipped, blocked (why), anuvṛtti, citations.
   Script: dev / varṇa-vibhāga / SLP1 / IAST.  Gloss: sa / hi / en.  Each step has a permalink (#s-N); print and JSON export. */
const Prakriya = (() => {
  const K = "panini-pk", esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
  const load = () => { try { return JSON.parse(localStorage.getItem(K)) || {}; } catch (e) { return {}; } };
  const pref = Object.assign({depth: "beginner", script: "dev", gloss: "hi"}, load());
  if (pref.mode) { pref.depth = pref.mode === "scholar" ? "shastriya" : "beginner"; delete pref.mode; }
  const save = () => { try { localStorage.setItem(K, JSON.stringify(pref)); } catch (e) {} };
  const TYPE_EN = {SAMJNA: "definition", PARIBHASHA: "interpretive rule", VIDHI: "operation", NIYAMA: "restriction", ATIDESHA: "extension",
    ADHIKARA: "heading", PRATISHEDHA: "prohibition", ANUVADA: "restatement", VIBHASHA: "optional rule", NIPATANA: "irregular form"};
  const STATUS = {APPLIED: ["प्रयुक्तम्", "applied"], APPLIED_VACUOUS: ["शून्यप्रयुक्तम्", "applied, no change"], AUDIT: ["निरीक्षितम्", "checked"],
    BLOCKED: ["निवारितम्", "blocked"], SKIPPED: ["अतिक्रान्तम्", "not applicable"], DEFINED: ["परिभाषितम्", "defined"], VACUOUS: ["शून्यम्", "no effect"],
    DECLINED: ["विकल्पेन न", "optional, declined"]};
  const fmt = (slp, dev) => pref.script === "slp1" ? slp : pref.script === "iast" ? Transliterate.fromSLP1(slp, "iast")
    : pref.script === "varna" ? Transliterate.slp1ToVarnas(slp) : (dev || Transliterate.fromSLP1(slp, "devanagari"));   // varna: vyañjana with halanta, svara apart
  let LK = null;                                                 // Laghukaumudī sūtra ids, fetched once
  const lk = () => { if (!LK) { LK = new Set(); fetch("/api/lk-sutras").then(r => r.json()).then(a => { LK = new Set(a); window.dispatchEvent(new Event("prakriya-change")); }).catch(() => {}); } return LK; };

  const changes = s => s.form_before !== s.form_after;
  const num = id => String(id).split(".").map(Number);
  const isIt = s => { const [a, p, n] = num(s.sutra_id); return a === 1 && p === 3 && n >= 2 && n <= 9; };
  const milestone = s => s.status === "APPLIED" && (changes(s) || s._is_structural) && (s._is_structural || num(s.sutra_id)[0] >= 3);
  const applied = s => /^APPLIED/.test(s.status);

  /* → [{s, i, group?}] rows for the chosen depth; i is the index in the full trace (stable permalink). */
  function rowsFor(t) {
    const all = t.map((s, i) => ({s, i}));
    if (pref.depth === "shastriya") return all;
    if (pref.depth === "beginner") return all.filter(({s}) => milestone(s));
    const out = []; let grp = null;
    for (const r of all) {
      if (!applied(r.s)) continue;
      if (isIt(r.s)) { if (!grp) { grp = {s: r.s, i: r.i, group: []}; out.push(grp); } grp.group.push(r.s); continue; }
      grp = null; out.push(r);
    }
    return out;
  }

  function gloss(s) {
    const a = fmt(s.form_before, s.form_before_dev), b = fmt(s.form_after, s.form_after_dev);
    if (pref.gloss === "sa") return s.why_now_dev || s.why_dev || "";
    if (pref.gloss === "hi") return s._hint_hi || s.why_now_dev || s.why_dev || "";
    const k = TYPE_EN[s.sutra_type] || "rule";
    return s._is_structural ? "" : changes(s) ? `Sūtra ${s.sutra_id} (${k}) rewrites ${a} as ${b}.` : `Sūtra ${s.sutra_id} (${k}) applies; the form stays ${a}.`;
  }

  function row({s, i, group}) {
    const st = STATUS[s.status] || [s.status, s.status], id = "s-" + (i + 1), deep = pref.depth === "shastriya";
    const star = lk().has(s.sutra_id) && pref.depth !== "beginner" ? `<span class="pk-lk" title="Laghukaumudī sūtra">★</span>` : "";
    if (group) return `<li class="pk-step pk-applied" id="${id}"><a class="pk-no" href="#${id}">${i + 1}</a><div class="pk-main">
      <div><b class="dev">इत्संज्ञा-लोपः</b> <span class="pk-tag">1.3.2–1.3.9</span> <span class="muted">${group.length} steps</span></div>
      <div class="pk-gloss">${esc(pref.gloss === "en" ? "markers (it) are named and removed from the affix and root" : "उपदेशे इत्-वर्णानां संज्ञा लोपश्च")}</div></div></li>`;
    const why = s.status === "BLOCKED" ? s.gate_reason : s.status === "SKIPPED" ? s.skip_reason : "";
    const sch = deep ? `
      <div class="pk-sch">${s._sutra_text_dev ? `<span class="dev">${esc(s._sutra_text_dev)}</span>` : ""}
        ${s._padaccheda_dev ? `<span class="muted dev"> · ${esc(s._padaccheda_dev)}</span>` : ""}
        ${(s._anuvritti_from || []).length ? `<div class="muted">अनुवृत्तिः ← ${s._anuvritti_from.map(x => `<a href="/sutra/${esc(x)}">${esc(x)}</a>`).join(", ")}</div>` : ""}
        ${why ? `<div class="pk-why">${esc(why)}</div>` : ""}
        ${(s._lsk || []).length ? `<div class="muted">LSK pp. ${esc([...new Set(s._lsk.map(x => x.page))].slice(0, 6).join(", "))}${s._lsk.length > 6 ? "…" : ""}</div>` : ""}</div>` : "";
    return `<li class="pk-step pk-${(s.status || "").toLowerCase()}" id="${id}">
      <a class="pk-no" href="#${id}" title="permalink to this step">${i + 1}</a>
      <div class="pk-main"><div><a class="pk-sid" href="/sutra/${esc(s.sutra_id)}">${esc(s.sutra_id)}</a>${star}
        <span class="pk-tag">${esc(pref.gloss === "en" ? st[1] : st[0])}</span>
        <span class="pk-form dev">${esc(fmt(s.form_before, s.form_before_dev))} → <b>${esc(fmt(s.form_after, s.form_after_dev))}</b></span></div>
        <div class="pk-gloss">${esc(gloss(s))}</div>${sch}</div></li>`;
  }

  /* "Why didn't rule X apply?" — what the trace says about one sūtra. */
  function inspect(t, sid) {
    sid = sid.trim(); if (!sid) return "";
    const hits = t.map((s, i) => ({s, i})).filter(({s}) => s.sutra_id === sid);
    const link = `<a href="/sutra/${esc(sid)}">${esc(sid)}</a>`;
    if (!hits.length) return `${link}: never offered in this derivation — its conditions were not even reached (or it is not implemented).`;
    return hits.map(({s, i}) => {
      const st = STATUS[s.status] || [s.status, s.status], why = s.gate_reason || s.skip_reason || s.why_now_dev || s.why_dev || "";
      const verdict = s.status === "BLOCKED" ? "blocked" : s.status === "SKIPPED" ? "checked, did not apply" : /^APPLIED/.test(s.status) ? "applied" : (STATUS[s.status] || [0, s.status])[1];
      return `${link} <a href="#s-${i + 1}">step ${i + 1}</a>: <b>${esc(verdict)}</b> (${esc(st[0])})${why ? ` — <span class="dev">${esc(why)}</span>` : ""}`;
    }).join("<br>");
  }

  function mount(el, d) {
    const t = d.trace || [], L = t[t.length - 1];
    if (!d.surface && L && L.form_after) d.surface = {slp1: L.form_after, dev: L.form_after_dev};
    const sel = (id, opts, v) => `<select id="${id}">${opts.map(([k, l]) => `<option value="${k}"${k === v ? " selected" : ""}>${l}</option>`).join("")}</select>`;
    el.innerHTML = `<div class="pk-bar no-print">
      <label>गहनता ${sel("pk-depth", [["beginner", "आरम्भिकः · Beginner"], ["kaumudi", "कौमुदी · Kaumudī"], ["shastriya", "शास्त्रीयः · Śāstrīya"]], pref.depth)}</label>
      <label>लिपिः ${sel("pk-script", [["dev", "देवनागरी"], ["varna", "देवनागरी — वर्ण-विभागः"], ["slp1", "SLP1"], ["iast", "IAST"]], pref.script)}</label>
      <label>व्याख्या ${sel("pk-gloss", [["hi", "हिन्दी"], ["en", "English"], ["sa", "संस्कृतम्"]], pref.gloss)}</label>
      <button type="button" id="pk-print">Print</button><button type="button" id="pk-json">Export JSON</button></div>
      <h2 class="pk-result dev"></h2><div class="pk-letters"></div><div class="pk-letter-info muted" aria-live="polite"></div>
      <p class="muted pk-count"></p><ol class="pk-list"></ol>
      <div class="pk-inspect no-print"><label>कस्मात् सूत्रं न प्रयुक्तम्? · Why didn't rule apply? <input class="pk-sid-in" placeholder="e.g. 7.1.9" size="10"></label>
        <div class="pk-inspect-out" aria-live="polite"></div></div>`;
    const q = s => el.querySelector(s);
    const letters = () => (d.letters || []).map((l, n) => `<button type="button" class="pk-letter${l.origin.length ? "" : " pk-given"}" data-n="${n}"
      title="${l.origin.length ? "created by " + esc(l.origin.join(", ")) : "given (upadeśa)"}">${esc(fmt(l.slp1, ""))}</button>`).join("");
    const paint = () => {
      const rows = rowsFor(t);
      q(".pk-list").innerHTML = rows.map(row).join("") || "<li class='muted'>—</li>";
      q(".pk-count").textContent = pref.depth === "beginner" ? `${rows.length} milestones (of ${t.length} rule checks). Choose Kaumudī or Śāstrīya for more.`
        : pref.depth === "kaumudi" ? `${rows.length} rows — every applied sūtra; ★ = in the Laghukaumudī list.` : `${t.length} rows: ${t.filter(applied).length} applied.`;
      q(".pk-result").innerHTML = `${esc(d.title || "")} ${d.surface ? `→ <b>${esc(fmt(d.surface.slp1, d.surface.dev))}</b>` : ""}`;
      q(".pk-letters").innerHTML = letters();
      q(".pk-inspect").hidden = pref.depth === "beginner";
      if (location.hash.startsWith("#s-")) { const n = document.getElementById(location.hash.slice(1)); if (n) { n.classList.add("pk-hit"); n.scrollIntoView({block: "center"}); } }
    };
    [["pk-depth", "depth"], ["pk-script", "script"], ["pk-gloss", "gloss"]].forEach(([id, k]) =>
      q("#" + id).addEventListener("change", e => { pref[k] = e.target.value; save(); window.dispatchEvent(new Event("prakriya-change")); }));
    q(".pk-letters").addEventListener("click", e => {
      const b = e.target.closest(".pk-letter"); if (!b) return;
      const l = d.letters[+b.dataset.n];
      q(".pk-letter-info").innerHTML = l.origin.length ? `${esc(fmt(l.slp1, ""))} ← ${l.origin.map(o => {
        const i = t.findIndex(s => s.sutra_id === o && applied(s));
        return `<a href="/sutra/${esc(o)}">${esc(o)}</a>${i >= 0 ? ` (<a href="#s-${i + 1}">step ${i + 1}</a>)` : ""}`; }).join(", ")}` : `${esc(fmt(l.slp1, ""))} — part of the given upadeśa, not created by a rule.`;
    });
    q(".pk-sid-in").addEventListener("input", e => { q(".pk-inspect-out").innerHTML = inspect(t, e.target.value); });
    q("#pk-print").onclick = () => window.print();
    q("#pk-json").onclick = () => {
      const a = document.createElement("a");
      a.href = URL.createObjectURL(new Blob([JSON.stringify(d, null, 1)], {type: "application/json"}));
      a.download = "prakriya.json"; a.click();
    };
    const repaint = () => { if (!el.isConnected) window.removeEventListener("prakriya-change", repaint); else paint(); };
    window.addEventListener("prakriya-change", repaint);
    paint();
  }
  return {mount, pref, fmt, rowsFor, inspect};
})();
