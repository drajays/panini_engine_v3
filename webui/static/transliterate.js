/**
 * transliterate.js — Pāṇini Engine v3
 * Converts between Sanskrit input encoding schemes and SLP1 (internal).
 *
 * Schemes (per https://sanskrit.uohyd.ac.in/scl/table.html):
 *   slp1       — SLP1 (Sanskrit Library Phonetic, used internally)
 *   iast       — IAST (International Alphabet of Sanskrit Transliteration)
 *   hk         — Harvard-Kyoto
 *   velthuis   — Velthuis (.t .d .n "s .s etc.)
 *   wx         — WX notation (retroflex=lowercase, dental=w/x/W/X)
 *   itrans     — ITRANS
 *   devanagari — Devanāgarī Unicode
 *
 * API:
 *   Transliterate.toSLP1(text, scheme)   → SLP1 string
 *   Transliterate.fromSLP1(text, scheme) → target-scheme string
 *   Transliterate.SCHEME_LABELS          → {id → display label}
 */
const Transliterate = (() => {

  const SCHEME_LABELS = {
    slp1:       "SLP1",
    iast:       "IAST",
    hk:         "Harvard-Kyoto",
    velthuis:   "Velthuis",
    wx:         "WX",
    itrans:     "ITRANS",
    devanagari: "देवनागरी",
  };

  // ── Phoneme table ──────────────────────────────────────────────────────────
  // Each vowel row: { s:SLP1, i:IAST, h:HK, v:Velthuis, w:WX, t:ITRANS[], d:DevInd, m:DevMatra }
  // m:"" = inherent-a (no separate matra char), m:null = no matra form
  const V = [
    {s:"O",i:"au", h:"au",v:"au", w:"O",t:["au"],         d:"औ",m:"ौ"},
    {s:"E",i:"ai", h:"ai",v:"ai", w:"E",t:["ai"],         d:"ऐ",m:"ै"},
    {s:"A",i:"ā",  h:"A", v:"aa", w:"A",t:["aa","A"],     d:"आ",m:"ा"},
    {s:"I",i:"ī",  h:"I", v:"ii", w:"I",t:["ii","I"],     d:"ई",m:"ी"},
    {s:"U",i:"ū",  h:"U", v:"uu", w:"U",t:["uu","U"],     d:"ऊ",m:"ू"},
    {s:"F",i:"ṝ",  h:"RR",v:".rr",w:"Q",t:["RRI","R^I"],  d:"ॠ",m:"ॄ"},
    {s:"f",i:"ṛ",  h:"R", v:".r", w:"q",t:["RRi","R^i"],  d:"ऋ",m:"ृ"},
    {s:"x",i:"ḷ",  h:"lR",v:".l", w:"L",t:["LLi","L^i"],  d:"ऌ",m:"ॢ"},
    {s:"e",i:"e",  h:"e", v:"e",  w:"e",t:["e"],           d:"ए",m:"े"},
    {s:"o",i:"o",  h:"o", v:"o",  w:"o",t:["o"],           d:"ओ",m:"ो"},
    {s:"a",i:"a",  h:"a", v:"a",  w:"a",t:["a"],           d:"अ",m:""},
    {s:"i",i:"i",  h:"i", v:"i",  w:"i",t:["i"],           d:"इ",m:"ि"},
    {s:"u",i:"u",  h:"u", v:"u",  w:"u",t:["u"],           d:"उ",m:"ु"},
    {s:"M",i:"ṃ",  h:"M", v:".m", w:"M",t:["M",".m","m~"],d:"ं",m:"ं"},
    {s:"H",i:"ḥ",  h:"H", v:".h", w:"Z",t:["H",".h"],     d:"ः",m:"ः"},
    {s:"'",i:"'",  h:"'", v:"'",  w:"Z",t:["'",".a"],      d:"ऽ",m:null},
  ];

  // Each consonant row: { s:SLP1, i:IAST, h:HK, v:Velthuis, w:WX, t:ITRANS[], d:Dev }
  const C = [
    {s:"k", i:"k",  h:"k",  v:"k",   w:"k",  t:["k"],          d:"क"},
    {s:"K", i:"kh", h:"kh", v:"kh",  w:"K",  t:["kh"],         d:"ख"},
    {s:"g", i:"g",  h:"g",  v:"g",   w:"g",  t:["g"],          d:"ग"},
    {s:"G", i:"gh", h:"gh", v:"gh",  w:"G",  t:["gh"],         d:"घ"},
    {s:"N", i:"ṅ",  h:"G",  v:"\"n", w:"f",  t:["~N","N^"],    d:"ङ"},
    {s:"c", i:"c",  h:"c",  v:"c",   w:"c",  t:["ch","c"],     d:"च"},
    {s:"C", i:"ch", h:"ch", v:"ch",  w:"C",  t:["Ch","chh"],   d:"छ"},
    {s:"j", i:"j",  h:"j",  v:"j",   w:"j",  t:["j"],          d:"ज"},
    {s:"J", i:"jh", h:"jh", v:"jh",  w:"J",  t:["jh"],         d:"झ"},
    {s:"Y", i:"ñ",  h:"J",  v:"~n",  w:"F",  t:["~n","JN"],    d:"ञ"},
    {s:"w", i:"ṭ",  h:"T",  v:".t",  w:"t",  t:["T"],          d:"ट"},
    {s:"W", i:"ṭh", h:"Th", v:".th", w:"T",  t:["Th"],         d:"ठ"},
    {s:"q", i:"ḍ",  h:"D",  v:".d",  w:"d",  t:["D"],          d:"ड"},
    {s:"Q", i:"ḍh", h:"Dh", v:".dh", w:"D",  t:["Dh"],         d:"ढ"},
    {s:"R", i:"ṇ",  h:"N",  v:".n",  w:"N",  t:["N"],          d:"ण"},
    {s:"t", i:"t",  h:"t",  v:"t",   w:"w",  t:["t"],          d:"त"},
    {s:"T", i:"th", h:"th", v:"th",  w:"W",  t:["th"],         d:"थ"},
    {s:"d", i:"d",  h:"d",  v:"d",   w:"x",  t:["d"],          d:"द"},
    {s:"D", i:"dh", h:"dh", v:"dh",  w:"X",  t:["dh"],         d:"ध"},
    {s:"n", i:"n",  h:"n",  v:"n",   w:"n",  t:["n"],          d:"न"},
    {s:"p", i:"p",  h:"p",  v:"p",   w:"p",  t:["p"],          d:"प"},
    {s:"P", i:"ph", h:"ph", v:"ph",  w:"P",  t:["ph"],         d:"फ"},
    {s:"b", i:"b",  h:"b",  v:"b",   w:"b",  t:["b"],          d:"ब"},
    {s:"B", i:"bh", h:"bh", v:"bh",  w:"B",  t:["bh"],         d:"भ"},
    {s:"m", i:"m",  h:"m",  v:"m",   w:"m",  t:["m"],          d:"म"},
    {s:"y", i:"y",  h:"y",  v:"y",   w:"y",  t:["y"],          d:"य"},
    {s:"r", i:"r",  h:"r",  v:"r",   w:"r",  t:["r"],          d:"र"},
    {s:"l", i:"l",  h:"l",  v:"l",   w:"l",  t:["l"],          d:"ल"},
    {s:"v", i:"v",  h:"v",  v:"v",   w:"v",  t:["v","w"],      d:"व"},
    {s:"S", i:"ś",  h:"z",  v:"\"s", w:"z",  t:["sh","z"],     d:"श"},
    {s:"z", i:"ṣ",  h:"S",  v:".s",  w:"s",  t:["Sh","S"],     d:"ष"},
    {s:"s", i:"s",  h:"s",  v:"s",   w:"S",  t:["s"],          d:"स"},
    {s:"h", i:"h",  h:"h",  v:"h",   w:"H",  t:["h"],          d:"ह"},
    {s:"L", i:"ḻ",  h:"L",  v:".L",  w:"lY", t:["ld","L"],     d:"ळ"},
  ];

  const HALANT = "्";

  // ── Devanāgarī lookup tables ───────────────────────────────────────────────
  const devVow   = {};  // independent vowel char → SLP1
  const devMat   = {};  // matra char → SLP1  (empty string matra NOT stored here)
  const devCons  = {};  // consonant char → SLP1
  const slp1Ind  = {};  // SLP1 vowel → independent dev char
  const slp1Mat  = {};  // SLP1 vowel → matra dev char (empty string = inherent a)
  const slp1Dev  = {};  // SLP1 consonant/special → dev char

  V.forEach(e => {
    if (e.d)       devVow[e.d]  = e.s;
    if (e.m)       devMat[e.m]  = e.s;   // skip "" (inherent a has no matra char)
    slp1Ind[e.s]  = e.d;
    if (e.m != null) slp1Mat[e.s] = e.m; // "" = inherent a
  });
  C.forEach(e => {
    devCons[e.d] = e.s;
    slp1Dev[e.s] = e.d;
  });
  // Special
  slp1Dev["M"] = "ं"; slp1Dev["H"] = "ः"; slp1Dev["'"] = "ऽ";

  const VOW_SET  = new Set(V.map(e => e.s));
  const CONS_SET = new Set(C.map(e => e.s));

  // ── Build scheme → SLP1 lookup (longest match first) ──────────────────────
  function buildRevLookup(fieldName) {
    const pairs = [];
    const add = (repr, slp1) => { if (repr) pairs.push([repr, slp1]); };
    V.forEach(e => {
      if (fieldName === "t") e.t.forEach(r => add(r, e.s));
      else add(e[fieldName], e.s);
    });
    C.forEach(e => {
      if (fieldName === "t") e.t.forEach(r => add(r, e.s));
      else add(e[fieldName], e.s);
    });
    pairs.sort((a, b) => b[0].length - a[0].length);
    return pairs;
  }

  const LOOKUP = {
    iast:     buildRevLookup("i"),
    hk:       buildRevLookup("h"),
    velthuis: buildRevLookup("v"),
    wx:       buildRevLookup("w"),
    itrans:   buildRevLookup("t"),
  };

  // ── Build SLP1 → scheme forward map ───────────────────────────────────────
  function buildFwdMap(fieldName) {
    const m = {};
    V.forEach(e => { m[e.s] = (fieldName === "t") ? e.t[0] : e[fieldName]; });
    C.forEach(e => { m[e.s] = (fieldName === "t") ? e.t[0] : e[fieldName]; });
    return m;
  }

  const FORWARD = {
    iast:     buildFwdMap("i"),
    hk:       buildFwdMap("h"),
    velthuis: buildFwdMap("v"),
    wx:       buildFwdMap("w"),
    itrans:   buildFwdMap("t"),
  };

  // ── Devanāgarī → SLP1 ─────────────────────────────────────────────────────
  function devToSLP1(text) {
    let out = "";
    const ch = [...text];   // iterate by Unicode code point
    let i = 0;
    while (i < ch.length) {
      const c = ch[i];
      if (c === "ं")  { out += "M"; i++; continue; }
      if (c === "ः")  { out += "H"; i++; continue; }
      if (c === "ँ")  { out += "~"; i++; continue; }  // chandrabindu (skip/mark)
      if (c === "ऽ")  { out += "'"; i++; continue; }
      if (devVow[c] !== undefined) { out += devVow[c]; i++; continue; }
      if (devCons[c] !== undefined) {
        const cs = devCons[c]; i++;
        const nx = i < ch.length ? ch[i] : null;
        if (nx === HALANT) {
          out += cs; i++;
        } else if (nx && devMat[nx] !== undefined) {
          out += cs + devMat[nx]; i++;
        } else {
          out += cs + "a";  // inherent a
        }
        continue;
      }
      out += c; i++;  // pass through spaces, digits, punctuation
    }
    return out;
  }

  // ── Generic scheme → SLP1 ─────────────────────────────────────────────────
  function toSLP1(text, scheme) {
    scheme = scheme || "slp1";
    text = (text || "").trim();
    if (!text) return text;
    if (scheme === "slp1") return text;
    if (scheme === "devanagari") return devToSLP1(text);
    const lkp = LOOKUP[scheme];
    if (!lkp) return text;
    if (scheme === "iast") text = text.normalize("NFC");
    let out = ""; let i = 0;
    while (i < text.length) {
      let matched = false;
      for (const [repr, s] of lkp) {
        if (text.startsWith(repr, i)) { out += s; i += repr.length; matched = true; break; }
      }
      if (!matched) { out += text[i]; i++; }
    }
    return out;
  }

  // ── SLP1 → Devanāgarī ─────────────────────────────────────────────────────
  function slp1ToDev(text) {
    let out = ""; let i = 0;
    while (i < text.length) {
      const c = text[i];
      if (slp1Dev[c] !== undefined && CONS_SET.has(c)) {
        i++;
        const nx = i < text.length ? text[i] : null;
        if (nx !== null && VOW_SET.has(nx) && nx !== "M" && nx !== "H" && nx !== "'") {
          const mat = slp1Mat[nx];
          out += slp1Dev[c] + (mat === "" ? "" : (mat || ""));
          // mat==="" → inherent a → just write consonant dev char
          i++;
        } else if (nx !== null && CONS_SET.has(nx)) {
          out += slp1Dev[c] + HALANT;  // consonant cluster
        } else {
          // terminal consonant or before M/H
          out += slp1Dev[c] + HALANT;
          // (for display of dhātu like "BU" at end, halant is suppressed by following vowel logic above)
        }
        continue;
      }
      if (VOW_SET.has(c) && c !== "M" && c !== "H" && c !== "'") {
        out += slp1Ind[c] || c; i++; continue;
      }
      if (c === "M") { out += "ं"; i++; continue; }
      if (c === "H") { out += "ः"; i++; continue; }
      if (c === "'") { out += "ऽ"; i++; continue; }
      out += c; i++;
    }
    return out;
  }

  // ── SLP1 → target scheme ───────────────────────────────────────────────────
  function fromSLP1(text, scheme) {
    scheme = scheme || "slp1";
    if (!text) return text;
    if (scheme === "slp1") return text;
    if (scheme === "devanagari") return slp1ToDev(text);
    const fwd = FORWARD[scheme];
    if (!fwd) return text;
    let out = "";
    for (const c of text) out += (fwd[c] !== undefined ? fwd[c] : c);
    return out;
  }

  return { SCHEME_LABELS, toSLP1, fromSLP1,
    preview: (t, s) => { const slp1 = toSLP1(t, s); return { slp1, dev: slp1ToDev(slp1) }; }
  };
})();
