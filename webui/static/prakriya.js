/* prakriya.js — ONE derivation view for every page (display only; reads an enriched trace, never feeds the engine).
   Prakriya.mount(el, {trace, surface, title, letters}) draws controls, the letters of the word, the steps and a rule inspector.
   Depth:  Beginner   — only the milestones that build the word (affix added, sandhi, stem change; Aṣṭādhyāyī 3–8, form changes).
           Kaumudī    — every applied sūtra, it-saṃjñā 1.3.2–1.3.9 collapsed into one row, Laghukaumudī sūtras marked ★.
           Śāstrīya   — everything: checked, skipped, blocked (why), anuvṛtti, citations.
   Script: dev / varṇa-vibhāga / SLP1 / IAST.  Gloss: sa / hi / en.  Each step has a permalink (#s-N); print and JSON export. */
const Prakriya = (() => {
  const K = "panini-pk", esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
  const load = () => { try { return JSON.parse(localStorage.getItem(K)) || {}; } catch (e) { return {}; } };
  const pref = Object.assign({depth: "beginner", script: "dev", gloss: "hi", split: false}, load());
  if (pref.mode) { pref.depth = pref.mode === "scholar" ? "shastriya" : "beginner"; delete pref.mode; }
  const save = () => { try { localStorage.setItem(K, JSON.stringify(pref)); } catch (e) {} };
  const TYPE_EN = {SAMJNA: "definition", PARIBHASHA: "interpretive rule", VIDHI: "operation", NIYAMA: "restriction", ATIDESHA: "extension",
    ADHIKARA: "heading", PRATISHEDHA: "prohibition", ANUVADA: "restatement", VIBHASHA: "optional rule", NIPATANA: "irregular form"};
  const STATUS = {APPLIED: ["प्रयुक्तम्", "applied"], APPLIED_VACUOUS: ["शून्यप्रयुक्तम्", "applied, no change"], AUDIT: ["निरीक्षितम्", "checked"],
    BLOCKED: ["निवारितम्", "blocked"], SKIPPED: ["अतिक्रान्तम्", "not applicable"], DEFINED: ["परिभाषितम्", "defined"], VACUOUS: ["शून्यम्", "no effect"],
    DECLINED: ["विकल्पेन न", "optional, declined"]};
  /* UI-only teaching aids are marked ◆ everywhere (screen, Copy panel, Copy to LLM). Rows of the engine trace (sūtra id + status) are never marked. */
  const PED = (en, note) => `<span class="pk-ped" title="${esc(note || (en ? "Teaching aid added by this page — not a sūtra step of the Aṣṭādhyāyī" : "शिक्षण-सहायक — इस पृष्ठ द्वारा जोड़ा गया; अष्टाध्यायी-क्रम का अंग नहीं"))}">◆ ${en ? "teaching aid" : "शिक्षण-सहायक"}</span>`;
  const isStruct = s => !!s._is_structural || String(s.sutra_id || "").startsWith("__");
  const pedGloss = s => !isStruct(s) && (pref.gloss === "en" ? true : pref.gloss === "hi" && !!s._hint_hi);   // en: generated template; hi: hint text — neither is the engine's own why
  const devOf = slp => String(slp || "").split("~").map((c, k, a) => (c ? Transliterate.fromSLP1(c, "devanagari") : "") + (k < a.length - 1 ? "ँ" : "")).join("");  // anunāsika ~ → ँ
  const fmt = (slp, dev) => pref.script === "slp1" ? slp : pref.script === "iast" ? Transliterate.fromSLP1(slp, "iast")
    : pref.script === "varna" ? Transliterate.slp1ToVarnas(slp) : (dev || devOf(slp));   // varna: vyañjana with halanta, svara apart
  let LK = null;                                                 // Laghukaumudī sūtra ids, fetched once
  const lk = () => { if (!LK) { LK = new Set(); fetch("/api/lk-sutras").then(r => r.json()).then(a => { LK = new Set(a); window.dispatchEvent(new Event("prakriya-change")); }).catch(() => {}); } return LK; };

  const changes = s => s.form_before !== s.form_after;
  const num = id => String(id).split(".").map(Number);
  const isIt = s => { const [a, p, n] = num(s.sutra_id); return a === 1 && p === 3 && n >= 2 && n <= 9; };
  const milestone = s => s.status === "APPLIED" && (changes(s) || s._is_structural) && (s._is_structural || num(s.sutra_id)[0] >= 3);
  const applied = s => /^APPLIED/.test(s.status);

  /* ── parts (aṅga, pratyaya, āgama, abhyāsa …) and varṇas: who is the target, what replaced it ──────────────
     Each applied step carries ``parts`` = [[text, role, upadeśa], …] (engine/trace.term_parts). Colours mark the role;
     a click on a form toggles संहितम् (merged) ↔ वर्णविभागः (र् आ म् अ) with the स्थानी struck and the new varṇas boxed. */
  const ROLE = {dhatu: ["धातुः", "root"], prakriti: ["प्रकृतिः", "stem"], pratipadika: ["प्रातिपदिकम्", "nominal stem"],
    abhyasa: ["अभ्यासः", "reduplicate"], vikarana: ["विकरणम्", "class affix"], agama: ["आगमः", "augment"],
    pratyaya: ["प्रत्ययः", "affix"], sup: ["सुप्", "case ending"], tin: ["तिङ्", "verb ending"], krt: ["कृत्", "kṛt affix"],
    taddhita: ["तद्धितः", "taddhita affix"], stri: ["स्त्रीप्रत्ययः", "feminine affix"], upasarga: ["उपसर्गः", "preverb"],
    pada: ["पदम्", "word"], other: ["अंशः", "part"]};
  const roleOf = r => ROLE[r] ? r : "other";
  const SAMJNA = {"1.2.45": ["प्रातिपदिकम्", "stem"], "1.2.46": ["प्रातिपदिकम्", "stem"], "3.1.32": ["धातुः", "all"],
    "1.4.13": ["अङ्गम्", "pre"], "1.4.14": ["पदम्", "all"], "1.4.17": ["पदम्", "pre"], "1.4.18": ["भम्", "pre"],
    "3.4.113": ["सार्वधातुकम्", "last"], "3.4.114": ["आर्धधातुकम्", "sesa"], "3.4.115": ["आर्धधातुकम्", "sesa"], "3.4.116": ["आर्धधातुकम्", "sesa"], "1.1.73": ["वृद्धम्", "all"],
    "1.4.110": ["अवसानम्", "all"], "1.4.59": ["उपसर्गः", "first"], "1.4.99": ["परस्मैपदम्", "last"], "1.4.100": ["आत्मनेपदम्", "last"],
    "1.4.101": ["पुरुषः", "last"], "1.4.103": ["वचनम्", "last"], "1.4.104": ["विभक्तिः", "last"], "3.1.1": ["प्रत्ययः", "last"],
    "1.1.20": ["घु", "all"], "1.1.27": ["सर्वनाम", "stem"], "1.4.7": ["घि", "stem"], "1.4.3": ["नदी", "stem"], "1.1.42": ["सर्वनामस्थानम्", "last"]};
  const parseParts = p => { if (Array.isArray(p)) return p; try { return JSON.parse(String(p).replace(/'/g, '"')); } catch (e) { return null; } };
  const VTOK = /[kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh]|[aAiIuUfFxXeEoO][~]?|[MH']|./g;
  const vtoks = slp => (String(slp || "").replace(/[\s\^\\\/]/g, "").match(VTOK) || []);
  const vfmt = tok => pref.script === "slp1" ? tok : pref.script === "iast" ? Transliterate.fromSLP1(tok, "iast") : Transliterate.slp1ToVarnas(tok);
  /* longest common subsequence → ops over two varṇa lists */
  function diff(a, b) {
    const n = a.length, m = b.length, L = Array.from({length: n + 1}, () => new Int16Array(m + 1));
    for (let i = n - 1; i >= 0; i--) for (let j = m - 1; j >= 0; j--) L[i][j] = a[i] === b[j] ? L[i + 1][j + 1] + 1 : Math.max(L[i + 1][j], L[i][j + 1]);
    const ops = []; let i = 0, j = 0;
    while (i < n || j < m) {          // among equally long alignments, an insertion goes first (abhyāsa, āgama, upasarga precede)
      if (j < m && L[i][j + 1] === L[i][j]) { ops.push(["+", -1, j++]); }
      else if (i < n && j < m && a[i] === b[j]) { ops.push(["=", i++, j++]); }
      else if (i < n && (j >= m || L[i + 1][j] === L[i][j])) { ops.push(["-", i++, -1]); }
      else { ops.push(["+", -1, j++]); }
    }
    return ops;
  }
  /* varṇa index → part index, for a parts list whose texts concatenate to the form */
  const roleMap = (parts, toks) => { const out = []; if (!parts) return out;
    parts.forEach(([txt], k) => { vtoks(txt).forEach(() => out.push(k)); });
    return out.length === toks.length ? out : []; };
  const joined = parts => parts ? parts.map(p => p[0]).join("") : null;
  const partTitle = p => `${(ROLE[roleOf(p[1])] || ROLE.other)[pref.gloss === "en" ? 1 : 0]}${p[2] ? ` · उपदेशः ${Transliterate.fromSLP1(p[2], "devanagari")}` : ""}`;

  function mergedHtml(form, dev, parts, changed) {
    if (!parts || joined(parts) !== String(form).replace(/\s/g, "")) return `<span>${esc(fmt(form, dev))}</span>`;
    return parts.map((p, k) => `<span class="pk-part pk-r-${roleOf(p[1])}${changed && changed.has(k) ? " pk-chg" : ""}" title="${esc(partTitle(p))}">${esc(fmt(p[0], ""))}</span>`).join("");
  }
  /* the two forms of one step, merged or split, with the change marked */
  function formHtml(s, pb, pa, split) {
    const a = vtoks(s.form_before), b = vtoks(s.form_after), ops = diff(a, b);
    const ra = roleMap(pb, a), rb = roleMap(pa, b);
    const del = new Set(ops.filter(o => o[0] === "-").map(o => o[1])), ins = new Set(ops.filter(o => o[0] === "+").map(o => o[2]));
    if (!split) {
      const chA = new Set([...del].map(i => ra[i]).filter(x => x !== undefined)), chB = new Set([...ins].map(j => rb[j]).filter(x => x !== undefined));
      return `${mergedHtml(s.form_before, s.form_before_dev, pb, chA)} <span class="pk-arrow">→</span> <b>${mergedHtml(s.form_after, s.form_after_dev, pa, chB)}</b>`;
    }
    const tok = (t, r, parts, cls) => { const p = parts && r !== undefined ? parts[r] : null;
      return `<span class="pk-v pk-r-${p ? roleOf(p[1]) : "other"}${cls}"${p ? ` title="${esc(partTitle(p))}"` : ""}>${esc(vfmt(t))}</span>`; };
    const left = a.map((t, i) => tok(t, ra[i], pb, del.has(i) ? " pk-del" : "")).join("");
    const right = b.map((t, j) => tok(t, rb[j], pa, ins.has(j) ? " pk-ins" : "")).join("");
    return `<span class="pk-vrow">${left}</span> <span class="pk-arrow">→</span> <span class="pk-vrow">${right}</span>${changeNote(a, b, ops, j => pa && rb[j] !== undefined ? roleOf(pa[rb[j]][1]) : "other")}`;
  }
  /* स्थानी → आदेशः / आगमः / लोपः, read off the varṇa diff (runs of − and + between unchanged varṇas) */
  const INS = {abhyasa: "द्वित्वम् (अभ्यासः)", agama: "आगमः", sup: "प्रत्ययः (सुप्)", tin: "प्रत्ययः (तिङ्)", pratyaya: "प्रत्ययः",
    krt: "प्रत्ययः (कृत्)", taddhita: "प्रत्ययः (तद्धितः)", vikarana: "विकरणम्", stri: "स्त्रीप्रत्ययः", upasarga: "उपसर्गः"};
  function changeNote(a, b, ops, roleAt = () => "other") {
    const runs = []; let cur = null;
    for (const [op, i, j] of ops) {
      if (op === "=") { if (cur) { runs.push(cur); cur = null; } continue; }
      cur = cur || {del: [], ins: [], role: null};
      if (op === "-") cur.del.push(a[i]); else { cur.ins.push(b[j]); cur.role = cur.role || roleAt(j); }
    }
    if (cur) runs.push(cur);
    if (!runs.length) return "";
    const v = xs => xs.map(vfmt).join(" ");
    return `<span class="pk-note">${runs.slice(0, 3).map(r => r.del.length && r.ins.length ? `<span class="pk-del">${esc(v(r.del))}</span> ⇒ <span class="pk-ins">${esc(v(r.ins))}</span> <i>स्थानी → आदेशः</i>`
      : r.ins.length ? `+ <span class="pk-ins">${esc(v(r.ins))}</span> <i>${INS[r.role] || "योजनम्"}</i>` : `<span class="pk-del">${esc(v(r.del))}</span> ⇒ ∅ <i>लोपः</i>`).join(" · ")}</span>`;
  }
  /* 1.3.9's own record: "तिप् — प् → पित् (१.३.३)" → chips upadeśa | letter → class (sūtra) */
  const itParse = s => {
    const m = String(s.why_now_dev || "").match(/\):\s*(.+?)\s+—\s+(.+?)।/);
    if (!m) return null;
    const items = m[2].split(/,\s*/).map(x => { const k = x.match(/^(.+?)\s*→\s*(.+?)\s*\((.+?)\)$/); return k ? {letter: k[1], name: k[2], sutra: k[3]} : {letter: x, name: "", sutra: ""}; });
    return {upadesha: m[1], items};
  };
  function itChips(s) {
    const r = itParse(s); if (!r) return "";
    return `<div class="pk-itrec"><span class="pk-sj">उपदेशः <b>${esc(r.upadesha)}</b></span>${r.items.map(x =>
      `<span class="pk-itx"><span class="pk-v pk-del">${esc(x.letter)}</span> ${x.name ? `→ <b>${esc(x.name)}</b>` : ""} ${x.sutra ? `<small>(${esc(x.sutra)})</small>` : ""}</span>`).join("")}</div>`;
  }
  /* Every upadeśa unit of the derivation, from the trace's own `parts` (current form · role · upadeśa), with what the trace shows of its it-kārya:
       ledger  — a 1.3.9 step took it-letters off it;   grown — its form got longer at a step with no 1.3.x row for it (an augment / ādeśa put in without it-steps: ledger S174 …);
       none    — no 1.3.9 step for it in this trace.  Built by comparing strings the engine already recorded; no grammar is computed here. */
  function itUnits(t) {
    const units = new Map(), order = [];
    t.forEach((s, i) => { const ps = parseParts(s.parts); if (!ps) return;
      ps.forEach(p => { const [f, role, u] = p; if (!u || ["pada", "other"].includes(roleOf(role)) || role === "abhyasa") return;
        const k = role + "|" + u; let x = units.get(k);
        if (!x) { x = {u, role, first: i, forms: [f], grown: []}; units.set(k, x); order.push(x); }
        const prev = x.forms[x.forms.length - 1];
        if (f !== prev) { if (f.length > prev.length && (f.endsWith(prev) || f.startsWith(prev) || f.includes(prev))) x.grown.push({i, sid: s.sutra_id, from: prev, to: f}); x.forms.push(f); } }); });
    return order;
  }
  function itLedger(t) {
    const rows = t.map((s, i) => ({s, i})).filter(({s}) => s.sutra_id === "1.3.9" && changes(s)).map(({s, i}) => ({i, r: itParse(s)})).filter(x => x.r);
    const units = itUnits(t), en = pref.gloss === "en";
    const nz = x => String(x || "").replace(/[~M\s]/g, "");
    const slpOf = dev => { try { return Transliterate.toSLP1(dev, "devanagari"); } catch (e) { return dev; } };
    const same = (up, x) => devOf(x.u) === up || nz(slpOf(up)) === nz(x.u) || nz(slpOf(up)).startsWith(nz(x.u)) || nz(x.u).startsWith(nz(slpOf(up)));      // the ledger prints the upadeśa as the 1.3.9 step wrote it; the unit is the trace's own spelling
    const kindOf = up => { const u = units.find(x => same(up, x)); return u ? ROLE[roleOf(u.role)][en ? 1 : 0] : "—"; };
    const rest = units.filter(x => !rows.some(({r}) => same(r.upadesha, x)));
    if (!rows.length && !rest.length) return "";
    const grown = rest.filter(x => x.grown.length), plain = rest.filter(x => !x.grown.length);
    const note = (en ? "from the trace's parts: each upadeśa unit, whether a 1.3.9 step took it-letters off it, and any growth of its form with no it-steps" : "ट्रेस के भागों से: प्रत्येक उपदेश-इकाई, १.३.९ से इत्-लोप हुआ या नहीं, और इत्-चरणों के बिना रूप-वृद्धि");
    return `<details class="pk-ledger"${pref.depth === "beginner" ? "" : " open"}><summary>${PED(en, note)} इत्संज्ञा-कोशः — ${rows.length} ${en ? "upadeśas with it-steps" : "उपदेशाः (इत्-चरणैः)"}${grown.length ? ` · <span class="pk-warn">⚠ ${grown.length} ${en ? "augment/ādeśa without it-steps" : "आगम/आदेश इत्-चरणों के बिना"}</span>` : ""}${plain.length ? ` · ${plain.length} ${en ? "with no it-step shown" : "इत्-चरण-रहिताः"}` : ""}</summary>
      <table class="pk-ledger-t"><tr><th>उपदेशः</th><th>${en ? "kind" : "प्रकारः"}</th><th>इत्-वर्णाः → संज्ञा (सूत्रम्)</th><th>लोपः</th></tr>${rows.map(({i, r}) =>
        `<tr><td class="dev"><b>${esc(r.upadesha)}</b></td><td>${esc(kindOf(r.upadesha))}</td><td>${r.items.map(x => `${esc(x.letter)} → <b>${esc(x.name)}</b> <small>${esc(x.sutra)}</small>`).join(" · ")}</td><td><a href="#s-${i + 1}">${i + 1}</a></td></tr>`).join("")}
      ${grown.map(x => `<tr class="pk-it-gap"><td class="dev"><b>${esc(devOf(x.u))}</b></td><td>${esc(ROLE[roleOf(x.role)][en ? 1 : 0])}</td><td>⚠ ${esc(x.grown.map(g => `${g.from} → ${g.to}`).join("; "))} — ${en ? "the engine put this in without running 1.3.2–1.3.9 on it (shortcut ledger S174)" : "इञ्जन ने इस पर १.३.२–१.३.९ चलाए बिना इसे जोड़ा (शॉर्टकट-बही S174)"}</td><td>${x.grown.map(g => `<a href="#s-${g.i + 1}">${g.i + 1}</a> <small>${esc(g.sid)}</small>`).join(" ")}</td></tr>`).join("")}
      ${plain.map(x => `<tr class="pk-it-none"><td class="dev">${esc(devOf(x.u))}</td><td>${esc(ROLE[roleOf(x.role)][en ? 1 : 0])}</td><td class="muted">${en ? "no 1.3.9 step in this trace (none is due for an ādeśa without an it-letter, e.g. ya)" : "इस ट्रेस में १.३.९ चरण नहीं (इत्-वर्णरहित आदेश, जैसे य, के लिए आवश्यक नहीं)"}</td><td></td></tr>`).join("")}</table></details>`;
  }

  /* a saṃjñā step: which part the name falls on */
  function samjnaChip(s, parts) {
    const m = SAMJNA[s.sutra_id]; if (!m && s.sutra_type !== "SAMJNA") return "";
    if (!m) return `<span class="pk-sj">संज्ञा-सूत्रम्</span>`;
    const [name, where] = m;
    if (!parts || !parts.length) return `<span class="pk-sj">संज्ञा: ${esc(name)}</span>`;
    // sesa (3.4.114): आर्धधातुकं शेषः — vikaraṇa/kṛt, never the tiṅ that 3.4.113 already named सार्वधातुक
    const idx = where === "last" ? [parts.length - 1] : where === "first" ? [0] : where === "pre" ? parts.slice(0, -1).map((_, k) => k)
      : where === "stem" ? [0]
      : where === "sesa" ? (() => {
          const v = parts.map((p, k) => [p, k]).filter(([p]) => roleOf(p[1]) === "vikarana").map(([, k]) => k);
          if (v.length) return v;
          const krt = parts.map((p, k) => [p, k]).filter(([p]) => ["krt", "taddhita"].includes(roleOf(p[1]))).map(([, k]) => k);
          if (krt.length) return krt;
          const nonTin = parts.map((p, k) => [p, k]).filter(([p]) => !["tin", "pratyaya"].includes(roleOf(p[1])) || (p[2] || "").match(/^(sya|sic|aG|tAsi)/)).map(([, k]) => k);
          return nonTin.length ? nonTin : [Math.max(0, parts.length - 2)];
        })()
      : parts.map((_, k) => k);
    const target = fmt(idx.map(k => parts[k]).filter(Boolean).map(p => p[0]).join(""), "");
    return `<span class="pk-sj" title="${esc(name)} — ${esc(target)} (◆ शिक्षण-सहायक: which part the saṃjñā falls on is shown by this page)">संज्ञा: <b>${esc(name)}</b> ⇐ <span class="pk-sj-t">${esc(target)}</span> <span class="pk-pedmark">◆</span></span>`;
  }

  /* → [{s, i, group?}] rows for the chosen depth; i is the index in the full trace (stable permalink). */
  function rowsFor(t) {
    const all = t.map((s, i) => ({s, i}));
    if (pref.depth === "shastriya") return all;
    const out = []; let grp = null;
    for (const r of all) {
      if (!applied(r.s)) continue;
      if (pref.depth === "beginner" && !isIt(r.s)) { grp = null; if (milestone(r.s)) out.push(r); continue; }
      if (isIt(r.s)) { if (!grp) { grp = {s: r.s, i: r.i, group: []}; out.push(grp); } grp.group.push(r.s); continue; }
      grp = null; out.push(r);
    }
    return pref.depth === "beginner" ? out.filter(r => !r.group || r.group.some(x => x.sutra_id === "1.3.9" && changes(x))) : out;
  }

  function gloss(s) {
    const a = fmt(s.form_before, s.form_before_dev), b = fmt(s.form_after, s.form_after_dev);
    if (pref.gloss === "sa") return s.why_now_dev || s.why_dev || "";
    if (pref.gloss === "hi") return s._hint_hi || s.why_now_dev || s.why_dev || "";
    const k = TYPE_EN[s.sutra_type] || "rule";
    return s._is_structural ? "" : changes(s) ? `Sūtra ${s.sutra_id} (${k}) rewrites ${a} as ${b}.` : `Sūtra ${s.sutra_id} (${k}) applies; the form stays ${a}.`;
  }

  /* 3.4.78 — eighteen tiṅ ādeśas (Pāṇini order). Vivakṣā (pada × puruṣa × vacana) picks one cell;
     the sūtra itself only substitutes the committed ādeśa (CONSTITUTION Art. 2). */
  const TIN78 = {
    pu: {3: ["प्रथमः", "3rd"], 2: ["मध्यमः", "2nd"], 1: ["उत्तमः", "1st"]},
    vc: {1: ["एकवचनम्", "sg"], 2: ["द्विवचनम्", "du"], 3: ["बहुवचनम्", "pl"]},
    pada: {parasmai: ["परस्मैपदम्", "parasmaipada"], atmane: ["आत्मनेपदम्", "ātmanepada"]},
    parasmai: [["tip", "तिप्"], ["tas", "तस्"], ["Ji", "झि"], ["sip", "सिप्"], ["Tas", "थस्"], ["Ta", "थ"], ["mip", "मिप्"], ["vas", "वस्"], ["mas", "मस्"]],
    atmane: [["ta", "त"], ["AtAm", "आताम्"], ["Ja", "झ"], ["TAs", "थास्"], ["ATAm", "आथाम्"], ["Dvam", "ध्वम्"], ["iw", "इट्"], ["vahi", "वहि"], ["mahiG", "महिङ्"]],
  };
  const tinCell = (pada, pu, vc) => {
    const list = TIN78[pada === "atmane" || pada === "Atmanepada" ? "atmane" : "parasmai"];
    const ri = {3: 0, 2: 1, 1: 2}[pu], ci = vc - 1;
    return list[ri * 3 + ci];
  };
  const chosenTin = s => {
    const p = parseParts(s.parts);
    if (p && p.length) { const last = p[p.length - 1]; if (last[2]) return last[2]; if (last[0]) return last[0]; }
    return (s.form_after || "").replace(/.*(?=[A-Z]?[a-zA-Z~]+$)/, "") || "";
  };
  /* 4.1.2 — the 21 sup (7 vibhakti × 3 vacana). A menu for students: the chosen cell comes from the step's sup; 1.4.21/22 (vacana) and 2.3.x (vibhakti) do not yet pick it (ledger S179). */
  const SUP21 = [["प्रथमा", [["su~", "सुँ"], ["O", "औ"], ["jas", "जस्"]]], ["द्वितीया", [["am", "अम्"], ["Ow", "औट्"], ["Sas", "शस्"]]],
    ["तृतीया", [["wA", "टा"], ["ByAm", "भ्याम्"], ["Bis", "भिस्"]]], ["चतुर्थी", [["Ne", "ङे"], ["ByAm", "भ्याम्"], ["Byas", "भ्यस्"]]],
    ["पञ्चमी", [["Nasi~", "ङसिँ"], ["ByAm", "भ्याम्"], ["Byas", "भ्यस्"]]], ["षष्ठी", [["Nas", "ङस्"], ["os", "ओस्"], ["Am", "आम्"]]], ["सप्तमी", [["Ni", "ङि"], ["os", "ओस्"], ["sup", "सुप्"]]]];
  function supGridHtml(s) {
    if (s.sutra_id !== "4.1.2" || !/^APPLIED/.test(s.status)) return "";
    const p = parseParts(s.parts), last = p && p.length ? p[p.length - 1] : null, raw = last ? String(last[0] || "") : "";
    const norm = x => String(x).replace(/[~]/g, ""), mark = norm(raw);          // exact upadeśa: O (au, prathamā) and Ow (auṭ, dvitīyā) are different cells
    const hit = SUP21.flatMap(([, r]) => r).filter(([k]) => mark && norm(k) === mark).length;
    const en = pref.gloss === "en";
    return `<details class="pk-supwrap no-print"><summary>${en ? "the 21 sup of 4.1.2" : "४.१.२ के २१ सुप्-प्रत्यय"} — ${mark ? `${en ? "chosen" : "चुना"}: <b class="dev">${esc(fmt(raw, ""))}</b>${hit > 1 ? (en ? " (the same form stands in several cells)" : " (यह रूप कई कोष्ठकों में है)") : ""}` : "—"}</summary>
      <table class="pk-sup"><tr><th></th><th>एकवचनम्</th><th>द्विवचनम्</th><th>बहुवचनम्</th></tr>${SUP21.map(([v, r]) => `<tr><th>${v}</th>${r.map(([k, dv]) => `<td class="dev${mark && norm(k) === mark ? " pk-sup-on" : ""}">${dv}</td>`).join("")}</tr>`).join("")}</table>
      <div class="muted">${PED(en)} ${en ? "A menu for students. Today the caller's (vibhakti, vacana) picks the cell; 1.4.21/22 (vacana by number) and 1.4.103 (the names) should do it — ledger S179." : "शिक्षण हेतु तालिका। अभी (विभक्ति, वचन) कर्ता से आता है; १.४.२१/२२ तथा १.४.१०३ को यह करना चाहिए — S179।"}</div></details>`;
  }
  function tinGridHtml(s, viv) {
    if (s.sutra_id !== "3.4.78" || !/^APPLIED/.test(s.status)) return "";
    const en = pref.gloss === "en";
    const chosen = (s._tin_chosen || chosenTin(s) || "").trim();
    let pada = (viv && (viv.pada || viv.pada_key) || "").replace(/^Atmane.*/i, "atmane").replace(/^Parasmai.*/i, "parasmai");
    if (!pada && chosen) {
      const inA = TIN78.atmane.some(([sl]) => sl === chosen);
      const inP = TIN78.parasmai.some(([sl]) => sl === chosen);
      pada = inA && !inP ? "atmane" : "parasmai";
    }
    if (!pada) pada = "parasmai";
    const pu = viv && +viv.purusha || 0, vc = viv && +viv.vacana || 0;
    const expect = (pu && vc) ? tinCell(pada, pu, vc) : null;
    const mark = expect ? expect[0] : chosen;
    const lak = (viv && (viv.lakara_dev || viv.lakara)) || "";
    const puL = TIN78.pu[pu] ? TIN78.pu[pu][en ? 1 : 0] : (pu || "—");
    const vcL = TIN78.vc[vc] ? TIN78.vc[vc][en ? 1 : 0] : (vc || "—");
    const pdL = TIN78.pada[pada] ? TIN78.pada[pada][en ? 1 : 0] : pada;
    const banner = en
      ? `Vivakṣā (from dhātūrūpa): lakāra ${lak || "—"} · ${pdL} · ${puL} · ${vcL} → chosen <b class="dev">${esc(fmt(mark, expect ? expect[1] : ""))}</b>. 3.4.78 lists all 18; 1.4.99–1.4.103 name pada/puruṣa/vacana; the recipe commits this cell (Art. 2 — the sūtra does not read the coordinates).`
      : `विवक्षा (धातु-रूपे चयनिता): लकार ${esc(lak || "—")} · ${esc(pdL)} · ${esc(puL)} · ${esc(vcL)} → चुनाः <b class="dev">${esc(expect ? expect[1] : fmt(mark, ""))}</b> (${esc(mark)})। ३.४.७८ अष्टादश तिङ्; १.४.९९–१.४.१०३ पद/पुरुष/वचन-संज्ञाः; रेसिपिः एतद्-कोष्ठं निश्चिनोति (संविधान २ — सूत्रं निर्देशान् न पठति)।`;
    const half = (key, title) => {
      const cells = TIN78[key];
      let h = `<table class="pk-tin"><caption>${esc(title)}</caption><tr><th></th><th>${esc(TIN78.vc[1][en ? 1 : 0])}</th><th>${esc(TIN78.vc[2][en ? 1 : 0])}</th><th>${esc(TIN78.vc[3][en ? 1 : 0])}</th></tr>`;
      [3, 2, 1].forEach((pui, ri) => {
        h += `<tr><th>${esc(TIN78.pu[pui][en ? 1 : 0])}</th>`;
        [1, 2, 3].forEach((vci, ci) => {
          const [sl, dv] = cells[ri * 3 + ci];
          const hit = sl === mark || (key === pada && pui === pu && vci === vc);
          h += `<td class="${hit ? "pk-tin-hit" : ""}" title="${esc(sl)}">${esc(dv)}<small>${esc(sl)}</small>${hit ? `<span class="pk-tin-pick">${en ? "chosen" : "चुनाः"}</span>` : ""}</td>`;
        });
        h += `</tr>`;
      });
      return h + `</table>`;
    };
    return `<div class="pk-tinwrap"><div class="pk-tin-banner">${PED(en, en ? "The grid is a menu for students; sūtra 3.4.78 only substitutes the ādeśa the vivakṣā chose (1.4.100–108 name pada/puruṣa/vacana)" : "यह तालिका विद्यार्थियों हेतु है; ३.४.७८ केवल वक्ता-इच्छा से चुना आदेश रखता है")} ${banner}</div>
      <div class="pk-tin-grid">${half("parasmai", TIN78.pada.parasmai[en ? 1 : 0])}${half("atmane", TIN78.pada.atmane[en ? 1 : 0])}</div>
      <div class="pk-tin-note muted">${en
        ? "Later lakāra-specific rewrites (loṭ 3.4.85–93, liṅ, …) may still change this ādeśa; the grid is the 3.4.78 menu."
        : "लोठ् ३.४.८५–९३ आदि लकार-विशेष आदेशाः पश्चात् भिन्दन्ति; अत्र ३.४.७८-सूची एव।"}</div></div>`;
  }

  /* the kind of sūtra, in colour and plain words — every row carries it so a new student sees at once what sort of rule fired */
  const TYPE_PLAIN = {VIDHI: ["विधिः", "Does something", "the rule makes a change or adds a part"], SAMJNA: ["संज्ञा", "Gives a name", "the rule defines a technical name"],
    PARIBHASHA: ["परिभाषा", "Reading rule", "a rule about how other rules are read"], ADHIKARA: ["अधिकारः", "Heading", "a heading that governs the rules after it"],
    NIYAMA: ["नियमः", "Restricts", "limits where another rule may act"], PRATISHEDHA: ["प्रतिषेधः", "Forbids", "stops another rule from acting"],
    ATIDESHA: ["अतिदेशः", "Treats as", "says: treat this as if it were that"], VIBHASHA: ["विभाषा", "Optional", "the rule may or may not apply"],
    ANUVADA: ["अनुवादः", "Restates", "repeats something already taught"], NIPATANA: ["निपातनम्", "Irregular", "fixes an irregular form by statement"]};
  const typeChip = s => { const t = TYPE_PLAIN[s.sutra_type]; if (!t) return ""; return `<span class="pk-type pk-ty-${esc(s.sutra_type)}" title="${esc(t[2])}">${esc(pref.gloss === "en" ? t[1] : t[0])}</span>`; };
  /* the sūtra itself, opened with one click on every row (Śāstrīya depth shows it open) */
  const sutraCard = (s, deepOpen) => {
    if (!s._sutra_text_dev && !s._padaccheda_dev && !(s._anuvritti_from || []).length) return "";
    const t = TYPE_PLAIN[s.sutra_type];
    return `<details class="pk-sutra"${deepOpen ? " open" : ""}><summary>📖 ${pref.gloss === "en" ? "The sūtra" : "सूत्रम्"}</summary><div class="pk-sutra-b">
      ${s._sutra_text_dev ? `<div class="pk-sutra-t dev">${esc(s._sutra_text_dev)}</div>` : ""}
      ${s._padaccheda_dev ? `<div class="pk-sutra-p dev"><b>${pref.gloss === "en" ? "split into words" : "पदच्छेदः"}:</b> ${esc(s._padaccheda_dev)}</div>` : ""}
      ${(s._anuvritti_from || []).length ? `<div class="pk-sutra-a"><b>${pref.gloss === "en" ? "carried in from" : "अनुवृत्तिः"}:</b> ${s._anuvritti_from.map(x => `<a href="/sutra/${esc(x)}">${esc(x)}</a>`).join(", ")}</div>` : ""}
      ${t ? `<div class="pk-sutra-k"><b>${esc(t[0])}</b> — ${esc(t[2])}</div>` : ""}</div></details>`;
  };

  /* the vyutpatti prakriyā a note was written on: every row of the full trace, the noted step marked — saved with the note so the question can be reproduced */
  const traceText = (d, t, at) => {
    const viv = d.vivaksa || d["vivakṣā"] || null, surface = d.surface ? `${d.surface.dev || ""} (${d.surface.slp1 || ""})` : "";
    const L = [`Derivation: ${d.title || "—"} → ${surface}`, `Page: ${location.pathname}${location.search}`, `Rows: ${t.length} (full trace; #n = the row number, stable across depths)`];
    if (viv) L.push(`Vivakṣā: ${Object.entries(viv).map(([k, v]) => `${k}=${v}`).join(" · ")}`);
    L.push(`Marked ◀ = the step this note is about (#${at + 1}).`, "");
    t.forEach((s, i) => {
      const why = s.status === "BLOCKED" ? s.gate_reason : s.status === "SKIPPED" ? s.skip_reason : "";
      L.push(`#${i + 1} ${s.sutra_id} [${s.status}] ${s.form_before} → ${s.form_after}${s.parts ? "  parts=" + (typeof s.parts === "string" ? s.parts : JSON.stringify(s.parts)) : ""}${why ? "  (" + String(why).slice(0, 160) + ")" : ""}${i === at ? "   ◀ NOTE HERE" : ""}`);
    });
    return L.join("\n");
  };

  /* ✎ a question / doubt / note on this step: it is saved under the sūtra (webui/notes.py) and shows on /sutra/<id>, with the derivation and step it came from */
  let NOTE_N = null;
  const noteCounts = () => { if (!NOTE_N) { NOTE_N = {}; fetch("/api/notes-counts").then(r => r.json()).then(o => { NOTE_N = o; document.querySelectorAll(".pk-ask").forEach(b => { b.innerHTML = askLabel(b.dataset.sid); }); }).catch(() => {}); } return NOTE_N; };
  const askLabel = sid => { const c = (noteCounts()[sid] || {}).n; return `✎${c ? `<small>${c}</small>` : ""}`; };
  const askBtn = (sid, i) => `<button type="button" class="pk-ask no-print" data-sid="${esc(sid)}" data-i="${i}" title="${pref.gloss === "en" ? "Ask a question or add a note on this sūtra (saved under it)" : "इस सूत्र पर प्रश्न / टिप्पणी जोड़ें (सूत्र-पृष्ठ पर सुरक्षित)"}">${askLabel(sid)}</button>`;

  function row({s, i, group}, ctx) {
    const st = STATUS[s.status] || [s.status, s.status], id = "s-" + (i + 1), deep = pref.depth === "shastriya";
    const star = lk().has(s.sutra_id) && pref.depth !== "beginner" ? `<span class="pk-lk" title="Laghukaumudī sūtra">★</span>` : "";
    const struct = isStruct(s) ? `<span class="pk-struct" title="Engine bookkeeping (e.g. merging parts into one pada) — not an Aṣṭādhyāyī sūtra">⚙ ${pref.gloss === "en" ? "structural, not a sūtra" : "संरचनात्मक — सूत्र नहीं"}</span>` : "";
    if (group) {
      const lopa = [...group].reverse().find(x => x.sutra_id === "1.3.9" && changes(x));
      const li = lopa ? ctx.t.indexOf(lopa) : -1;
      const named = [...new Set(group.filter(x => x.sutra_id !== "1.3.9").map(x => x.sutra_id))];
      return `<li class="pk-step pk-applied pk-itgrp" id="${id}">${li >= 0 && li + 1 !== i + 1 ? `<span id="s-${li + 1}"></span>` : ""}<a class="pk-no" href="#${id}">${i + 1}</a><div class="pk-main">
      <div><b class="dev">इत्संज्ञा-लोपः</b> <span class="pk-tag">${named.map(x => `<a href="/sutra/${esc(x)}">${esc(x)}</a>`).join(" · ") || "1.3.2–1.3.8"} → <a href="/sutra/1.3.9">1.3.9</a></span>${askBtn("1.3.9", li >= 0 ? li : i)}
        ${lopa ? `<span class="pk-form pk-fx dev" data-i="${li}" title="क्लिक् — संहितम् ↔ वर्णविभागः">${formHtml(lopa, ctx.pb[li], ctx.pa[li] || ctx.pb[li], pref.split !== ctx.open.has(li))}</span>` : ""}</div>
      ${lopa ? itChips(lopa) : ""}
      <div class="pk-gloss">${PED(pref.gloss === "en", "Grouped display: Śāstrīya depth lists each of 1.3.2–1.3.9 as its own step")} ${esc(pref.gloss === "en" ? "it-letters of the upadeśa are named (1.3.2–1.3.8) and removed (1.3.9); the record (kit, ṅit, pit …) stays for later rules" : "उपदेशे इत्-वर्णानां संज्ञा (१.३.२–१.३.८), तस्य लोपः (१.३.९); इत्-अभिलेखः (कित्, ङित्, पित् …) परसूत्रेभ्यः स्थिरः")}</div></div></li>`;
    }
    const why = s.status === "BLOCKED" ? s.gate_reason : s.status === "SKIPPED" ? s.skip_reason : "";
    const sch = deep ? `
      <div class="pk-sch">${s._sutra_text_dev ? `<span class="dev">${esc(s._sutra_text_dev)}</span>` : ""}
        ${s._padaccheda_dev ? `<span class="muted dev"> · ${esc(s._padaccheda_dev)}</span>` : ""}
        ${(s._anuvritti_from || []).length ? `<div class="muted">अनुवृत्तिः ← ${s._anuvritti_from.map(x => `<a href="/sutra/${esc(x)}">${esc(x)}</a>`).join(", ")}</div>` : ""}
        ${why ? `<div class="pk-why">${esc(why)}</div>` : ""}
        ${(s._lsk || []).length ? `<div class="muted">LSK pp. ${esc([...new Set(s._lsk.map(x => x.page))].slice(0, 6).join(", "))}${s._lsk.length > 6 ? "…" : ""}</div>` : ""}</div>` : "";
    return `<li class="pk-step pk-${(s.status || "").toLowerCase()} pk-t-${esc(s.sutra_type || "X")}" id="${id}">
      <a class="pk-no" href="#${id}" title="permalink to this step">${i + 1}</a>
      <div class="pk-main"><div><a class="pk-sid" href="/sutra/${esc(s.sutra_id)}">${esc(s.sutra_id)}</a>${star}${struct}${askBtn(s.sutra_id, i)}${isStruct(s) ? "" : `<button type="button" class="pk-hide no-print" data-sid="${esc(s.sutra_id)}" title="Hide this sūtra in every prakriyā (still included in Copy to LLM)">🙈</button>`} ${typeChip(s)}
        <span class="pk-tag">${esc(pref.gloss === "en" ? st[1] : st[0])}</span>
        ${samjnaChip(s, ctx.pa[i] || ctx.pb[i])}
        <span class="pk-form pk-fx dev${ctx.padaAt >= 0 && i >= ctx.padaAt ? " pk-padaed" : ""}" data-i="${i}" title="${ctx.padaAt >= 0 && i >= ctx.padaAt ? "पदम् (सुप्तिङन्तं पदम् १.४.१४) — whole word, stem + ending · " : ""}क्लिक् — संहितम् ↔ वर्णविभागः (click: merged ↔ split)">${
          formHtml(s, ctx.pb[i], ctx.pa[i] || ctx.pb[i], pref.split !== ctx.open.has(i))}</span></div>
        ${tinGridHtml(s, ctx.viv)}${supGridHtml(s)}
        <div class="pk-gloss">${pedGloss(s) && gloss(s) ? PED(pref.gloss === "en") + " " : ""}${esc(gloss(s))}</div>${deep ? "" : sutraCard(s, false)}${sch}</div></li>`;
  }

  /* "Why didn't rule X apply?" — what the trace says about one sūtra. */
  function inspect(t, sid) {
    sid = sid.trim(); if (!sid) return "";
    const hits = t.map((s, i) => ({s, i})).filter(({s}) => s.sutra_id === sid);
    const link = `<a href="/sutra/${esc(sid)}">${esc(sid)}</a>`;
    const kas = `<details class="pk-kas" data-sid="${esc(sid)}"><summary>📖 Kāśikā ${esc(sid)} — ${pref.gloss === "en" ? "what the tradition says (for students)" : "परम्परा क्या कहती है (छात्रों हेतु)"}</summary><div class="pk-kas-b muted dev">…</div></details>`;
    if (!hits.length) return `${link}: never offered in this derivation — its conditions were not even reached (or it is not implemented).${kas}`;
    return hits.map(({s, i}) => {
      const st = STATUS[s.status] || [s.status, s.status], why = s.gate_reason || s.skip_reason || s.why_now_dev || s.why_dev || "";
      const verdict = s.status === "BLOCKED" ? "blocked" : s.status === "SKIPPED" ? "checked, did not apply" : /^APPLIED/.test(s.status) ? "applied" : (STATUS[s.status] || [0, s.status])[1];
      return `${link} <a href="#s-${i + 1}">step ${i + 1}</a>: <b>${esc(verdict)}</b> (${esc(st[0])})${why ? ` — <span class="dev">${esc(why)}</span>` : ""}`;
    }).join("<br>") + kas;
  }

  /* repeated checked/blocked/skipped rows of one sūtra → one line, click to expand; user-hidden sūtras are dropped from the screen only (llm/plain copy use rowsFor, unfiltered) */
  function collapseRows(rows) {
    const key = r => r.group || applied(r.s) || isStruct(r.s) ? null : r.s.sutra_id + "|" + r.s.status, n = {}, seen = {};
    rows.forEach(r => { const k = key(r); if (k) n[k] = (n[k] || 0) + 1; });
    return rows.flatMap(r => { const k = key(r); if (!k || n[k] < 2) return [r]; if (seen[k]) return []; seen[k] = 1; return [{rep: rows.filter(x => key(x) === k)}]; });
  }

  /* shared ✎ form for pages that show a step outside the engine panel (Vidyut / corpus columns): saves a note under the sūtra */
  function noteForm(host, sid, where, trace, hint) {
    host.innerHTML = `<form class="pk-askform no-print"><div class="pk-ask-h"><b>✎ ${esc(sid)}</b> <span class="muted">· ${esc(hint || where)}</span></div>
      <select name="kind"><option value="question">प्रश्न · question</option><option value="doubt">संशय · doubt</option><option value="note">टिप्पणी · note</option><option value="solution">समाधान · proposed solution</option></select>
      <textarea name="text" rows="3" required placeholder="Your question, doubt or note on this sūtra…"></textarea>
      <button type="submit">Save under ${esc(sid)}</button> <button type="button" data-x="1">Cancel</button> <span class="pk-ask-msg muted"></span></form>`;
    const f = host.firstChild; f.text.focus();
    f.addEventListener("click", e => { if (e.target.dataset.x) host.innerHTML = ""; });
    f.addEventListener("submit", async e => {
      e.preventDefault();
      try {
        const r = await fetch("/api/notes/" + encodeURIComponent(sid), {method: "POST", headers: {"Content-Type": "application/json"},
          body: JSON.stringify({text: f.text.value, kind: f.kind.value, author: "me", derivation: where + " · " + location.pathname, trace: trace || ""})});
        if (!r.ok) throw new Error(await r.text());
        NOTE_N = null; noteCounts();
        host.innerHTML = `<span class="muted">Saved under ${esc(sid)} — <a href="/sutra/${esc(sid)}#sutra-notes" target="_blank">open the sūtra page</a></span>`;
      } catch (err) { f.querySelector(".pk-ask-msg").textContent = "Save failed: " + String(err.message).slice(0, 120); }
    });
  }
  /* ✎ button for an outside step (Vidyut / corpus rows) */
  const outBtn = sid => `<button type="button" class="pk-ask vm-note no-print" data-sid="${esc(sid)}" title="Note / question on this sūtra (saved under it)">✎</button>`;
  /* one delegated click handler: opens the form under the clicked step; ctx() → {where, trace} */
  function wireOutNotes(root, ctx) {
    root.addEventListener("click", ev => {
      const b = ev.target.closest(".vm-note"); if (!b) return;
      const step = b.closest(".dr-step"), c = ctx(b.dataset.sid) || {};
      let host = step ? step.nextElementSibling : null;
      if (!host || !host.classList.contains("vm-host")) { host = document.createElement("div"); host.className = "vm-host"; (step || b.parentNode).after(host); }
      noteForm(host, b.dataset.sid, c.where || "", c.trace || "", c.hint);
    });
  }

  /* Copy to LLM for the Vidyut column: Vidyut's steps + the sūtras our engine did not run + our engine's trace, with the audit prompt */
  function vidyutLlmText({title, V, missing, E, corpus}, plain) {
    const vs = Array.isArray(V) ? V.map(pth => `${pth.text || ""}\n` + (pth.steps || []).map((st, n) => `  ${n + 1}. ${st.code}  ${(st.result || []).map(x => fmt(x, "")).join(" + ")}`).join("\n")).join("\n\n") : String((V && V.error) || "Vidyut unavailable");
    const et = ((E && E.trace) || []).filter(x => applied(x)).map(x => `  #${(E.trace.indexOf(x)) + 1} ${x.sutra_id} [${x.status}] ${x.form_before} → ${x.form_after}`).join("\n");
    const cs = corpus ? `\n\n===== CORPUS (hand-checked upstream) ${corpus.form}\n` + corpus.steps.map((x, n) => `  ${n + 1}. ${x.step}  ${(x.sutras || []).join(", ")}`).join("\n") : "";
    const head = `Act as a Pāṇini Aṣṭādhyāyī expert and a strict, fair auditor of a computational prakriyā engine (Panini Engine v3).
Below, Vidyut (an external engine, only a minimum-rule floor — never an authority) and our engine derive the same form. Compare them against the Aṣṭādhyāyī and the Kāśikā.
- Vidyut steps may include no-op stamps (a sūtra named although no letter changes); say which Vidyut sūtras genuinely act and which are stamps.
- For each sūtra Vidyut runs and our engine does not: is it an engine gap, a Vidyut artefact, or a display issue? Give the reason and the sūtra text.
- Say where our engine is right and Vidyut is wrong. End with a severity summary (blocker / major / minor). Audit only; do not rewrite the engine.

`;
    return (plain ? "" : head) + `===== ${title}
VIDYUT:
${vs}

Vidyut sūtras our engine did not execute: ${(missing || []).join(", ") || "none"}

OUR ENGINE (applied steps only; #n = index in the full trace):
${et || "  (no trace)"}${cs}
`;
  }
  async function copyText(text, btn) {
    const o = btn.textContent; let ok = true;
    try {
      if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(text);
      else { const ta = document.createElement("textarea"); ta.value = text; ta.style.cssText = "position:fixed;left:-9999px"; document.body.appendChild(ta); ta.select(); document.execCommand("copy"); ta.remove(); }
    } catch (e) { ok = false; }
    btn.textContent = ok ? "Copied ✓" : "Copy failed"; setTimeout(() => { btn.textContent = o; }, 1600);
  }

  function mount(el, d) {
    const t = d.trace || [], L = t[t.length - 1];
    if (!d.surface && L && L.form_after) d.surface = {slp1: L.form_after, dev: L.form_after_dev};
    const sel = (id, opts, v) => `<select id="${id}">${opts.map(([k, l]) => `<option value="${k}"${k === v ? " selected" : ""}>${l}</option>`).join("")}</select>`;
    const ctx = {pb: [], pa: [], open: new Set(), t, viv: d.vivaksa || d.vivakṣā || null};
    ctx.padaAt = t.findIndex(s => applied(s) && ["1.4.14", "1.4.15", "1.4.16", "1.4.17"].includes(s.sutra_id));   // from here on the whole form is a pada
    let last = null;                                              // parts of the tape before each step, after each applied step
    t.forEach((s, i) => { let p = parseParts(s.parts);
      if ((!p || !p.length) && s.sutra_id === "__MERGE__") p = [[String(s.form_after || ""), "pada", ""]];   // after the merge it is ONE word, not stem | ending
      ctx.pb[i] = last && joined(last) === String(s.form_before || "").replace(/\s/g, "") ? last : null;
      if (p && p.length) { ctx.pa[i] = p; last = p; } });
    const roles = [...new Set(ctx.pa.filter(Boolean).flat().map(p => roleOf(p[1])))];
    const legend = () => roles.length ? `${PED(pref.gloss === "en")} <span class="muted">भागाः:</span> ${roles.map(r => `<span class="pk-part pk-r-${r}">${esc(ROLE[r][pref.gloss === "en" ? 1 : 0])}</span>`).join(" ")}
      <span class="muted"> · <span class="pk-v pk-del">स्थानी</span> → <span class="pk-v pk-ins">नूतनम्</span> · ${pref.gloss === "en" ? "click a form to split / merge its varṇas" : "रूपे क्लिक् — वर्णविभागः / संहितम्"}</span>` : "";
    el.innerHTML = `<div class="pk-bar no-print">
      <label>गहनता ${sel("pk-depth", [["beginner", "आरम्भिकः · Beginner"], ["kaumudi", "कौमुदी · Kaumudī"], ["shastriya", "शास्त्रीयः · Śāstrīya"]], pref.depth)}</label>
      <label>लिपिः ${sel("pk-script", [["dev", "देवनागरी"], ["varna", "देवनागरी — वर्ण-विभागः"], ["slp1", "SLP1"], ["iast", "IAST"]], pref.script)}</label>
      <label>व्याख्या ${sel("pk-gloss", [["hi", "हिन्दी"], ["en", "English"], ["sa", "संस्कृतम्"]], pref.gloss)}</label>
      <label>वर्णाः ${sel("pk-split", [["0", "संहितम् · merged (राम)"], ["1", "विभक्तम् · split (र् आ म् अ)"]], pref.split ? "1" : "0")}</label>
      <button type="button" id="pk-full" class="pk-btn-full" title="Full page — use the whole screen (Esc to close)">⛶ Full page</button><button type="button" id="pk-print">Print</button><button type="button" id="pk-json">Export JSON</button>
      <button type="button" id="pk-copy" class="pk-btn-copy" title="पैनल् में दिखी पूरी प्रक्रिया — Copy entire panel">प्रतिलिपिः · Copy panel</button>
      <button type="button" id="pk-copy-llm" class="pk-btn-copy" title="LLM-समीक्षा हेतु — Copy panel + audit prompt">LLM-कृते · Copy to LLM</button></div>
      <h2 class="pk-result dev"></h2><div class="pk-letters"></div><div class="pk-letter-info muted" aria-live="polite"></div>
      <div class="pk-legend"></div><div class="pk-ledger-box"></div><p class="muted pk-count"></p><div class="pk-auth muted"></div><div class="pk-hidden-bar no-print"></div><ol class="pk-list"></ol>
      <div class="pk-inspect no-print"><label>कस्मात् सूत्रं न प्रयुक्तम्? · Why didn't rule apply? <input class="pk-sid-in" placeholder="e.g. 7.1.9" size="10"></label>
        <button type="button" class="pk-inspect-note" title="Note on this sūtra: why you think it was needed here, with the śāstra that supports it">✎ टिप्पणी · note</button>
        <div class="pk-inspect-out" aria-live="polite"></div><div class="pk-inspect-form"></div></div>`;
    const q = s => el.querySelector(s);
    const finalParts = [...ctx.pa].reverse().find(Boolean) || [];
    const authNote = () => {
      const en = pref.gloss === "en", sh = pref.depth === "shastriya";
      return `<b>${en ? "How to read this page" : "इस पृष्ठ को कैसे पढ़ें"}</b> — ${en
        ? "Every numbered row is a step of the engine's own trace (a sūtra, its status, the form before and after). "
        : "प्रत्येक क्रमाङ्कित पङ्क्ति इञ्जन-प्रक्रिया का वास्तविक चरण है (सूत्र, स्थिति, पूर्व-पश्चात् रूप)। "}${PED(en)} ${en
        ? "marks what this page adds for teaching (colours, letter chips, saṃjñā targets, tiṅ menu, grouped it-rows, glosses in English/Hindi hints); it is not part of Pāṇini's sequence. ⚙ marks engine bookkeeping that is not a sūtra. "
        : "का अर्थ: शिक्षण हेतु इस पृष्ठ का जोड़ा हुआ (रङ्ग, वर्ण-चिह्न, संज्ञा-लक्ष्य, तिङ्-सूची, समूहित इत्-पङ्क्ति, हिन्दी/English संकेत); यह पाणिनीय क्रम नहीं। ⚙ = इञ्जन की संरचना, सूत्र नहीं। "}${sh ? "" : (en
        ? "This depth hides checked / skipped / blocked rows; step numbers stay those of the full trace (Śāstrīya depth shows all)."
        : "इस गहनता में निरीक्षित/अतिक्रान्त/निवारित पङ्क्तियाँ छिपी हैं; क्रमाङ्क पूर्ण-क्रम के ही रहते हैं (शास्त्रीय में सब दिखता है)।")}`;
    };
    const letters = () => (d.letters || []).length ? PED(pref.gloss === "en") + " " + lettersChips() : "";
    const lettersChips = () => (d.letters || []).map((l, n) => `<button type="button" class="pk-letter${l.origin.length ? "" : " pk-given"} pk-r-${roleOf((finalParts[l.term] || [])[1])}" data-n="${n}"
      title="${l.origin.length ? "created by " + esc(l.origin.join(", ")) : "given (upadeśa)"}">${esc(fmt(l.slp1, ""))}</button>`).join("");
    const paint = () => {
      const hid = new Set(pref.hidden || []), rows = collapseRows(rowsFor(t).filter(r => r.group || !hid.has(r.s.sutra_id)));
      q(".pk-list").innerHTML = rows.map(r => {
        if (!r.rep) return row(r, ctx);
        const f = r.rep[0].s, st = STATUS[f.status] || [f.status, f.status];
        return `<li class="pk-rep"><details><summary><a class="pk-sid" href="/sutra/${esc(f.sutra_id)}">${esc(f.sutra_id)}</a> <span class="pk-tag">${esc(pref.gloss === "en" ? st[1] : st[0])}</span> ×${r.rep.length} <span class="muted">· steps ${r.rep.map(x => x.i + 1).join(", ")}</span></summary><ol class="pk-rep-list">${r.rep.map(x => row(x, ctx)).join("")}</ol></details></li>`;
      }).join("") || "<li class='muted'>—</li>";
      q(".pk-hidden-bar").innerHTML = hid.size ? `<span class="muted">🙈 hidden on screen (kept in Copy to LLM):</span> ${[...hid].map(x => `<button type="button" class="pk-unhide" data-sid="${esc(x)}" title="Show again">${esc(x)} ✕</button>`).join(" ")}` : "";
      q(".pk-legend").innerHTML = legend() + `<div class="pk-tkey"><b>${pref.gloss === "en" ? "Rule colours" : "सूत्र-रङ्गाः"}:</b> ${Object.entries(TYPE_PLAIN).map(([k, v]) => `<span class="pk-type pk-ty-${k}" title="${esc(v[2])}">${esc(pref.gloss === "en" ? v[1] : v[0])}</span>`).join(" ")}</div>`;
      q(".pk-auth").innerHTML = authNote();
      q(".pk-ledger-box").innerHTML = itLedger(t);
      q(".pk-count").textContent = pref.depth === "beginner" ? `${rows.length} milestones (of ${t.length} rule checks). Choose Kaumudī or Śāstrīya for more.`
        : pref.depth === "kaumudi" ? `${rows.length} rows — every applied sūtra; ★ = in the Laghukaumudī list.` : `${t.length} rows: ${t.filter(applied).length} applied.`;
      q(".pk-result").innerHTML = `${esc(d.title || "")} ${d.surface ? `→ <b>${esc(fmt(d.surface.slp1, d.surface.dev))}</b>` : ""}`;
      q(".pk-letters").innerHTML = letters();
      if (location.hash.startsWith("#s-")) { const n = document.getElementById(location.hash.slice(1)); if (n) { n.classList.add("pk-hit"); n.scrollIntoView({block: "center"}); } }
    };
    [["pk-depth", "depth"], ["pk-script", "script"], ["pk-gloss", "gloss"]].forEach(([id, k]) =>
      q("#" + id).addEventListener("change", e => { pref[k] = e.target.value; save(); window.dispatchEvent(new Event("prakriya-change")); }));
    q("#pk-split").addEventListener("change", e => { pref.split = e.target.value === "1"; ctx.open.clear(); save(); window.dispatchEvent(new Event("prakriya-change")); });
    q(".pk-list").addEventListener("click", async e => {            // ✎ ask / note on this step
      const b = e.target.closest(".pk-ask"); if (!b) return;
      const host = b.closest("li"); let f = host.querySelector(".pk-askform");
      if (f) { f.remove(); return; }
      const sid = b.dataset.sid, i = +b.dataset.i, s = t[i] || {};
      f = document.createElement("form"); f.className = "pk-askform no-print";
      f.innerHTML = `<div class="pk-ask-h"><b>✎ ${esc(sid)}</b> <span class="muted">· step ${i + 1} · ${esc(String(s.form_before || ""))} → ${esc(String(s.form_after || ""))}</span></div>
        <select name="kind"><option value="question">प्रश्न · question</option><option value="doubt">संशय · doubt</option><option value="note">टिप्पणी · note</option><option value="solution">समाधान · proposed solution</option></select>
        <textarea name="text" rows="3" required placeholder="${pref.gloss === "en" ? "Your question, doubt or note on this sūtra in this derivation…" : "इस प्रक्रिया में इस सूत्र पर आपका प्रश्न / संशय / टिप्पणी…"}"></textarea>
        <button type="submit">Save under ${esc(sid)}</button> <button type="button" data-x="1">Cancel</button> <span class="pk-ask-msg muted"></span>`;
      host.querySelector(".pk-main").appendChild(f);
      f.querySelector("textarea").focus();
      f.addEventListener("click", ev => { if (ev.target.dataset.x) f.remove(); });
      f.addEventListener("submit", async ev => {
        ev.preventDefault(); const m = f.querySelector(".pk-ask-msg");
        const where = `${d.title || ""} · step #${i + 1} (${s.form_before || ""} → ${s.form_after || ""}) · ${location.pathname}${location.search}#s-${i + 1}`;
        try {
          const r = await fetch("/api/notes/" + encodeURIComponent(sid), {method: "POST", headers: {"Content-Type": "application/json"},
            body: JSON.stringify({text: f.text.value, kind: f.kind.value, author: "me", derivation: where, trace: traceText(d, t, i)})});
          if (!r.ok) throw new Error(await r.text());
          NOTE_N = null; noteCounts();
          f.innerHTML = `<span class="muted">Saved under ${esc(sid)} — <a href="/sutra/${esc(sid)}#sutra-notes" target="_blank">open the sūtra page</a></span>`;
        } catch (err) { m.textContent = "Save failed: " + String(err.message).slice(0, 120); }
      });
    });
    el.addEventListener("click", e => {                            // 🙈 hide / ✕ show a sūtra everywhere
      const h = e.target.closest(".pk-hide, .pk-unhide"); if (!h) return;
      const set = new Set(pref.hidden || []); h.classList.contains("pk-hide") ? set.add(h.dataset.sid) : set.delete(h.dataset.sid);
      pref.hidden = [...set]; save(); window.dispatchEvent(new Event("prakriya-change"));
    });
    q(".pk-list").addEventListener("click", e => {                 // one form: merged ↔ split
      const f = e.target.closest(".pk-fx"); if (!f) return;
      const i = +f.dataset.i; ctx.open.has(i) ? ctx.open.delete(i) : ctx.open.add(i);
      const s = t[i]; f.innerHTML = formHtml(s, ctx.pb[i], ctx.pa[i] || ctx.pb[i], pref.split !== ctx.open.has(i));
    });
    q(".pk-letters").addEventListener("click", e => {
      const b = e.target.closest(".pk-letter"); if (!b) return;
      const l = d.letters[+b.dataset.n];
      q(".pk-letter-info").innerHTML = l.origin.length ? `${esc(fmt(l.slp1, ""))} ← ${l.origin.map(o => {
        const i = t.findIndex(s => s.sutra_id === o && applied(s));
        return `<a href="/sutra/${esc(o)}">${esc(o)}</a>${i >= 0 ? ` (<a href="#s-${i + 1}">step ${i + 1}</a>)` : ""}`; }).join(", ")}` : `${esc(fmt(l.slp1, ""))} — part of the given upadeśa, not created by a rule.`;
    });
    q(".pk-inspect-note").addEventListener("click", () => {          // ✎ "this sūtra seems needed here" — note + śāstra support, saved under that sūtra
      const box = q(".pk-inspect-form"), sid = q(".pk-sid-in").value.trim();
      if (box.firstChild) { box.innerHTML = ""; return; }
      if (!/^\d+\.\d+\.\d+$/.test(sid)) { q(".pk-inspect-out").textContent = "Type a sūtra number (e.g. 2.1.1) first."; return; }
      box.innerHTML = `<form class="pk-askform no-print"><div class="pk-ask-h"><b>✎ ${esc(sid)}</b> <span class="muted">· whole derivation: ${esc(d.title || "")}</span></div>
        <select name="kind"><option value="solution">समाधान · this sūtra is needed here</option><option value="question">प्रश्न · question</option><option value="doubt">संशय · doubt</option><option value="note">टिप्पणी · note</option></select>
        <textarea name="text" rows="3" required placeholder="Why this sūtra should act here (which condition is met)…"></textarea>
        <textarea name="support" rows="3" placeholder="Supporting material: Kāśikā / Bhāṣya / vārttika / pāṭha / teacher, with reference…"></textarea>
        <button type="submit">Save under ${esc(sid)}</button> <button type="button" data-x="1">Cancel</button> <span class="pk-ask-msg muted"></span></form>`;
      const f = box.firstChild; f.text.focus();
      f.addEventListener("click", ev => { if (ev.target.dataset.x) box.innerHTML = ""; });
      f.addEventListener("submit", async ev => {
        ev.preventDefault(); const m = f.querySelector(".pk-ask-msg");
        const hit = t.findIndex(x => x.sutra_id === sid), at = hit >= 0 ? hit : t.length - 1;
        const text = f.text.value + (f.support.value.trim() ? "\n\nSupporting material:\n" + f.support.value.trim() : "");
        const where = `${d.title || ""} · "why didn't ${sid} apply?" (${hit >= 0 ? "step #" + (hit + 1) : "never offered"}) · ${location.pathname}${location.search}`;
        try {
          const r = await fetch("/api/notes/" + encodeURIComponent(sid), {method: "POST", headers: {"Content-Type": "application/json"},
            body: JSON.stringify({text, kind: f.kind.value, author: "me", derivation: where, trace: traceText(d, t, at)})});
          if (!r.ok) throw new Error(await r.text());
          NOTE_N = null; noteCounts();
          box.innerHTML = `<span class="muted">Saved under ${esc(sid)} — <a href="/sutra/${esc(sid)}#sutra-notes" target="_blank">open the sūtra page</a></span>`;
        } catch (err) { m.textContent = "Save failed: " + String(err.message).slice(0, 120); }
      });
    });
    q(".pk-inspect-out").addEventListener("toggle", async e => {      // lazy: the Kāśikā on this sūtra, shown for teaching (the engine never reads it)
      const dt = e.target; if (!dt.classList || !dt.classList.contains("pk-kas") || !dt.open || dt.dataset.done) return; dt.dataset.done = "1";
      const box = dt.querySelector(".pk-kas-b");
      try { const r = await fetch("/api/kashika/" + encodeURIComponent(dt.dataset.sid)); const j = await r.json(); box.textContent = j.text || j.error || "—"; }
      catch (err) { box.textContent = "unavailable"; }
    }, true);
    q(".pk-sid-in").addEventListener("input", e => { q(".pk-inspect-out").innerHTML = inspect(t, e.target.value); });
    const fullToggle = on => { el.classList.toggle("pk-full", on); document.body.classList.toggle("pk-noscroll", on); q("#pk-full").textContent = on ? "✕ Close full page" : "⛶ Full page"; };
    q("#pk-full").onclick = () => fullToggle(!el.classList.contains("pk-full"));
    document.addEventListener("keydown", e => { if (e.key === "Escape" && el.classList.contains("pk-full")) fullToggle(false); });
    q("#pk-print").onclick = () => window.print();
    q("#pk-json").onclick = () => {
      const a = document.createElement("a");
      a.href = URL.createObjectURL(new Blob([JSON.stringify(d, null, 1)], {type: "application/json"}));
      a.download = "prakriya.json"; a.click();
    };
    const flash = (btn, ok) => { const o = btn.textContent; btn.textContent = ok ? "Copied ✓" : "Copy failed"; setTimeout(() => { btn.textContent = o; }, 1600); };
    const clip = async (text, btn) => {
      try {
        if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(text);
        else {
          const ta = document.createElement("textarea"); ta.value = text; ta.style.cssText = "position:fixed;left:-9999px";
          document.body.appendChild(ta); ta.select(); document.execCommand("copy"); ta.remove();
        }
        flash(btn, true);
      } catch (e) { flash(btn, false); }
    };
    const panelDump = () => {
      const bits = [".pk-result", ".pk-letters", ".pk-letter-info", ".pk-legend", ".pk-ledger-box", ".pk-count", ".pk-list"]
        .map(sel => q(sel)).filter(n => n && n.innerText && n.innerText.trim())
        .map(n => n.innerText.trim());
      return bits.join("\n\n");
    };
    q("#pk-copy").onclick = () => clip(plainPrakriya(d, t, ctx, panelDump), q("#pk-copy"));
    q("#pk-copy-llm").onclick = () => clip(llmPrakriyaPrompt(d, t, ctx, panelDump), q("#pk-copy-llm"));
    const repaint = () => { if (!el.isConnected) window.removeEventListener("prakriya-change", repaint); else paint(); };
    window.addEventListener("prakriya-change", repaint);
    paint();
  }

  /* Full panel dump: vivakṣā header + visible panel text + structured steps (incl. 3.4.78 tin menu). */
  function plainPrakriya(d, t, ctx, panelTextFn) {
    const depth = {beginner: "आरम्भिकः / Beginner", kaumudi: "कौमुदी / Kaumudī", shastriya: "शास्त्रीयः / Śāstrīya"}[pref.depth] || pref.depth;
    const surface = d.surface ? `${d.surface.dev || ""} (${d.surface.slp1 || ""})` : "";
    const viv = ctx && ctx.viv;
    const lines = [
      `Pāṇini Engine v3 — prakriyā (entire panel)`,
      `Legend: numbered steps = the engine's own trace rows (sūtra id + status). [PED] = a teaching aid added by the web page (not Pāṇini's sequence, not engine output). [STRUCTURAL] = engine bookkeeping, not a sūtra.`,
      `Title: ${d.title || "—"}`,
      `Surface: ${surface}`,
      `Depth: ${depth} · Script: ${pref.script} · Gloss: ${pref.gloss}`,
    ];
    if (viv) {
      lines.push(`Vivakṣā: lakāra=${viv.lakara || "—"} · prayoga=${viv.prayoga || "—"} · pada=${viv.pada || "—"} · puruṣa=${viv.purusha || "—"} · vacana=${viv.vacana || "—"}`);
    }
    lines.push("");
    if (typeof panelTextFn === "function") {
      const panel = panelTextFn();
      if (panel) {
        lines.push("===== PANEL (as shown) =====");
        lines.push(panel);
        lines.push("===== END PANEL =====");
        lines.push("");
      }
    }
    const led = t.map((s, i) => ({s, i})).filter(({s}) => s.sutra_id === "1.3.9" && changes(s)).map(({s, i}) => ({i, r: itParse(s)})).filter(x => x.r);
    if (led.length) {
      lines.push("[PED] इत्संज्ञा-कोशः (summary table built by the page from the 1.3.2–1.3.9 steps; links = step numbers of the full trace)");
      lines.push("उपदेशः | इत्-वर्णाः → संज्ञा (सूत्रम्) | लोप-पदम्");
      led.forEach(({i, r}) => lines.push(`  ${r.upadesha} | ${r.items.map(x => `${x.letter} → ${x.name} ${x.sutra}`).join(" · ")} | #${i + 1}`));
      lines.push("");
    }
    const _u = itUnits(t).filter(x => !led.some(({r}) => devOf(x.u) === r.upadesha));
    if (_u.length) {
      lines.push("[PED] upadeśa units with no 1.3.9 step in this trace (from the trace's parts; ⚠ = form grew with no it-steps: an augment / ādeśa the engine put in without 1.3.2–1.3.9, ledger S174)");
      _u.forEach(x => lines.push(`  ${x.grown.length ? "⚠ " : ""}${devOf(x.u)} (${x.role})${x.grown.length ? " " + x.grown.map(g => `${g.from} → ${g.to} @#${g.i + 1} ${g.sid}`).join("; ") : ""}`));
      lines.push("");
    }
    if (d.letters && d.letters.length) {
      lines.push("[PED] Letters / वर्ण-उत्पत्तिः (page overlay built from the trace)");
      d.letters.forEach((l, n) => lines.push(`  ${n + 1}. ${fmt(l.slp1, "")} ← ${(l.origin || []).join(", ") || "upadeśa (given)"}`));
      lines.push("");
    }
    if ((pref.hidden || []).length) lines.push(`(Hidden on screen by the user, but listed below in full: ${pref.hidden.join(", ")})`);
    lines.push(`Steps (${pref.depth}) — structured:`);
    rowsFor(t).forEach(({s, i, group}) => {
      if (group) {
        const lopa = [...group].reverse().find(x => x.sutra_id === "1.3.9" && changes(x));
        const named = [...new Set(group.filter(x => x.sutra_id !== "1.3.9").map(x => x.sutra_id))];
        const tag = `${named.join(" · ") || "1.3.2–1.3.8"} → 1.3.9`;
        lines.push(`#${i + 1} इत्संज्ञा-लोपः ${tag}  [PED: grouped display of the 1.3.2–1.3.9 steps; Śāstrīya depth lists each]`);
        if (lopa) {
          lines.push(`  ${lopa.form_before_dev || fmt(lopa.form_before)} → ${lopa.form_after_dev || fmt(lopa.form_after)}`);
          lines.push(`  SLP1: ${lopa.form_before} → ${lopa.form_after}`);
          const r = itParse(lopa);
          if (r) lines.push(`  उपदेशः ${r.upadesha} · ${r.items.map(x => `${x.letter} → ${x.name} (${x.sutra})`).join(", ")}`);
          lines.push(`  ${(lopa.why_now_dev || lopa.why_dev || "").trim()}`);
        }
        return;
      }
      const st = STATUS[s.status] || [s.status, s.status];
      lines.push(`#${i + 1} ${s.sutra_id} [${st[0]} / ${st[1]}]${s.sutra_type ? ` · ${s.sutra_type}` : ""}${isStruct(s) ? "  [STRUCTURAL — engine bookkeeping, not a sūtra]" : ""}`);
      lines.push(`  ${s.form_before_dev || fmt(s.form_before)} → ${s.form_after_dev || fmt(s.form_after)}`);
      lines.push(`  SLP1: ${s.form_before} → ${s.form_after}`);
      if (s._sutra_text_dev) lines.push(`  pāṭha: ${s._sutra_text_dev}`);
      if (s._padaccheda_dev) lines.push(`  padaccheda: ${s._padaccheda_dev}`);
      if ((s._anuvritti_from || []).length) lines.push(`  anuvṛtti ← ${(s._anuvritti_from || []).join(", ")}`);
      const g = gloss(s); if (g) lines.push(`  ${pedGloss(s) ? "[PED gloss] " : ""}${g}`);
      if (s.why_now_dev && s.why_now_dev !== g) lines.push(`  why_now: ${s.why_now_dev}`);
      if (s.why_dev && s.why_dev !== g && s.why_dev !== s.why_now_dev) lines.push(`  why: ${s.why_dev}`);
      if (s.gate_reason) lines.push(`  gate: ${s.gate_reason}`);
      if (s.skip_reason) lines.push(`  skip: ${s.skip_reason}`);
      if (s.parts) lines.push(`  parts: ${typeof s.parts === "string" ? s.parts : JSON.stringify(s.parts)}`);
      if (s.sutra_id === "3.4.78" && /^APPLIED/.test(s.status)) {
        const chosen = s._tin_chosen || chosenTin(s);
        lines.push(`  [PED] 3.4.78 tiṅ menu (a student's table; the sūtra only substitutes the chosen ādeśa) — chosen: ${chosen || "—"}`);
        ["parasmai", "atmane"].forEach(pd => {
          lines.push(`  [${TIN78.pada[pd][0]}]`);
          [3, 2, 1].forEach((pui, ri) => {
            const row = [1, 2, 3].map((vci, ci) => {
              const [sl, dv] = TIN78[pd][ri * 3 + ci];
              const hit = sl === chosen ? " ★" : "";
              return `${dv}(${sl})${hit}`;
            }).join(" | ");
            lines.push(`    ${TIN78.pu[pui][0]}: ${row}`);
          });
        });
      }
    });
    lines.push("");
    lines.push(`Engine totals: ${t.length} rule checks; ${t.filter(applied).length} applied.` +
      (pref.depth !== "shastriya" ? " (Switch depth to Śāstrīya for SKIPPED/BLOCKED/AUDIT rows.)" : ""));
    return lines.join("\n");
  }

  function llmPrakriyaPrompt(d, t, ctx, panelTextFn) {
    const body = plainPrakriya(d, t, ctx, panelTextFn);
    return `Act as a Pāṇini Aṣṭādhyāyī expert and a strict, fair auditor of a computational prakriyā engine (Panini Engine v3).

HOW TO READ THE DUMP (so you do not mistake the page for the engine):
- ENGINE OUTPUT = the numbered steps "#n <sūtra id> [status]". These come from the engine's own trace; "#n" is the stable index into the FULL trace (all depths use the same numbers).
- Lines tagged [PED] are TEACHING AIDS added by the web page for students (letter chips, colours, saṃjñā targets, the 3.4.78 tiṅ menu, the इत्संज्ञा-कोश summary table, English/Hindi glosses, grouped it-rows). They are NOT engine output and NOT Pāṇini's sequence. Never report a [PED] item as an engine defect, and do not treat it as evidence of what the engine did.
- [STRUCTURAL] = engine bookkeeping (for example merging the parts into one pada before the Tripādī), explicitly not a sūtra.
- Depth matters. Beginner/Kaumudī views hide checked, skipped, blocked and audit rows and group the it-saṃjñā steps 1.3.2–1.3.9 into one row; absence of such a row in those views is NOT a missing step. Judge omissions only against Śāstrīya depth, or say that the depth cannot show it.
- The sūtra texts, padacchedas and anuvṛtti shown come from the engine's registry; check them against the Kāśikā/Aṣṭādhyāyī and report errors.

Engine principles you may audit against (summary of AGENTS.md / CONSTITUTION.md; the numbering below is only for this prompt):
1. Glass box: every change is made by a sūtra through apply_rule; a step the engine performs without a sūtra is a recorded gap, not code.
2. cond() reads the linguistic state only (never the target form, a lookup table of vivakṣā, or reference data); a table that picks the tiṅ from (lakāra, puruṣa, vacana) is a known, ledgered shortcut.
3. One sūtra = one operation; the Aṣṭādhyāyī's own order (para, apavāda, tripādī asiddhatva) decides conflicts, not the Kaumudī sequence.
4. it-saṃjñā (1.3.2–1.3.8) and tasya lopaḥ (1.3.9) should be shown for every upadeśa, āgama and ādeśa that carries it-letters; an augment shown without them is a gap.
5. Vidyut or other external engines are only a minimum-rule floor for comparison, never an authority; the Aṣṭādhyāyī and its Kāśikā decide.

Task:
- Critically analyse the dump below against the Aṣṭādhyāyī (with the Kāśikā and standard udāharaṇa) and the principles above.
- Say what is correctly followed.
- List weaknesses, gaps, wrong order, missing it-kārya, or non-Pāṇinian shortcuts: numbered, concrete, with sūtra ids and step numbers (#n). For each, say whether it is an engine defect, or only a display/depth artefact, or a [PED] page issue.
- Quote the sūtra text when you claim a rule was misapplied; do not rely on memory of numbering alone.
- End with a short severity summary (blocker / major / minor).

Do not rewrite the engine; audit only.

===== PRAKRIYĀ DUMP =====
${body}
===== END =====
`;
  }

  return {mount, vidyutLlmText, copyText, noteForm, outBtn, wireOutNotes, pref, fmt, rowsFor, inspect, plainPrakriya, llmPrakriyaPrompt};
})();
