/* अभ्यासशाला — the /practice tab. sanskritabhyas.in's drills and lists, every answer from /api/abhyasa/* (core/abhyasa.py):
   the engine's form, agreed with Vidyut and/or the printed paradigm; the sources travel with each answer as badges.
   Plan: docs/ABHYASA_PLAN.md. Progress, options and favourites live in localStorage only. */
(() => {
  const $ = id => document.getElementById(id);
  const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]));
  const post = (u, b) => fetch(u, {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(b)}).then(r => r.json());
  const get = u => fetch(u).then(r => r.json());
  const pick = a => a[Math.floor(Math.random() * a.length)];
  const KEY = "abhyasa.v1";
  let CAT = null, cur = null;
  let S = {fam: "noun", view: "practice", opts: {}, score: {}, fav: [], cmp: [], scale: 1, lang: "hi"};
  try { S = {...S, ...JSON.parse(localStorage.getItem(KEY) || "{}")}; } catch (e) {}
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} };

  const T = {
    hi: {sub: "हर उत्तर हमारे यन्त्र से सिद्ध — विद्युत् और मुद्रित रूपों से जाँचा", v_practice: "अभ्यास", v_list: "सूचियाँ", v_compare: "तुलना",
         v_fav: "पसंदीदा ★", v_pratyaya: "प्रत्यय", next: "नया प्रश्न", check: "उत्तर जांचें", show: "उत्तर दिखाएं", full: "पूर्ण रूप दिखाएं",
         why: "प्रक्रिया (सूत्र-क्रम)", fav: "पसंदीदा में जोड़ें", options: "विकल्प", level: "कठिनाई का स्तर", drills: "अभ्यास",
         right: "सही ✓", wrong: "गलत ✗", answer: "उत्तर", search: "खोजें", practiceThis: "इस शब्द का अभ्यास", addCmp: "तुलना में जोड़ें",
         empty: "अभी कुछ नहीं", fallback: "जहाँ यन्त्र अभी न्यून है वहाँ विद्युत्-रूप भी", loading: "यन्त्रेण सिध्यति…"},
    en: {sub: "every answer is derived by our engine, checked with Vidyut and the printed paradigms", v_practice: "Practice", v_list: "Lists",
         v_compare: "Compare", v_fav: "Favourites ★", v_pratyaya: "Pratyayas", next: "New question", check: "Check", show: "Show answer",
         full: "Show full table", why: "Derivation (sūtra by sūtra)", fav: "Add to favourites", options: "Options", level: "Difficulty",
         drills: "Drills", right: "Correct ✓", wrong: "Not quite ✗", answer: "Answer", search: "Search", practiceThis: "Practise this word",
         addCmp: "Add to comparison", empty: "Nothing yet", fallback: "Use Vidyut's forms where the engine is not ready yet", loading: "deriving…"},
    sa: {sub: "प्रत्युत्तरं यन्त्रेण सिद्धं, विद्युता मुद्रितरूपैश्च परीक्षितम्", v_practice: "अभ्यासः", v_list: "सूच्यः", v_compare: "तुलना",
         v_fav: "प्रियाणि ★", v_pratyaya: "प्रत्ययाः", next: "नूतनः प्रश्नः", check: "परीक्ष्यताम्", show: "उत्तरं दर्श्यताम्", full: "पूर्णरूपाणि",
         why: "प्रक्रिया", fav: "प्रियेषु योज्यताम्", options: "विकल्पाः", level: "स्तरः", drills: "अभ्यासप्रकाराः", right: "सम्यक् ✓",
         wrong: "न सम्यक् ✗", answer: "उत्तरम्", search: "अन्विष्यताम्", practiceThis: "अस्य शब्दस्य अभ्यासः", addCmp: "तुलनायां योज्यताम्",
         empty: "किमपि नास्ति", fallback: "यत्र यन्त्रं न्यूनं तत्र विद्युद्रूपाणि अपि", loading: "सिध्यति…"},
  };
  const t = k => (T[S.lang] || T.hi)[k] || T.hi[k] || k;
  const SRC = {engine: "यन्त्रम्", vidyut: "विद्युत्", corpus: "मुद्रितम्", "vidyut-lipi": "विद्युत्-लिपिः"};
  const badges = srcs => !srcs || !srcs.length ? "" : `<span class="ab-src" title="answer sources">${srcs.map(s => `<span class="${esc(s)}">${esc(SRC[s] || s)}</span>`).join("")}${srcs.includes("engine") ? "" : `<span class="only">यन्त्रं न्यूनम्</span>`}</span>`;
  const D = s => Transliterate.fromSLP1(s || "", "devanagari");
  const norm = s => (s || "").normalize("NFC").replace(/[\s'ऽ।॥,.]/g, "");
  const toSlp = txt => { txt = (txt || "").trim(); if (!txt) return ""; try { return /[ऀ-ॿ]/.test(txt) ? Transliterate.toSLP1(txt, "devanagari") : Transliterate.toSLP1(txt, $("sch").value === "devanagari" ? "slp1" : $("sch").value); } catch (e) { return txt; } };
  const same = (got, accepted) => accepted.some(a => norm(a) === norm(got));
  const opt = fam => (S.opts[fam] = S.opts[fam] || {levels: [1], drills: [], filters: {}});

  function tally(ok) {
    const s = S.score[S.fam] = S.score[S.fam] || {n: 0, ok: 0, streak: 0};
    s.n++; if (ok) { s.ok++; s.streak++; } else s.streak = 0; save(); score();
  }
  function score() {
    const s = S.score[S.fam]; $("score").textContent = s ? `${s.ok} / ${s.n}${s.streak > 2 ? ` · 🔥${s.streak}` : ""}` : "";
  }
  function applyChrome() {
    document.documentElement.style.setProperty("--ab-scale", S.scale);
    document.querySelectorAll("[data-l]").forEach(el => { el.textContent = t(el.dataset.l); });
    $("ui-lang").value = S.lang;
  }

  // ── shell ──────────────────────────────────────────────────────────────────────────────────────
  function fams() {
    $("fams").innerHTML = CAT.family_order.map(k => [k, CAT.families[k]]).map(([k, f]) =>
      `<button role="tab" data-f="${k}" class="${k === S.fam ? "on" : ""}" title="${esc(f.en)}">${esc(f.dev)}</button>`).join("");
    $("fams").querySelectorAll("button").forEach(b => b.onclick = () => { S.fam = b.dataset.f; save(); fams(); render(); });
  }
  document.querySelectorAll(".ab-views button[data-v]").forEach(b => b.onclick = () => {
    S.view = b.dataset.v; save();
    document.querySelectorAll(".ab-views button[data-v]").forEach(x => x.classList.toggle("on", x === b)); render();
  });
  $("fs-").onclick = () => { S.scale = Math.max(.8, +(S.scale - .1).toFixed(1)); save(); applyChrome(); };
  $("fs+").onclick = () => { S.scale = Math.min(1.8, +(S.scale + .1).toFixed(1)); save(); applyChrome(); };
  $("ui-lang").onchange = e => { S.lang = e.target.value; save(); applyChrome(); render(); };

  function render() {
    $("why").hidden = true; score();
    document.querySelectorAll(".ab-views button[data-v]").forEach(x => x.classList.toggle("on", x.dataset.v === S.view));
    ({practice: viewPractice, list: viewList, compare: viewCompare, fav: viewFav, pratyaya: viewPratyaya, search: viewSearch}[S.view] || viewPractice)();
  }

  // ── options panel (विकल्प), as sanskritabhyas: level, drill types, family filters ───────────────
  function sel(name, items, val, any = true) {
    return `<select data-f="${name}">${any ? `<option value="">— कोई भी —</option>` : ""}${items.map(([v, l]) => `<option value="${esc(v)}" ${String(val ?? "") === String(v) ? "selected" : ""}>${esc(l)}</option>`).join("")}</select>`;
  }
  function optsPanel() {
    const o = opt(S.fam), f = o.filters, fam = S.fam, C = CAT;
    const drills = C.families[fam].drills;
    let h = `<h3 style="margin:.2rem 0" data-l="options">${t("options")}</h3>
      <label>${t("level")}</label><div class="chk">${C.levels.map(l => `<label><input type="checkbox" data-lv="${l.id}" ${o.levels.includes(l.id) ? "checked" : ""}>${esc(S.lang === "en" ? l.en : l.hi)}</label>`).join("")}</div>
      <label>${t("drills")}</label><div class="chk">${drills.map(d => `<label><input type="checkbox" data-dr="${d}" ${(!o.drills.length || o.drills.includes(d)) ? "checked" : ""}>${esc(S.lang === "en" ? C.drills[d].en : C.drills[d].hi)}</label>`).join("")}</div>`;
    const lingas = Object.entries(C.linga);
    if (["noun", "pronoun", "number"].includes(fam)) {
      h += `<label>लिङ्गम्</label>${sel("linga", lingas, f.linga)}`;
      if (fam !== "number") h += `<label>विभक्तिः</label>${sel("vibhakti", C.vibhakti.slice(1, 8).map((v, i) => [i + 1, v]), f.vibhakti)}`;
      if (fam !== "pronoun") h += `<label>अन्तः</label>${sel("anta", [["ajanta", "अजन्तः"], ["halanta", "हलन्तः"]], f.anta)}
        <label>केवल (अन्त्य-वर्णः)</label>${sel("anta_letter", "a A i I u U f o O k c j t d n p B m r l v S z s h".split(" ").map(x => [x, D(x)]), f.anta_letter)}`;
      if (fam === "noun") h += `<label>शब्दः (SLP1/देवनागरी)</label><input type="text" data-f="stem" value="${esc(f.stem || "")}">`;
    }
    if (fam === "verb" || fam === "krdanta") {
      h += `<label>गणः</label>${sel("gana", C.gana.slice(1).map((g, i) => [i + 1, g]), f.gana)}
        <label>उपसर्गः</label>${sel("upasarga", [["any", "कोई भी"], ...C.upasarga.map(u => [u.slp1, u.dev])], f.upasarga)}
        <label>सनादि प्रत्ययः</label>${sel("sanadi", [["any", "कोई भी"], ...Object.entries(C.sanadi)], f.sanadi)}
        <label><input type="checkbox" data-f="popular" ${f.popular !== false ? "checked" : ""}> केवल लोकप्रिय धातु</label>`;
    }
    if (fam === "verb") {
      h += `<label>प्रयोगः</label>${sel("prayoga", Object.entries(C.prayoga), f.prayoga)}
        <label>पदम्</label>${sel("pada", [["parasmai", "परस्मैपदम्"], ["atmane", "आत्मनेपदम्"]], f.pada)}
        <label>लकारः</label><div class="chk">${Object.entries(C.lakara).map(([k, v]) => `<label><input type="checkbox" data-lak="${k}" ${(f.lakara || []).includes(k) ? "checked" : ""}>${esc(v)}</label>`).join("")}</div>
        <label>धातुः (id / उपदेशः)</label><input type="text" data-f="dhatu" value="${esc(f.dhatu || "")}">`;
    }
    if (fam === "taddhita") h += `<label>प्रत्ययः</label>${sel("pratyaya", Object.entries(C.taddhita), f.pratyaya)}`;
    if (fam === "namadhatu") h += `<label>लकारः</label>${sel("lakara", Object.entries(C.lakara), f.lakara, false)}`;
    if (fam === "sandhi") h += `<label>सन्धिः</label>${sel("rule", C.sandhi_rules, f.rule)}`;
    if (fam === "varna") h += `<label>प्रकारः</label>${sel("mode", [["svara", "स्वरयुक्त व्यञ्जन"], ["samyukta", "संयुक्त व्यञ्जन"], ["lipi", "लिपिः"]], f.mode)}
        <label>लिपिः</label>${sel("lipi", Object.entries(C.lipi), f.lipi)}`;
    if (fam === "vakya") h += `<label>पाठः</label>${sel("lesson", C.vakya_lessons.map(L => [L.id, `${L.deva} — ${L.title} (${L.n})`]), f.lesson)}`;
    if (["noun", "pronoun", "number", "verb"].includes(fam)) h += `<label><input type="checkbox" data-f="vidyut_fallback" ${f.vidyut_fallback ? "checked" : ""}> ${t("fallback")}</label>`;
    h += `<p class="muted" style="font-size:12px;margin-top:.8rem">${CAT.vidyut ? "विद्युत् ✓" : "विद्युत् ✗ (.venv missing — only engine + printed forms)"} · bank ${esc(CAT.bank.engine_commit || "—")}</p>`;
    return h;
  }
  function wireOpts(box) {
    const o = opt(S.fam);
    box.querySelectorAll("[data-lv]").forEach(c => c.onchange = () => { o.levels = [...box.querySelectorAll("[data-lv]:checked")].map(x => +x.dataset.lv); if (!o.levels.length) o.levels = [1]; save(); ask(); });
    box.querySelectorAll("[data-dr]").forEach(c => c.onchange = () => { o.drills = [...box.querySelectorAll("[data-dr]:checked")].map(x => x.dataset.dr); save(); ask(); });
    box.querySelectorAll("[data-lak]").forEach(c => c.onchange = () => { o.filters.lakara = [...box.querySelectorAll("[data-lak]:checked")].map(x => x.dataset.lak); save(); ask(); });
    box.querySelectorAll("[data-f]").forEach(c => c.onchange = () => {
      let v = c.type === "checkbox" ? c.checked : c.value;
      if (c.dataset.f === "stem" && v) v = toSlp(v);
      o.filters[c.dataset.f] = v; save(); ask();
    });
  }

  // ── practice ─────────────────────────────────────────────────────────────────────────────────
  function viewPractice() {
    $("view").innerHTML = `<div class="ab-grid"><div class="ab-card" id="qcard" aria-live="polite"></div><aside class="ab-card ab-side" id="opts"></aside></div>`;
    $("opts").innerHTML = optsPanel(); wireOpts($("opts")); ask();
  }

  async function ask() {
    const o = opt(S.fam), drills = CAT.families[S.fam].drills.filter(d => !o.drills.length || o.drills.includes(d));
    const drill = pick(drills.length ? drills : CAT.families[S.fam].drills), level = pick(o.levels.length ? o.levels : [1]);
    $("why").hidden = true;
    $("qcard").innerHTML = `<p class="muted">${t("loading")}</p>`;
    const q = await post("/api/abhyasa/question", {family: S.fam, drill, level, filters: o.filters, seed: Math.floor(Math.random() * 1e9)});
    if (q.error) { $("qcard").innerHTML = `<p class="ab-note">${esc(q.error)}</p>${btns({})}`; wireBtns(); return; }
    cur = {q, done: false};
    const head = `<div class="ab-drill">${esc(S.lang === "en" ? CAT.drills[q.drill].en : CAT.drills[q.drill].hi)} · ${esc((CAT.levels[q.level - 1] || {}).hi || "")}</div>
      <div class="ab-title">${esc(q.title || "")} ${q.paradigm && q.paradigm.stem ? `<button class="ab-star" id="star" title="${t("fav")}">${isFav(q.paradigm) ? "★" : "☆"}</button>` : ""}</div>
      ${q.note ? `<p class="ab-note">${esc(q.note)}</p>` : ""}`;
    $("qcard").innerHTML = head + `<div id="qbody"></div><div id="fb" class="ab-fb"></div>` + btns(q);
    ({mcq: drawChoice, recall: drawRecall, tf: drawTF, match: drawMatch, odd: drawOdd, table: drawTable, sutra: drawSutra,
      compose: drawCompose, karaka: drawKaraka}[q.drill] || drawChoice)(q);
    wireBtns();
    if ($("star")) $("star").onclick = () => { toggleFav(q.paradigm); $("star").textContent = isFav(q.paradigm) ? "★" : "☆"; };
  }

  function btns(q) {
    const canFull = q.paradigm && (q.paradigm.rows || []).length;
    const canWhy = (q.cell && q.paradigm && ["subanta", "tinanta"].includes(q.paradigm.kind)) || (q.steps || []).length > 0;
    return `<div class="ab-btns"><button class="go" id="b-check">${t("check")}</button><button id="b-show">${t("show")}</button>
      ${canFull ? `<button id="b-full">${t("full")}</button>` : ""}${canWhy ? `<button id="b-why">${t("why")}</button>` : ""}
      <button id="b-next">${t("next")} →</button></div>`;
  }
  function wireBtns() {
    const on = (id, fn) => { const b = $(id); if (b) b.onclick = fn; };
    on("b-next", ask); on("b-check", () => cur && cur.check && cur.check()); on("b-show", () => cur && cur.show && cur.show());
    on("b-full", () => showTable(cur.q.paradigm, $("why"))); on("b-why", () => explain(cur.q));
  }
  const finish = (ok, html) => { if (!cur.done) tally(ok); cur.done = true;
    $("fb").innerHTML = `<span class="${ok ? "ok" : "no"}">${ok ? t("right") : t("wrong")}</span> ${html || ""}`; };
  const answerLine = q => `${t("answer")}: <b class="dev">${esc((q.accepted_dev || []).join(" / "))}</b>${badges(q.sources)}`;

  function drawChoice(q) {
    $("qbody").innerHTML = `<div class="ab-prompt ${q.prompt_is_glyph ? "ab-glyph" : ""}">${esc(q.prompt)}</div>
      <div class="ab-opts">${q.options.map((o, i) => `<button class="ab-opt" data-i="${i}">${esc(o.dev)}${o.glyph ? ` <small>${esc(o.glyph)}</small>` : ""}</button>`).join("")}</div>`;
    let chosen = null;
    $("qbody").querySelectorAll(".ab-opt").forEach(b => b.onclick = () => { chosen = q.options[+b.dataset.i];
      $("qbody").querySelectorAll(".ab-opt").forEach(x => x.classList.toggle("sel", x === b)); cur.check(); });
    const good = o => (q.accepted || []).length ? same(o.slp1, q.accepted) : (q.accepted_dev || []).includes(o.dev);
    cur.check = () => { if (!chosen) return;
      $("qbody").querySelectorAll(".ab-opt").forEach((x, i) => { const o = q.options[i]; x.classList.toggle("good", good(o)); if (o === chosen && !good(o)) x.classList.add("bad");
        if (o.labels && o.labels.length) x.insertAdjacentHTML("beforeend", `<small>${esc(o.labels.join(" / "))}</small>`); });
      finish(good(chosen), answerLine(q) + (q.explain ? ` — ${esc(q.explain)}` : "") + (q.its ? itNote(q) : "")); };
    cur.show = () => { $("qbody").querySelectorAll(".ab-opt").forEach((x, i) => x.classList.toggle("good", good(q.options[i]))); cur.done = true;
      $("fb").innerHTML = answerLine(q) + (q.its ? itNote(q) : ""); };
  }
  const itNote = q => `<ul class="ab-steps">${q.its.map(r => `<li>${esc(r.letters_dev)} — <a href="/sutra/${esc(r.sutra)}">${esc(r.sutra)}</a> ${esc(r.name_dev)}</li>`).join("")}</ul> शेषः: <b>${esc(q.residue_dev)}</b>`;

  function drawRecall(q) {
    $("qbody").innerHTML = `<div class="ab-prompt">${esc(q.prompt)}</div><form id="rf"><input id="ans" class="ab-in" autocomplete="off" spellcheck="false" aria-label="${t("answer")}"></form>`;
    $("ans").focus(); $("rf").onsubmit = e => { e.preventDefault(); cur.check(); };
    cur.check = () => { const v = $("ans").value; if (!v.trim()) return;
      let ok;
      if (q.set_answer) { const got = new Set(v.trim().split(/[\s,]+/).map(toSlp)); ok = got.size === q.set_answer.length && q.set_answer.every(x => got.has(x)); }
      else if (q.accepted && q.accepted.length) ok = same(toSlp(v), q.accepted);
      else ok = (q.accepted_dev || []).some(a => norm(a) === norm(/[ऀ-ॿ]/.test(v) ? v : D(toSlp(v))));
      $("ans").className = "ab-in " + (ok ? "good" : "bad"); finish(ok, answerLine(q) + (q.its ? itNote(q) : "")); };
    cur.show = () => { cur.done = true; $("fb").innerHTML = answerLine(q) + (q.its ? itNote(q) : ""); };
  }

  function drawTF(q) {
    $("qbody").innerHTML = `<div class="ab-tf">${q.statements.map((s, i) => `<div>${esc(s.label)} = <b>${esc(s.form.dev)}</b> <span class="res" id="tf${i}"></span></div>
      <div class="bt" data-i="${i}"><button data-v="1">सही</button><button data-v="0">गलत</button></div>`).join("")}</div>`;
    const ans = {};
    $("qbody").querySelectorAll(".bt").forEach(d => d.querySelectorAll("button").forEach(b => b.onclick = () => {
      ans[d.dataset.i] = b.dataset.v === "1"; d.querySelectorAll("button").forEach(x => x.classList.toggle("on", x === b)); }));
    const mark = reveal => q.statements.map((s, i) => { const ok = ans[i] === s.answer;
      $("tf" + i).className = "res " + (reveal || ok ? "good" : "bad");
      $("tf" + i).innerHTML = (ok ? "✓" : "✗") + (s.answer ? "" : ` → ${esc(s.correct_dev)}`) + badges(s.sources); return ok; });
    cur.check = () => { if (Object.keys(ans).length < q.statements.length) return; const r = mark(false); finish(r.every(Boolean), `${r.filter(Boolean).length} / ${r.length}`); };
    cur.show = () => { q.statements.forEach((s, i) => ans[i] = s.answer); mark(true); cur.done = true; };
  }

  function drawMatch(q) {
    const forms = q.pairs.map(p => p.form);
    $("qbody").innerHTML = `<div class="ab-match"><div>${forms.map((f, i) => `<button class="ab-opt" data-a="${i}">${esc(f.dev)}</button>`).join("")}</div>
      <div>${q.labels.map((l, i) => `<button class="ab-opt" data-b="${i}" style="font-size:15px">${esc(l)}</button>`).join("")}</div></div>`;
    const pairs = {}; let a = null;
    $("qbody").querySelectorAll("[data-a]").forEach(b => b.onclick = () => { a = +b.dataset.a; $("qbody").querySelectorAll("[data-a]").forEach(x => x.classList.toggle("sel", x === b)); });
    $("qbody").querySelectorAll("[data-b]").forEach(b => b.onclick = () => { if (a === null) return; pairs[a] = q.labels[+b.dataset.b];
      const fa = $("qbody").querySelector(`[data-a="${a}"]`); fa.querySelector("small")?.remove(); fa.insertAdjacentHTML("beforeend", `<small>→ ${esc(pairs[a])}</small>`); fa.classList.remove("sel"); a = null; });
    cur.check = () => { const r = q.pairs.map((p, i) => { const ok = pairs[i] === p.label; const el = $("qbody").querySelector(`[data-a="${i}"]`); el.classList.add(ok ? "good" : "bad"); return ok; });
      finish(r.every(Boolean), `${r.filter(Boolean).length} / ${r.length}`); };
    cur.show = () => { cur.done = true; q.pairs.forEach((p, i) => { const el = $("qbody").querySelector(`[data-a="${i}"]`); el.querySelector("small")?.remove(); el.insertAdjacentHTML("beforeend", `<small>= ${esc(p.label)}</small>`); el.classList.add("good"); }); };
  }

  function drawOdd(q) {
    $("qbody").innerHTML = `<div class="ab-prompt">${esc(CAT.drills.odd.hi)}</div><div class="ab-opts">${q.options.map((o, i) => `<button class="ab-opt" data-i="${i}">${esc(o.dev)}</button>`).join("")}</div>`;
    let chosen = null;
    const reveal = () => $("qbody").querySelectorAll(".ab-opt").forEach((x, i) => { const o = q.options[i]; x.insertAdjacentHTML("beforeend", `<small>${esc(o.label)}</small>`); x.classList.toggle("good", o.slp1 === q.answer); });
    $("qbody").querySelectorAll(".ab-opt").forEach(b => b.onclick = () => { chosen = q.options[+b.dataset.i]; cur.check(); });
    cur.check = () => { if (!chosen || cur.done) return; reveal(); finish(chosen.slp1 === q.answer, esc(q.reason)); };
    cur.show = () => { if (!cur.done) reveal(); cur.done = true; $("fb").innerHTML = esc(q.reason); };
  }

  function grid(p, cellHtml) {
    const k = p.kind, rows = p.rows || [];
    const key = (i, j) => k === "subanta" ? `${i + 1}-${j + 1}` : `${3 - i}-${j + 1}`;
    return `<table class="ab-tbl"><tr><th></th>${(p.cols || []).map(c => `<th>${esc(c)}</th>`).join("")}</tr>${rows.map((r, i) =>
      `<tr><th>${esc(r)}</th>${(p.cols || []).map((c, j) => `<td data-k="${key(i, j)}">${cellHtml(key(i, j))}</td>`).join("")}</tr>`).join("")}</table>`;
  }
  function drawTable(q) {
    const by = Object.fromEntries(q.cells.map(c => [c.key, c]));
    $("qbody").innerHTML = grid(q.paradigm, k => by[k] ? `<input data-c="${k}" autocomplete="off" spellcheck="false">` : "—");
    cur.check = () => { const r = q.cells.map(c => { const el = $("qbody").querySelector(`[data-c="${c.key}"]`); const ok = same(toSlp(el.value), c.accepted);
      el.style.background = ok ? "#eef7ee" : "#fbeeee"; if (!ok) el.title = c.accepted_dev.join(" / "); return ok; });
      finish(r.every(Boolean), `${r.filter(Boolean).length} / ${r.length}`); };
    cur.show = () => { cur.done = true; q.cells.forEach(c => { const el = $("qbody").querySelector(`[data-c="${c.key}"]`); el.value = c.accepted_dev.join(" / "); }); };
  }

  function drawSutra(q) {
    $("qbody").innerHTML = `<div class="ab-prompt">${esc(q.prompt || "")}${q.before_dev ? `: <b>${esc(q.before_dev)} → ${esc(q.after_dev)}</b>` : ""} — कः सूत्रः?</div>
      <div class="ab-opts">${q.options.map((o, i) => `<button class="ab-opt" data-i="${i}" style="font-size:16px"><b>${esc(o.sutra_id)}</b> ${esc(o.text_dev)}</button>`).join("")}</div>`;
    let chosen = null;
    $("qbody").querySelectorAll(".ab-opt").forEach(b => b.onclick = () => { chosen = q.options[+b.dataset.i]; cur.check(); });
    const line = () => `सूत्रम्: <a href="/sutra/${esc(q.answer_sutra)}">${esc(q.answer_sutra)}</a> ${esc((q.options.find(o => o.sutra_id === q.answer_sutra) || {}).text_dev || "")}${badges(q.sources)}`;
    cur.check = () => { if (!chosen || cur.done) return; $("qbody").querySelectorAll(".ab-opt").forEach((x, i) => x.classList.toggle("good", q.options[i].sutra_id === q.answer_sutra));
      finish(chosen.sutra_id === q.answer_sutra, line()); };
    cur.show = () => { cur.done = true; $("fb").innerHTML = line(); };
  }

  function drawCompose(q) {
    $("qbody").innerHTML = `<p class="muted">${esc(q.lesson.about)} ${q.lesson.sutras.map(s => `<a href="/sutra/${s}" title="${esc(q.lesson.sutra_text[s] || "")}">${s}</a>`).join(" ")}</p>
      <div class="ab-en">“${esc(q.en)}”</div><form id="cf"><input id="ans" class="ab-in" style="width:100%" autocomplete="off" spellcheck="false" placeholder="संस्कृतेन लिखत — words apart, no sandhi, any order"></form>`;
    $("ans").focus(); $("cf").onsubmit = e => { e.preventDefault(); cur.check(); };
    const table = r => `<p class="dev" style="font-size:20px">${esc(r.answer_dev)} ${badges(q.sources)}</p><table class="ab-tbl"><tr><th>पदम्</th><th>कारकम्</th><th>विभक्तिः / लकारः</th><th>सूत्राणि</th></tr>${r.words.map(w =>
      `<tr><td>${esc(w.form_dev)}${w.alts_dev.length > 1 ? ` <small>(${esc(w.alts_dev.join(" / "))})</small>` : ""}</td><td>${esc(w.role_dev)}</td><td>${esc(w.what)}</td><td>${w.sutras.map(s => `<a href="/sutra/${s.id}" title="${esc(s.text)}">${s.id}</a>`).join(" ")}</td></tr>`).join("")}</table>`;
    cur.check = async () => { const words = $("ans").value.split(/[\s।॥,]+/).filter(Boolean).map(toSlp); if (!words.length) return;
      const r = await post("/api/abhyasa/grade", {sentence_id: q.id, answer: words});
      const notes = `<ul class="ab-steps">${r.notes.map(n => n.status === "ok" ? `<li>✓ ${esc(n.got_dev)}</li>`
        : n.status === "wrong" ? `<li>✗ ${esc(n.got_dev)} = ${esc(n.got_is)}; the ${esc(n.role)} needs ${esc(n.need)} — ${n.sutras.map(s => `<a href="/sutra/${s.id}" title="${esc(s.text)}">${s.id}</a>`).join(" ")}</li>`
        : n.status === "missing" ? `<li>✗ missing: ${esc(n.role)} (${esc(n.need)})</li>` : `<li>✗ ${esc(n.got_dev)}: not needed here (${esc(n.got_is)})</li>`).join("")}</ul>`;
      finish(r.ok, notes + (r.ok ? "" : table(r))); };
    cur.show = async () => { const r = await post("/api/abhyasa/grade", {sentence_id: q.id, answer: []}); cur.done = true; $("fb").innerHTML = table(r); };
  }

  function drawKaraka(q) {
    $("qbody").innerHTML = `<div class="ab-en">${esc(q.sentence_dev)} <span class="muted">“${esc(q.en)}”</span></div>
      <div class="ab-prompt">${esc(q.word_dev)} — किं कारकम्?</div><div class="ab-opts">${q.options.map((o, i) => `<button class="ab-opt" data-i="${i}">${esc(o.dev)}<small>${esc(o.vibhakti)}</small></button>`).join("")}</div>`;
    let chosen = null;
    $("qbody").querySelectorAll(".ab-opt").forEach(b => b.onclick = () => { chosen = q.options[+b.dataset.i]; cur.check(); });
    const line = () => q.why.map(w => `<a href="/sutra/${w.sutra}">${w.sutra}</a> ${esc(w.text)}`).join(" · ");
    cur.check = () => { if (!chosen || cur.done) return; $("qbody").querySelectorAll(".ab-opt").forEach((x, i) => x.classList.toggle("good", q.options[i].role === q.answer_role));
      finish(chosen.role === q.answer_role, line()); };
    cur.show = () => { cur.done = true; $("fb").innerHTML = line(); };
  }

  // ── explanations: the engine's derivation (shared prakriyā view) + Vidyut's path ───────────────
  async function explain(q) {
    const box = $("why"); box.hidden = false;
    if (q.steps && q.steps.length && !(q.cell && q.paradigm && ["subanta", "tinanta"].includes(q.paradigm.kind))) {
      box.innerHTML = `<h3>${t("why")}</h3><ol class="ab-steps">${q.steps.map(s => `<li><a href="/sutra/${esc(s[0])}">${esc(s[0])}</a> ${esc(s[1])} → <b>${esc(s[2])}</b></li>`).join("")}</ol>`;
      return;
    }
    const p = q.paradigm, c = q.cell;
    box.innerHTML = `<p class="muted">${t("loading")}</p>`;
    const body = p.kind === "subanta" ? {kind: "subanta", stem: p.stem, linga: p.linga, vibhakti: c.vibhakti, vacana: c.vacana}
      : {kind: "tinanta", ref: p.ref, lakara: p.lakara, prayoga: p.prayoga, pada: p.pada, sanadi: p.sanadi, prefix: p.prefix, purusha: c.purusha, vacana: c.vacana};
    const r = await post("/api/abhyasa/explain", body);
    if (r.error) { box.innerHTML = `<p class="ab-note">${esc(r.error)}</p>`; return; }
    box.innerHTML = `<div id="pk"></div><details style="margin-top:.6rem"><summary>विद्युत्-पथः (Vidyut's sūtra path, for comparison)</summary>${(r.vidyut || []).map(v =>
      `<p class="dev"><b>${esc(D(v.text))}</b></p><ol class="ab-steps">${v.steps.map(s => `<li>${esc(s.code)} → ${esc(D(s.result.join("")))}</li>`).join("")}</ol>`).join("") || "—"}</details>`;
    Prakriya.mount($("pk"), {trace: r.trace, letters: r.letters, title: `${q.title} — ${c.label}`, surface: {slp1: r.surface_slp1, dev: r.surface_dev}});
    box.scrollIntoView({behavior: "smooth", block: "start"});
  }

  function showTable(p, box) {
    box.hidden = false;
    if (!p) return;
    if (!(p.rows || []).length) {
      box.innerHTML = `<h3>${esc(p.title || "")}</h3><table class="ab-tbl">${p.cells.map(c => `<tr><th>${esc(c.label)}</th><td>${esc((c.accepted || []).map(D).join(" / "))} ${badges(c.sources)}</td></tr>`).join("")}</table>`;
      return;
    }
    const by = Object.fromEntries(p.cells.map(c => [c.key, c]));
    box.innerHTML = `<h3>${esc(p.title)}</h3>${grid(p, k => by[k] ? `${esc(by[k].accepted.map(D).join(" / "))}${badges(by[k].sources)}` : "—")}`;
    box.scrollIntoView({behavior: "smooth", block: "start"});
  }

  // ── favourites, lists, comparison, pratyayas ─────────────────────────────────────────────────
  const specOf = p => p.kind === "tinanta" ? {family: "verb", ref: p.ref, lakara: p.lakara, prayoga: p.prayoga, pada: p.pada, sanadi: p.sanadi, prefix: p.prefix, title: p.title}
    : p.kind === "namadhatu" ? {family: "namadhatu", stem: p.stem, pratyaya: p.pratyaya, title: p.title} : {family: "noun", stem: p.stem, linga: p.linga, title: p.title};
  const idOf = s => JSON.stringify([s.family, s.stem || s.ref, s.linga || s.lakara || s.pratyaya, s.prayoga || "", s.sanadi || "", s.prefix || ""]);
  const isFav = p => S.fav.some(f => idOf(f) === idOf(specOf(p)));
  function toggleFav(p) { const s = specOf(p); S.fav = isFav(p) ? S.fav.filter(f => idOf(f) !== idOf(s)) : [...S.fav, s]; save(); }

  async function viewWord(spec, box) {
    box.innerHTML = `<p class="muted">${t("loading")}</p>`;
    const p = await post("/api/abhyasa/paradigm", spec);
    if (p.error) { box.innerHTML = `<p class="ab-note">${esc(p.error)}</p>`; return; }
    const verbCtl = spec.family === "verb" ? `<div class="pk-bar">${sel("lakara", Object.entries(CAT.lakara), spec.lakara || "laT", false)}${sel("prayoga", Object.entries(CAT.prayoga), spec.prayoga || "kartari", false)}
      ${sel("pada", [["parasmai", "परस्मैपदम्"], ["atmane", "आत्मनेपदम्"]], spec.pada)}${sel("prefix", CAT.upasarga.map(u => [u.slp1, u.dev]), spec.prefix)}${sel("sanadi", Object.entries(CAT.sanadi), spec.sanadi)}</div>` : "";
    box.innerHTML = `<div class="ab-btns" style="margin:0 0 .5rem"><button id="w-fav">${isFav(p) ? "★" : "☆"} ${t("fav")}</button><button id="w-cmp">${t("addCmp")}</button><button class="go" id="w-pr">${t("practiceThis")}</button></div>${verbCtl}<div id="wt"></div>`;
    showTable(p, $("wt"));
    box.querySelectorAll(".pk-bar [data-f]").forEach(c => c.onchange = () => { spec[c.dataset.f] = c.value; viewWord(spec, box); });
    $("w-fav").onclick = () => { toggleFav(p); $("w-fav").textContent = `${isFav(p) ? "★" : "☆"} ${t("fav")}`; };
    $("w-cmp").onclick = () => { const s = specOf(p); if (!S.cmp.some(x => idOf(x) === idOf(s))) S.cmp = [...S.cmp.slice(-5), s]; save(); $("w-cmp").textContent = "✓"; };
    $("w-pr").onclick = () => { const fam = spec.family === "verb" ? "verb" : S.fam; const o = opt(fam);
      if (fam === "verb") { o.filters.dhatu = spec.ref; o.filters.lakara = [spec.lakara || "laT"]; } else { o.filters.stem = spec.stem; o.filters.linga = spec.linga; }
      S.fam = fam; S.view = "practice"; save(); fams(); render(); };
  }

  function viewList() {
    const fam = S.fam;
    if (fam === "varna") return viewLipi();
    if (!["noun", "pronoun", "number", "verb", "krdanta", "namadhatu"].includes(fam)) {
      $("view").innerHTML = `<p class="muted">${t("empty")} — see <a href="/shabdarupa">शब्दरूपाणि</a> · <a href="/dhaturupa">धातुरूपाणि</a> · <a href="/sutras">सूत्राणि</a></p>`; return;
    }
    $("view").innerHTML = `<div class="ab-grid"><div class="ab-card"><div class="pk-bar"><label>${t("search")}<input id="lq" class="ab-in" style="min-width:160px"></label>
      ${["noun", "pronoun", "number"].includes(fam) ? `<label>अन्तः${sel("anta", [["ajanta", "अजन्तः"], ["halanta", "हलन्तः"], ...("a A i I u U f o k c j t d n p B m r l v S z s h".split(" ").map(x => [x, D(x) + " (केवल)"]))], "")}</label><label>लिङ्गम्${sel("linga", Object.entries(CAT.linga), "")}</label>` : ""}</div>
      <div class="ab-list" id="ll"></div></div><div class="ab-card" id="lw"><p class="muted">← शब्दं चिनुत</p></div></div>`;
    const load = async () => {
      const a = $("view").querySelector('[data-f="anta"]'), l = $("view").querySelector('[data-f="linga"]');
      const qs = new URLSearchParams({family: fam === "krdanta" ? "verb" : fam, q: $("lq").value.trim(), anta: a ? a.value : "", linga: l ? l.value : ""});
      const rows = await get("/api/abhyasa/list?" + qs);
      $("ll").innerHTML = rows.map((r, i) => `<button data-i="${i}">${esc(r.dev)}<small>${esc(r.linga ? CAT.linga[r.linga] : r.gana || "")} ${esc((r.artha || "").slice(0, 40))}</small></button>`).join("") || t("empty");
      $("ll").querySelectorAll("button").forEach(b => b.onclick = () => { const r = rows[+b.dataset.i];
        const spec = r.ref ? {family: "verb", ref: r.ref, lakara: "laT", prayoga: "kartari"} : r.pratyaya ? {family: "namadhatu", stem: r.stem, pratyaya: r.pratyaya} : {family: "noun", stem: r.stem, linga: r.linga};
        viewWord(spec, $("lw")); });
    };
    $("lq").oninput = () => { clearTimeout($("lq")._t); $("lq")._t = setTimeout(load, 250); };
    $("view").querySelectorAll(".pk-bar select").forEach(s => s.onchange = load); load();
  }

  async function viewLipi() {
    const letters = ["a", "A", "i", "I", "u", "U", "f", "F", "x", "e", "E", "o", "O", ..."kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh".split("").map(c => c + "a")];
    const r = await post("/api/abhyasa/lipi", {text: letters.join(" "), to: Object.keys(CAT.lipi)});
    const cols = Object.keys(CAT.lipi), split = Object.fromEntries(cols.map(c => [c, (r[c] || "").split(" ")]));
    $("view").innerHTML = `<div class="ab-card"><h3>लिपियों की तुलना <span class="muted" style="font-size:13px">(Vidyut lipi)</span></h3><table class="ab-tbl"><tr><th>देवनागरी</th>${cols.map(c => `<th>${esc(CAT.lipi[c])}</th>`).join("")}</tr>
      ${letters.map((l, i) => `<tr><td>${esc(D(l))}</td>${cols.map(c => `<td style="font-size:22px">${esc(split[c][i] || "")}</td>`).join("")}</tr>`).join("")}</table></div>`;
  }

  async function viewCompare() {
    if (!S.cmp.length) { $("view").innerHTML = `<p class="muted">${t("empty")} — ${t("v_list")} → ${t("addCmp")}</p>`; return; }
    $("view").innerHTML = `<p class="muted">${t("loading")}</p>`;
    const ps = await Promise.all(S.cmp.map(s => post("/api/abhyasa/paradigm", s)));
    const keys = [...new Map(ps.flatMap(p => (p.cells || []).map(c => [c.key + "|" + c.label, c]))).values()];
    $("view").innerHTML = `<div class="ab-card"><div class="ab-btns" style="margin:0 0 .5rem"><button id="cmp-clear">✕ clear</button></div><table class="ab-tbl"><tr><th></th>${ps.map(p => `<th>${esc(p.title || p.error || "")}</th>`).join("")}</tr>
      ${keys.map(k => `<tr><th>${esc(k.label)}</th>${ps.map(p => { const c = (p.cells || []).find(x => x.key === k.key && x.label === k.label); return `<td>${c ? esc(c.accepted.map(D).join(" / ")) : "—"}</td>`; }).join("")}</tr>`).join("")}</table></div>`;
    $("cmp-clear").onclick = () => { S.cmp = []; save(); viewCompare(); };
  }

  function viewFav() {
    $("view").innerHTML = `<div class="ab-grid"><div class="ab-card"><div class="ab-list" id="fl">${S.fav.map((f, i) => `<button data-i="${i}">${esc(f.title || f.stem || f.ref)}</button>`).join("") || t("empty")}</div></div><div class="ab-card" id="fw"></div></div>`;
    $("fl").querySelectorAll("button[data-i]").forEach(b => b.onclick = () => viewWord({...S.fav[+b.dataset.i]}, $("fw")));
  }

  function viewPratyaya() {
    const SUP = [["सुँ", "औ", "जस्"], ["अम्", "औट्", "शस्"], ["टा", "भ्याम्", "भिस्"], ["ङे", "भ्याम्", "भ्यस्"], ["ङसिँ", "भ्याम्", "भ्यस्"], ["ङस्", "ओस्", "आम्"], ["ङि", "ओस्", "सुप्"]];
    const TIN = [["तिप्", "तस्", "झि", "त", "आताम्", "झ"], ["सिप्", "थस्", "थ", "थास्", "आथाम्", "ध्वम्"], ["मिप्", "वस्", "मस्", "इट्", "वहि", "महिङ्"]];
    $("view").innerHTML = `<div class="ab-card"><h3>सुप् प्रत्ययाः — <a href="/sutra/4.1.2">4.1.2</a> स्वौजसमौट्छष्टाभ्याम्भिस्ङेभ्याम्भ्यस्ङसिभ्याम्भ्यस्ङसोसाम्ङ्योस्सुप्</h3>
      <table class="ab-tbl"><tr><th></th>${["एकवचनम्", "द्विवचनम्", "बहुवचनम्"].map(x => `<th>${x}</th>`).join("")}</tr>${SUP.map((r, i) => `<tr><th>${esc(CAT.vibhakti[i + 1])}</th>${r.map(x => `<td>${x}</td>`).join("")}</tr>`).join("")}</table>
      <h3>तिङ् प्रत्ययाः — <a href="/sutra/3.4.78">3.4.78</a> तिप्तस्झिसिप्थस्थमिब्वस्मस्तातांझथासाथांध्वमिड्वहिमहिङ्</h3>
      <table class="ab-tbl"><tr><th></th><th colspan="3">परस्मैपदम् (1.4.99)</th><th colspan="3">आत्मनेपदम् (1.4.100)</th></tr>${TIN.map((r, i) => `<tr><th>${["प्रथमः", "मध्यमः", "उत्तमः"][i]}</th>${r.map(x => `<td>${x}</td>`).join("")}</tr>`).join("")}</table>
      <h3>कृत् प्रत्ययाः</h3><p class="dev">${Object.values(CAT.krt).map(esc).join(" · ")}</p>
      <h3>तद्धित प्रत्ययाः</h3><p class="dev">${Object.values(CAT.taddhita).map(esc).join(" · ")}</p></div>`;
  }

  // ── शब्द खोजें: any word → its table (even beyond the lists) and its व्युत्पत्ति ─────────────────
  $("sf").onsubmit = e => { e.preventDefault(); const q = $("sq").value.trim(); if (!q) return;
    S.search = {q, linga: $("sl").value}; S.view = "search"; save(); render(); };

  async function viewSearch() {
    const s = S.search || {}; if (!s.q) { S.view = "practice"; return viewPractice(); }
    $("sq").value = s.q; $("sl").value = s.linga || "";
    $("view").innerHTML = `<p class="muted">${t("loading")}</p>`;
    const r = await post("/api/abhyasa/search", {q: s.q, linga: s.linga || ""});
    if (r.error) { $("view").innerHTML = `<p class="ab-note">${esc(r.error)}</p>`; return; }
    const lg = Object.entries(CAT.linga).map(([k, v]) => `<option value="${k}" ${k === r.linga ? "selected" : ""}>${esc(v)}</option>`).join("");
    $("view").innerHTML = `<div class="ab-grid" style="grid-template-columns:minmax(0,1.1fr) minmax(0,1fr)"><div class="ab-card">
        <div class="ab-title">${esc(r.stem_dev)} <select id="s-lg" aria-label="लिङ्गम्">${lg}</select></div>
        ${r.form_of.length ? `<p>“${esc(r.dev)}” — ${r.form_of.map((f, i) => `<a href="#" data-fo="${i}">${esc(f.stem_dev)} (${esc(f.linga_dev)})</a> · ${esc(f.cell)}`).join("; ")}</p>` : ""}
        ${r.nouns.length > 1 || (r.nouns[0] && r.nouns[0].stem !== r.stem) ? `<div class="ab-list" style="max-height:120px;margin:.4rem 0">${r.nouns.map((n, i) => `<button data-n="${i}">${esc(n.dev)}<small>${esc(CAT.linga[n.linga] || "")} ${esc((n.artha || "").slice(0, 30))}</small></button>`).join("")}</div>` : ""}
        ${r.roots.length ? `<p>धातुः: ${r.roots.map((d, i) => `<a href="#" data-r="${i}">${esc(d.dev)} (${esc(d.gana)}, ${esc(d.artha)})</a>`).join(" · ")}</p>` : ""}
        <div id="sw"></div></div>
      <div class="ab-card vy"><h3 style="margin:.2rem 0">व्युत्पत्तिः <span class="muted" style="font-size:12px;font-family:var(--body)">kośas propose · Kāśikā / uṇādi / Vidyut / our engine verify</span></h3><div id="vy"><p class="muted">${t("loading")}</p></div></div></div>`;
    const open = (stem, linga) => { S.search = {q: D(stem), linga}; save(); render(); };
    $("s-lg").onchange = e => open(r.stem, e.target.value);
    $("view").querySelectorAll("[data-fo]").forEach(a => a.onclick = ev => { ev.preventDefault(); const f = r.form_of[+a.dataset.fo]; open(f.stem, f.linga); });
    $("view").querySelectorAll("[data-n]").forEach(b => b.onclick = () => { const n = r.nouns[+b.dataset.n]; open(n.stem, n.linga); });
    $("view").querySelectorAll("[data-r]").forEach(a => a.onclick = ev => { ev.preventDefault(); viewWord({family: "verb", ref: r.roots[+a.dataset.r].ref, lakara: "laT", prayoga: "kartari"}, $("sw")); });
    viewWord({family: "noun", stem: r.stem, linga: r.linga, vidyut_fallback: true}, $("sw"));
    const v = await post("/api/abhyasa/vyutpatti", {word: r.stem, linga: r.linga});
    $("vy").innerHTML = v.error ? `<p class="ab-note">${esc(v.error)}</p>` : vyNode(v, r.linga) + (v.lexdb ? "" : `<p class="ab-note">kośa database not found (set PANINI_LEXDB or install ~/subhastini/lexicon/lex.db) — Kāśikā, uṇādi and Vidyut only</p>`);
    wireVy($("vy"));
  }

  const ENG = {confident: "ok", working: "ok", unexercised: "no", placeholder: "no", gate_only: "warn"};
  function vyNode(n, linga) {
    const noms = Object.entries(n.nominatives || {}).map(([k, v]) => `${esc(CAT.linga[k] || k)}: ${esc(v.join(" / "))}`).join(" · ");
    const props = (n.proposals || []).map((p, i) => {
      const pr = p.pratyayas.map((x, j) => ({x, dev: p.pratyayas_dev[j], kind: p.kinds[j]}));
      const main = pr.find(x => x.kind === "taddhita" || x.kind === "krt");
      const kind = main && main.kind === "krt" ? "krdanta" : "taddhita";
      const dh = p.dhatus || [];
      const vy = p.vidyut.length ? `<span class="chip ok">विद्युत् ✓</span><details><summary>विद्युत्-पथः</summary><ol class="ab-steps">${p.vidyut[0].path.map(s => `<li>${esc(s.id)} ${esc(s.text)}</li>`).join("")}</ol></details>`
        : (p.vidyut_forms || []).filter(f => f.forms_dev.length).map(f => `<span class="chip warn">विद्युत् बनाता है: ${esc(f.forms_dev.join(" / "))}</span>`).join("") || `<span class="chip">विद्युत् —</span>`;
      const eng = main ? `<button type="button" data-eng='${esc(JSON.stringify({kind, base: p.base, pratyaya: main.x, linga: linga || "pulliṅga", word: n.word, dhatu_ref: (dh[0] || {}).ref || "", sutras: p.sutras.map(s => s.id)}))}'>यन्त्रेण परीक्ष्यताम्</button><div class="eng-out"></div>` : "";
      return `<div class="prop"><div class="chain"><b>${esc(p.base_dev || "?")}</b>${dh.length ? ` <small class="muted">(${dh.map(d => esc(d.dev + " " + d.artha)).join("; ")})</small>` : ""} + ${pr.map(x => esc(x.dev)).join(" + ")} → <b>${esc(n.word_dev)}</b></div>
        <div>${p.sources.map(s => `<span class="chip" title="${esc(s.text)}">${esc(s.label)}</span>`).join("")}</div>
        ${p.sutras.length ? `<ul class="ab-steps">${p.sutras.map(s => `<li>${s.kind === "unadi" ? esc(s.id) : `<a href="/sutra/${esc(s.id)}">${esc(s.id)}</a>`} ${esc(s.text)}
          ${s.kashika_has_word ? `<span class="chip ok">${s.kind === "unadi" ? "उणादि-उदाहरणम्" : "काशिका"} ✓ ${esc(n.word_dev)}</span>` : ""}${s.engine ? `<span class="chip ${ENG[s.engine] || ""}">यन्त्रम्: ${esc(s.engine)}</span>` : ""}</li>`).join("")}</ul>` : ""}
        ${vy} ${eng}<details><summary>कोश-पाठः</summary>${p.sources.map(s => `<p class="src"><b>${esc(s.label)}</b> — ${esc(s.text)}</p>`).join("")}</details></div>`;
    }).join("");
    const kas = (n.kashika || []).length ? `<details ${n.proposals.length ? "" : "open"}><summary>काशिका — sūtras whose udāharaṇa is this word (${n.kashika.length})</summary><ul class="ab-steps">${n.kashika.map(k => `<li><a href="/sutra/${esc(k.id)}">${esc(k.id)}</a> ${esc(k.text)} <span class="chip ${ENG[k.engine] || ""}">यन्त्रम्: ${esc(k.engine || "—")}</span><br><small>${esc(k.examples)}</small></li>`).join("")}</ul></details>` : "";
    const uni = (n.unadi || []).length ? `<p>उणादि: ${n.unadi.map(u => `${esc(u.id)} ${esc(u.text)}`).join(" · ")}</p>` : "";
    const srch = (n.search || []).length ? `<details><summary>विद्युत्-अन्वेषणम् (generate-and-test; no kośa backs these)</summary><ul class="ab-steps">${n.search.map(h => `<li>${esc(D(h.base || h.dhatu))} + ${esc(h.pratyaya || h.krt)} → ${esc(D(h.form))}</li>`).join("")}</ul></details>` : "";
    const mean = (n.meanings || []).length ? `<details><summary>अर्थः</summary>${n.meanings.map(m => `<p class="src"><b>${esc(m.label)}</b> — ${esc(m.text)}</p>`).join("")}</details>` : "";
    return `<div class="node"><div class="chain"><b>${esc(n.word_dev)}</b> <small class="muted">${noms}</small></div>${mean}
      ${props || (kas || uni || srch ? "" : `<p class="muted">कोशेषु व्युत्पत्तिः न लब्धा — no kośa proposal${n.lexdb ? "" : " (kośa database missing)"}</p>`)}${kas}${uni}${srch}
      ${n.base_tree ? vyNode(n.base_tree, "") : ""}</div>`;
  }
  function wireVy(box) {
    box.querySelectorAll("[data-eng]").forEach(b => b.onclick = async () => {
      const out = b.nextElementSibling; b.disabled = true; out.innerHTML = `<p class="muted">यन्त्रेण सिध्यति… (≈ 5–40 s)</p>`;
      const r = await post("/api/abhyasa/vyutpatti/engine", JSON.parse(b.dataset.eng)); b.disabled = false;
      if (r.error) { out.innerHTML = `<p class="ab-note">${esc(r.error)}</p>`; return; }
      if (r.match) {
        out.innerHTML = `<span class="chip ok">यन्त्रम् ✓ ${esc(r.form_dev)}</span><div class="pk"></div>`;
        Prakriya.mount(out.querySelector(".pk"), {trace: r.derivation.trace, letters: r.derivation.letters, title: r.form_dev,
          surface: {slp1: r.derivation.surface_slp1, dev: r.derivation.surface_dev}});
      } else {
        const got = [...new Set(r.tried.flatMap(x => (x.got || []).map(g => g.form_dev)))];
        out.innerHTML = `<span class="chip no">यन्त्रम् ✗</span> want ${esc((r.want_dev || []).join(" / "))}; the engine makes ${esc(got.join(" / ") || "nothing")}
          <small class="muted">— an engine gap (logged in docs/ABHYASA_PLAN.md §6 when confirmed)</small>`;
      }
    });
  }

  // ── boot ──────────────────────────────────────────────────────────────────────────────────────
  get("/api/abhyasa/catalog").then(c => { CAT = c; if (!CAT.families[S.fam]) S.fam = "noun"; applyChrome(); fams(); render(); })
    .catch(e => { $("view").innerHTML = `<p class="ab-note">catalog: ${esc(e)}</p>`; });
})();
