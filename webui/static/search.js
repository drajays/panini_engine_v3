/* search.js — client of the one search, GET /api/search (webui/search.py). Used by the stem, dhātu and matrix boxes.
   SSearch.ranked(q, kind) -> Promise<[{type,dev,slp,id,match,linga,gana,info,gloss}]>, best first; kind = shabda|dhatu|rupa|csv|all.
   SSearch.debounce(fn, ms) -> debounced fn. SSearch.tag(m) -> short label of the match kind. */
window.SSearch = (() => {
  const TAG = {exact: "exact", normalised: "≈ translit", prefix: "prefix", substring: "contains", "stem-of": "stem of", meaning: "meaning", near: "near"};
  const cache = new Map();
  const ranked = (q, kind = "all", limit = 100000) => {
    q = (q || "").trim(); if (!q) return Promise.resolve([]);
    const k = `${kind}|${limit}|${q}`;
    if (!cache.has(k)) cache.set(k, fetch(`/api/search?kind=${encodeURIComponent(kind)}&limit=${limit}&q=${encodeURIComponent(q)}`).then(r => r.json()).catch(() => []));
    return cache.get(k);
  };
  const debounce = (fn, ms = 180) => { let t; return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); }; };
  return {ranked, debounce, tag: m => TAG[m] || m};
})();
