/* यात्रा · Śabda journey (◆ teaching aid, hidden until opened). Reads only the engine's own trace; never changes it.
   Main path = what this derivation did. Dashed boxes = tributaries / branches / forks, each with an honest status:
   ✔ running · ◐ partly (example pipelines only) · ⌛ planned.  Authority: Kāśikā 1.2.45, 1.2.46, 1.2.64, 2.4.71, 3.1.8, 4.1.1, 4.1.82, 8.4.56. */
window.PkJourney = (function () {
  const esc = s => String(s == null ? "" : s).replace(/[&<>"]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]));
  const bi = (hi, en) => `<span class="dev">${esc(hi)}</span> <span class="pj-en">${esc(en)}</span>`;
  const ST = {ok: ["✔", "चालू", "running"], part: ["◐", "अंशतः", "partly"], plan: ["⌛", "योजित", "planned"]};
  const chip = k => `<span class="pj-st pj-${k}">${ST[k][0]} ${ST[k][1]} · ${ST[k][2]}</span>`;
  const box = (st, hi, en, auth, note) => `<div class="pj-side pj-${st}"><b>${bi(hi, en)}</b> ${chip(st)}<div class="muted">${esc(auth)}</div>${note ? `<div class="pj-note">${note}</div>` : ""}</div>`;
  const IN = [ // tributaries: where a stem can come FROM (1.2.46)
    ["ok", "अव्युत्पन्नम् (अर्थवत्)", "Primitive stem (arthavat)", "1.2.45", ""],
    ["part", "कृदन्तम् ← धातुः + कृत्", "Kṛdanta ← root + kṛt", "1.2.46", bi("तृच्, ण्वुल् उदाहरण-पाइपलाइन; शेष योजित", "tṛc / ṇvul example pipelines; rest planned")],
    ["part", "तद्धितान्तम् ← प्रातिपदिकम् + तद्धितः", "Taddhitānta ← stem + taddhita", "1.2.46 · 4.1.82", bi("उदाहरण-पाइपलाइन; सर्वत्र योजित", "example pipelines; general wiring planned")],
    ["part", "समासः ← सुबन्त-पदानि", "Samāsa ← subanta members (each its own journey)", "1.2.46 · 2.1.4 · 2.4.71", bi("द्वन्द्व/बहुव्रीहि उदाहरण; शेष योजित", "dvandva / bahuvrīhi examples; rest planned")]];
  const BR = [ // branches: where a stem + its sup can go (sup dropped by 2.4.71)
    ["part", "नामधातुः / सनाद्यन्तः धातुः", "Nāmadhātu / sanādyanta root", "3.1.8 सुबन्तात् · 3.1.32 · 2.4.71 (सुप्-लुक्)", bi("san/ṇic उदाहरण; नामधातु योजित", "san / ṇic examples; nāmadhātu planned")],
    ["plan", "स्त्री-प्रत्ययः (टाप्, ङीप् …) ↺", "Strī-pratyaya loop", "4.1.1 ङ्याप्प्रातिपदिकात् · 4.1.3–5", bi("लूप्: स्त्री-प्रत्ययान्तात् सुप् (४.१.१); सूत्र-फाइलें हैं, यहाँ जुड़ी नहीं", "loop back to the stem, then sup (4.1.1); sūtra files exist, not linked here")],
    ["plan", "एकशेषः (सरूपाणां, एकविभक्तौ)", "Ekaśeṣa (same-form words, one vibhakti)", "1.2.64 · 1.2.65", bi("स्रोत नहीं — सुबन्तों का मेल (वृत्ति); योजित", "not a stem-source: merges subantas (a vṛtti); planned")]];

  function stages(t, fmt) {
    const A = (s) => /^APPLIED/.test(s.status) && s.sutra_id !== "__MERGE__", f = s => fmt(s.form_after || "", s.form_after_dev || "");
    const at = ids => t.findIndex(s => A(s) && ids.includes(s.sutra_id)), out = [];
    const add = (i, hi, en, ids, extra) => { if (i >= 0) out.push({i, hi, en, ids, form: f(t[i]), extra: extra || ""}); };
    const a = at(["1.2.45", "1.2.46"]), b = at(["4.1.2"]), c = at(["1.4.13", "1.4.14"]), c2 = at(["1.4.14"]);
    add(a, "प्रातिपदिक-संज्ञा", "Stem named (prātipadika)", [t[a] && t[a].sutra_id]);
    add(b, "सुप्-प्रत्ययः", "Case ending (sup) added", ["4.1.2"], "BRANCH");
    add(c2 >= 0 ? c2 : c, "अङ्ग-/पद-संज्ञा", "Aṅga / pada named", ["1.4.13", "1.4.14"]);
    const ap = t.map((s, i) => A(s) && !/^(__|1\.[1-4])/.test(s.sutra_id) ? i : -1).filter(i => i > Math.max(b, c2));
    if (ap.length) out.push({i: ap[0], hi: `पद-कार्याणि (${ap.length} सूत्र-प्रयोगाः)`, en: `Operations on the pada (${ap.length} sūtras applied)`, ids: [...new Set(ap.map(i => t[i].sutra_id))].slice(0, 12), form: f(t[ap[ap.length - 1]]), extra: "RANGE", to: ap[ap.length - 1]});
    return out;
  }

  function render(t, d, fmt) {
    if (!t || !t.length) return "";
    const S = stages(t, fmt); if (!S.length) return "";
    const forks = (d.forks || []).filter(x => x && x.alternative), sur = d.surface ? fmt(d.surface.slp1, d.surface.dev) : "";
    const main = S.map((s, n) => `<div class="pj-st-main" data-n="${n}"><div class="pj-no">${n + 1}</div><b>${bi(s.hi, s.en)}</b><div class="pj-form dev">${esc(s.form)}</div>
      <div class="muted">${s.ids.filter(Boolean).map(x => `<a href="/sutra/${esc(x)}">${esc(x)}</a>`).join(" · ")} · <a href="#s-${s.i + 1}">#${s.i + 1}${s.to != null ? "–" + (s.to + 1) : ""}</a></div>
      ${s.extra === "BRANCH" ? `<div class="pj-branches">${BR.map(x => box(...x)).join("")}</div>` : ""}</div>`).join('<div class="pj-arrow">➜</div>');
    const fk = forks.length ? `<div class="pj-forks"><b>${bi("अन्ते पक्ष-भेदः (वा / विभाषा)", "Forks at the end (vā / vibhāṣā)")}</b>
      ${forks.map(x => { const m = t.find(r => /^APPLIED/.test(r.status) && r.sutra_type === "VIBHASHA" && r.form_before === x.alternative); x = Object.assign({}, x, m ? {sutra_id: m.sutra_id} : {}); return `<div class="pj-fork"><span class="pj-w">● ${esc(sur)}</span> <span class="muted">${bi("इञ्जन का मार्ग", "engine's path")}</span> &nbsp;⑂&nbsp; <span class="pj-w pj-alt">◌ ${esc(fmt(x.alternative, ""))}</span> <span class="muted">${bi("वैकल्पिक पक्ष", "other branch")} · <a href="/sutra/${esc(x.sutra_id)}">${esc(x.sutra_id)}</a> · ${chip("plan")} ${bi("इस पक्ष को अन्त तक चलाना योजित", "running this branch to its end is planned")}</span></div>`; }).join("")}</div>` : "";
    return `<details class="pk-journey no-print"><summary>🧭 ${bi("यात्रा — शब्द का मार्ग (आगे-पीछे)", "Journey — the word's path (step back / forward)")} <span class="pk-tag">◆ ${bi("शिक्षण-सहायक", "teaching aid")}</span></summary>
      <p class="muted">${bi("मुख्य मार्ग = इस प्रक्रिया ने जो किया। टूटी रेखा = स्रोत / शाखा / पक्ष; ✔ चालू, ◐ अंशतः, ⌛ योजित। केवल इञ्जन-अभिलिखित; शास्त्र-प्रमाण सूत्र-संख्या सहित।", "Solid = what this derivation did. Dashed = source / branch / fork; ✔ running, ◐ partly, ⌛ planned. Only the engine's own record; śāstra authority shown by sūtra number.")}</p>
      <div class="pj-ctl"><button type="button" class="pj-prev">‹ पीछे · back</button><input type="range" class="pj-sl" min="0" max="${S.length - 1}" value="0"><button type="button" class="pj-next">आगे · next ›</button> <span class="pj-lbl muted"></span></div>
      <div class="pj-in"><b>${bi("आरम्भ — शब्द कहाँ से आया (१.२.४५–४६)", "Start — where the stem comes from (1.2.45–46)")}</b><div class="pj-sides">${IN.map(x => box(...x)).join("")}</div></div>
      <div class="pj-main">${main}</div>${fk}</details>`;
  }

  function wire(root) {
    const d = root.querySelector(".pk-journey"); if (!d || d._w) return; d._w = 1;
    const sl = d.querySelector(".pj-sl"), cards = [...d.querySelectorAll(".pj-st-main")], lb = d.querySelector(".pj-lbl");
    const go = n => { n = Math.max(0, Math.min(cards.length - 1, n)); sl.value = n; cards.forEach((c, i) => c.classList.toggle("pj-on", i === n)); cards.forEach((c, i) => c.classList.toggle("pj-past", i < n));
      lb.textContent = `${n + 1} / ${cards.length}`; const m = d.querySelector(".pj-main"); m.scrollTo({left: Math.max(0, cards[n].offsetLeft - m.offsetLeft - 20), behavior: "smooth"}); };
    sl.oninput = () => go(+sl.value); d.querySelector(".pj-prev").onclick = () => go(+sl.value - 1); d.querySelector(".pj-next").onclick = () => go(+sl.value + 1); go(0);
  }
  return {render, wire};
})();
