/* ─────────────────────────────────────────────────────────────────
   lipi.js — लिपि-चयनम् for every prakriyā trace (SLP1 / देवनागरी / उभयम्).
   देवनागरी is varṇa-vibhāga — vyañjana with halanta, svara as its own
   letter — until __MERGE__ joins the pada; later steps show the joined
   pada.  Needs transliterate.js.
   ───────────────────────────────────────────────────────────────── */

const Lipi = (() => {
  const KEY = "panini-lipi";
  let mode = localStorage.getItem(KEY) || localStorage.getItem("shabda-lipi") || "both";
  const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
  const varna = t => Transliterate.slp1ToVarnas(t);
  const joined = t => Transliterate.fromSLP1(t, "devanagari");

  const show = (s, d) => mode === "slp1" ? s
    : mode === "dev" ? `<span class="lipi-dv">${d}</span>`
    : `${s}<span class="lipi-dv" style="display:block">${d}</span>`;

  /* Steps after __MERGE__ (e.g. tripāḍī 8.4.2) act on the joined pada. */
  const mergeAt = new WeakMap();
  const stageOf = (trace, step) => {
    if (step.sutra_id === "__MERGE__") return "merge";
    if (!mergeAt.has(trace)) mergeAt.set(trace, trace.findIndex(s => s.sutra_id === "__MERGE__"));
    const m = mergeAt.get(trace);
    return m >= 0 && trace.indexOf(step) > m ? "pada" : "varna";
  };
  const shift = (before, after, stage) => show(
    `${esc(before)} → ${esc(after)}`,
    `${esc(stage === "pada" ? joined(before) : varna(before))} → ${esc(stage === "varna" ? varna(after) : joined(after))}`);

  return {
    get mode() { return mode; },
    varna, joined, shift,
    /* One engine trace row: before → after, staged by its place relative to __MERGE__. */
    step: (trace, s) => shift(s.form_before, s.form_after, stageOf(trace, s)),
    form: (trace, s) => show(esc(s.form_after), esc(stageOf(trace, s) === "varna" ? varna(s.form_after) : joined(s.form_after))),
    /* Vidyut-style term list: [akza, Ne] → akza + Ne. */
    terms: ts => show(esc(ts.join(" + ")), esc(ts.map(varna).join(" + "))),
    select: id => `<label class="lipi-ctl" style="white-space:nowrap">लिपिः <select id="${id}">
      <option value="both">उभयम् — SLP1 + देवनागरी</option><option value="dev">देवनागरी — वर्ण-विभागः</option><option value="slp1">SLP1</option></select></label>`,
    bind(id) {
      const el = document.getElementById(id); if (!el) return;
      el.value = mode;
      el.addEventListener("change", () => {
        mode = el.value; localStorage.setItem(KEY, mode);
        document.querySelectorAll(".lipi-ctl select").forEach(s => { s.value = mode; });
        window.dispatchEvent(new CustomEvent("lipi-change"));
      });
    },
  };
})();
