"""
core/vyutpatti.py — how is a word made? Kośas propose, rules verify (CONSTITUTION Art. 17: analysis proposes, generation
verifies). Plan: docs/ABHYASA_PLAN.md §8.

Proposals (each labelled with its source):
  * the kośa entries in Subhastini's lexicon (``$PANINI_LEXDB``, default ~/subhastini/lexicon/lex.db: Śabdakalpadruma,
    Vācaspatyam, Bhāratīkośa, Apte …): sūtra numbers (४ । १ । १०५ / ४.१.१०५), quoted sūtra texts (“गर्गादिभ्यो यञ्”),
    formulas (गर्ग+यञ्+ङीप्, गॄ - ग), "इति X" pratyaya mentions, dhātu + artha (गॄ … शब्दे);
  * Kāśikā udāharaṇas (docs/data/sutras.json): the sūtras that cite this very word;
  * the uṇādi pāṭha (data/inputs/unadi_patha.json): sūtras whose SK examples give the word;
  * Vidyut generate-and-test over likely bases / dhātus when no kośa speaks.
Verification of a proposal: Vidyut regenerates the word from base + pratyaya (its sūtra path is shown); each cited
sūtra's Kāśikā examples are checked for the word; our engine's status for each cited sūtra (sig/sutra_class.json) is
shown, and the engine itself re-derives the word on request (``engine_check``).

Presentation code: never imported by engine / sutras / phonology / pipelines; nothing here reaches a cond().
"""
from __future__ import annotations

import json
import os
import re
import sqlite3
from functools import cache, lru_cache
from pathlib import Path
from typing import Any

from core.transliterate import dev_to_slp1, slp1_to_dev

ROOT = Path(__file__).resolve().parent.parent
LEXDB = Path(os.environ.get("PANINI_LEXDB", Path.home() / "subhastini" / "lexicon" / "lex.db"))
VY_SOURCES = ("skd", "vcp", "bharati", "apte-hi", "apte-en", "shs", "wil", "md")   # entries that carry vyutpatti
MEANING_SOURCES = ("apte-hi", "apte-en")
STRI = {"wAp": "टाप्", "cAp": "चाप्", "qAp": "डाप्", "NIp": "ङीप्", "NIz": "ङीष्", "NIn": "ङीन्", "UN": "ऊङ्", "ti": "ति"}
DEVNUM = str.maketrans("०१२३४५६७८९", "0123456789")
_SEP = r"\s*(?:\+|--|–|-)\s*"
_DW = r"[\u0900-\u0963\u0971-\u097F]+"
FORMULA = re.compile(rf"({_DW}(?:{_SEP}{_DW})+)")
NUM = re.compile(r"([१-८1-8])\s*[।.\s]\s*([१-४1-4])\s*[।.\s]\s*([०-९0-9]{1,3})")
QUOTE = re.compile(r"[“\"‘]([^”\"’]{3,80})[”\"’]")
ITI = re.compile(rf"इति\s+({_DW})")


def dev(s: str) -> str:
    return " ".join(slp1_to_dev(w) for w in s.split()) if s else ""


def _norm(t: str) -> str:
    return re.sub(r"[\s।॥.,;:\-–—“”\"'‘’()\[\]0-9०-९]", "", t or "")


# ── data ─────────────────────────────────────────────────────────────────────────────────────────

def lexdb() -> sqlite3.Connection | None:
    if not LEXDB.exists():
        return None
    con = sqlite3.connect(f"file:{LEXDB}?mode=ro", uri=True, check_same_thread=False)
    return con


@cache
def _registry() -> dict[str, str]:
    import sutras  # noqa: F401 — fills SUTRA_REGISTRY
    from engine import SUTRA_REGISTRY
    return {sid: r.text_dev for sid, r in SUTRA_REGISTRY.items() if r.text_dev}


@cache
def _sutra_by_text() -> dict[str, str]:
    return {_norm(t): sid for sid, t in _registry().items()}


@cache
def _unadi() -> list[dict[str, Any]]:
    try:
        return json.loads((ROOT / "data" / "inputs" / "unadi_patha.json").read_text(encoding="utf-8"))["entries"]
    except FileNotFoundError:
        return []


@cache
def _unadi_by_text() -> dict[str, dict]:
    return {_norm(e["sutra_dev"]): e for e in _unadi()}


@cache
def _kashika() -> dict[str, dict]:
    try:
        return json.loads((ROOT / "docs" / "data" / "sutras.json").read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}


@cache
def _kashika_index() -> dict[str, list[str]]:
    """Every word of every Kāśikā udāharaṇa line → the sūtras that cite it."""
    idx: dict[str, list[str]] = {}
    for sid, r in _kashika().items():
        for line in r.get("ex") or []:
            for w in re.findall(_DW, line):
                lst = idx.setdefault(w, [])
                if sid not in lst:
                    lst.append(sid)
    return idx


@cache
def _status() -> dict[str, str]:
    try:
        return {r["id"]: r["status"] for r in json.loads((ROOT / "sig" / "sutra_class.json").read_text())["rows"]}
    except FileNotFoundError:
        return {}


@cache
def _pratyayas() -> dict[str, str]:
    """Pratyaya upadeśas the proposals can name: kṛt + taddhita (Vidyut's inventory), strī, uṇādi. SLP1 → kind."""
    from core.abhyasa import vidyut
    names = vidyut({"op": "names"}) or {}
    out = {n: "krt" for n in names.get("krt", [])}
    out.update({n: "taddhita" for n in names.get("taddhita", [])})
    out.update({n: "stri" for n in STRI})
    for e in _unadi():
        for p in (e.get("pratyaya_slp1") or "").replace(",", " ").split():
            out.setdefault(p, "unadi")
    return out


@cache
def _dhatus_by_mula() -> dict[str, list[dict]]:
    from core.abhyasa import dhatu_pool
    by: dict[str, list[dict]] = {}
    for d in dhatu_pool():
        by.setdefault(d["dev"], []).append(d)
    return by


def _sutra(sid: str, kind: str = "ashtadhyayi", via: str = "") -> dict[str, Any]:
    if kind == "unadi":
        e = next((x for x in _unadi() if x["id"] == sid), None)
        return {"id": f"उ.{e['pada']}.{e['no']}" if e else str(sid), "text": e["sutra_dev"] if e else "", "kind": "unadi",
                "via": via, "examples": e.get("examples_sk", "")[:300] if e else ""}
    return {"id": sid, "text": _registry().get(sid, ""), "kind": kind, "via": via, "engine": _status().get(sid, "")}


# ── proposals from the kośas ─────────────────────────────────────────────────────────────────────

def kosha_entries(word_dev: str, sources=VY_SOURCES, limit: int = 12) -> list[dict[str, Any]]:
    con = lexdb()
    if con is None:
        return []
    labels = dict(con.execute("select code, label from src"))
    out = []
    for src in sources:
        for (i,) in con.execute("select id from dict where src=? and word=? limit 3", (src, word_dev)):
            row = con.execute("select body from tx where src=? and id=?", (src, i)).fetchone()
            if row:
                out.append({"src": src, "label": labels.get(src, src), "body": row[0]})
        if len(out) >= limit:
            break
    con.close()
    return out


def _parse(body: str) -> dict[str, Any]:
    """One kośa entry → the sūtras, formula parts, pratyayas and dhātus it names."""
    head = body[:600]
    sutras: list[dict] = []
    for m in NUM.finditer(head):
        a, p, n = (x.translate(DEVNUM) for x in m.groups())
        sid = f"{a}.{p}.{n}"
        if sid in _registry() and "उणा" not in head[max(0, m.start() - 12):m.start()]:
            sutras.append(_sutra(sid, via="number"))
    for m in QUOTE.finditer(head):
        key = _norm(m.group(1))
        if key in _sutra_by_text():
            sutras.append(_sutra(_sutra_by_text()[key], via="quote"))
        elif key in _unadi_by_text():
            sutras.append(_sutra(_unadi_by_text()[key]["id"], "unadi", "quote"))
    seen, uniq = set(), []
    for s in sutras:
        if s["id"] not in seen:
            seen.add(s["id"])
            uniq.append(s)
    known = _pratyayas()
    tok_p = lambda t: next((x for x in (dev_to_slp1(t), dev_to_slp1(t.rstrip("ः")), dev_to_slp1(t.rstrip("ः")) + "") if x in known), None)  # noqa: E731
    formulas = []
    for m in FORMULA.finditer(head):
        parts = [p for p in re.split(_SEP, m.group(1)) if p]
        prs = [tok_p(p) for p in parts[1:]]
        if parts and all(prs):
            formulas.append({"base_dev": parts[0], "pratyayas": prs})
    iti = [p for p in (tok_p(t) for t in ITI.findall(head)) if p]
    dhatus = []
    for tok in set(re.findall(_DW, head)):
        for d in _dhatus_by_mula().get(tok, []):
            artha = (d["artha"] or "").split()[0] if d["artha"] else ""
            if artha and artha in head:
                dhatus.append(d)
    return {"sutras": uniq, "formulas": formulas, "iti": iti, "dhatus": dhatus}


# ── verification ────────────────────────────────────────────────────────────────────────────────

def _nominatives(stem: str, linga: str | None) -> dict[str, list[str]]:
    from core.abhyasa import vidyut
    out = {}
    for lg in ([linga] if linga else ["pulliṅga", "strīliṅga", "napuṃsaka"]):
        g = vidyut({"op": "subgrid", "stem": stem, "linga": lg}) or []
        if g and g[0]:
            out[lg] = g[0]
    return out


def _vidyut_check(base: str, prs: list[str], forms: set[str], linga: str | None, dhatus: list[dict]) -> list[dict]:
    """Does Vidyut regenerate the word from this base (or dhātu) + pratyaya? Returns the hits with their sūtra paths."""
    from core.abhyasa import vidyut
    known = _pratyayas()
    lingas = [linga] if linga else None
    hits: list[dict] = []
    tad = [p for p in prs if known.get(p) == "taddhita"]
    krt = [p for p in prs if known.get(p) == "krt"]
    if tad and base:
        for h in vidyut({"op": "taddhita_reverse", "forms": sorted(forms), "bases": [base], "lingas": lingas}) or []:
            if h["pratyaya"] in tad:
                hits.append({**h, "kind": "taddhita"})
    if krt and dhatus:
        for h in vidyut({"op": "krt_reverse", "forms": sorted(forms), "dhatus": [[d["upadesha"], d["ref"]] for d in dhatus],
                         "lingas": lingas}) or []:
            if h["krt"] in krt:
                hits.append({**h, "kind": "krdanta"})
    for h in hits:
        h["path"] = [{"id": s["code"], "text": _registry().get(s["code"], "")} for s in h.pop("steps")]
    return hits


def _vidyut_forms(base: str, prs: list[str], linga: str | None, dhatus: list[dict]) -> list[dict]:
    """What Vidyut actually makes from the proposal (shown beside the word, so a near miss is visible)."""
    from core.abhyasa import vidyut
    known, out = _pratyayas(), []
    lg = linga or "pulliṅga"
    for p in prs:
        if known.get(p) == "taddhita" and base:
            v = vidyut({"op": "taddhita", "stem": base, "names": [p], "linga": lg}) or {}
            out += [{"pratyaya": p, "forms_dev": [dev(f) for f in v.get(p, [])]}]
        elif known.get(p) == "krt" and dhatus:
            d = dhatus[0]
            v = vidyut({"op": "krt", "upadesha": d["upadesha"], "path_id": d["ref"], "krts": [p]}) or {}
            key = {"pulliṅga": "pum", "strīliṅga": "stri", "napuṃsaka": "napum"}[lg]
            out += [{"pratyaya": p, "forms_dev": [dev(f) for f in (v.get(p) or {}).get(key, [])]}]
    return out


def _unadi_hits(word_dev: str, nom_devs: list[str]) -> list[dict]:
    keys = {word_dev, *nom_devs}
    out = []
    for e in _unadi():
        toks = set(re.findall(_DW, e.get("examples_sk", "")))
        if toks & keys:
            out.append(_sutra(e["id"], "unadi", "example"))
    return out


def _kashika_hits(word_dev: str, nom_devs: list[str]) -> list[dict]:
    idx = _kashika_index()
    sids: list[str] = []
    for w in [word_dev, *nom_devs]:
        for s in idx.get(w, []):
            if s not in sids:
                sids.append(s)
    return [{**_sutra(s, via="kashika"), "examples": " · ".join((_kashika().get(s, {}).get("ex") or [])[:4])} for s in sids[:12]]


@cache
def _mw_keys() -> frozenset[str]:
    con = lexdb()
    if con is None:
        return frozenset()
    try:
        return frozenset(k for (k,) in con.execute("select distinct k1 from mw"))
    finally:
        con.close()


def _is_word(stem: str) -> bool:
    from core.abhyasa import corpus
    return stem in _mw_keys() or any(k[0] == stem for k in corpus())


def _guess_bases(word: str) -> list[str]:
    """Bases a taddhita word may come from: undo ādi-vṛddhi, cut the ending (generate-and-test only)."""
    undo = {"A": ["a"], "E": ["i", "e"], "O": ["u", "o"]}
    firsts = [word]
    m = re.search(r"[aAiIuUfFeEoO]", word)
    if m and m.group() in undo:
        firsts += [word[:m.start()] + v + word[m.end():] for v in undo[m.group()]]
    m2 = re.search(r"Ar", word)
    if m2:
        firsts.append(word[:m2.start()] + "f" + word[m2.end():])
    out = []
    for w in firsts:
        for k in range(2, len(w)):
            stem = w[:k]
            for cand in (stem + "a", stem) if stem[-1] not in "aAiIuUfFeEoO" else (stem,):
                if len(cand) >= 2 and cand not in out:
                    out.append(cand)
    return out[:40]


@lru_cache(maxsize=256)
def explain(word: str, linga: str = "", depth: int = 2) -> dict[str, Any]:
    """The व्युत्पत्ति tree of ``word`` (SLP1 stem): proposals with sources, each verified; recursion on the base."""
    word_dev = dev(word)
    noms = _nominatives(word, linga or None)
    forms = {f for fs in noms.values() for f in fs}
    nom_devs = [dev(f) for f in forms]
    entries = kosha_entries(word_dev) or [e for nd in nom_devs for e in kosha_entries(nd)]
    props: dict[tuple, dict] = {}
    for e in entries:
        pr = _parse(e["body"])
        chains = [(f["base_dev"], tuple(f["pratyayas"])) for f in pr["formulas"]]
        if not chains and (pr["iti"] or pr["dhatus"]):
            base_dev = pr["dhatus"][0]["dev"] if pr["dhatus"] else ""
            chains = [(base_dev, tuple(p for p in pr["iti"]))]
        for base_dev, prs in chains:
            key = (base_dev, prs)
            p = props.setdefault(key, {"base_dev": base_dev, "base": dev_to_slp1(base_dev) if base_dev else "",
                                       "pratyayas": list(prs), "pratyayas_dev": [dev(x) if x not in STRI else STRI[x] for x in prs],
                                       "sources": [], "sutras": [], "dhatus": []})
            p["sources"].append({"src": e["src"], "label": e["label"], "text": e["body"][:420]})
            for s in pr["sutras"]:
                if s["id"] not in {x["id"] for x in p["sutras"]}:
                    p["sutras"].append(s)
            for d in pr["dhatus"] or _dhatus_by_mula().get(base_dev, []):
                if d["ref"] not in {x["ref"] for x in p["dhatus"]}:
                    p["dhatus"].append(d)
    for key, p in list(props.items()):
        if not p["base"]:
            twin = next((q for q in props.values() if q["base"] and q["pratyayas"] == p["pratyayas"]), None)
            if twin:
                twin["sources"] += p["sources"]
                twin["sutras"] += [x for x in p["sutras"] if x["id"] not in {y["id"] for y in twin["sutras"]}]
                del props[key]
    out_props = []
    kas = _kashika_hits(word_dev, nom_devs)
    kas_ids = {k["id"] for k in kas}
    uni_toks = set(nom_devs) | {word_dev}
    for p in props.values():
        p["vidyut"] = _vidyut_check(p["base"], p["pratyayas"], forms, linga or None, p["dhatus"]) if forms else []
        for s_ in p["sutras"]:
            s_["kashika_has_word"] = (s_["id"] in kas_ids if s_["kind"] != "unadi"
                                      else bool(set(re.findall(_DW, s_.get("examples", ""))) & uni_toks))
        p["vidyut_forms"] = _vidyut_forms(p["base"], p["pratyayas"], linga or None, p["dhatus"])
        p["kinds"] = [_pratyayas().get(x, "") for x in p["pratyayas"]]
        p["dhatus"] = [{"ref": d["ref"], "dev": d["dev"], "artha": d["artha"], "upadesha": d["upadesha"]} for d in p["dhatus"][:4]]
        p["verdict"] = ("vidyut" if p["vidyut"] else "") + ("+kashika" if any(s.get("kashika_has_word") for s in p["sutras"]) else "")
        out_props.append(p)
    out_props.sort(key=lambda p: (-len(p["sources"]), -bool(p["vidyut"]), -len(p["sutras"])))
    search: list[dict] = []
    if not any(p["vidyut"] for p in out_props) and forms:           # no kośa chain Vidyut confirms: generate and test
        from core.abhyasa import vidyut
        for h in vidyut({"op": "taddhita_reverse", "forms": sorted(forms), "bases": [b for b in _guess_bases(word) if _is_word(b)],
                         "lingas": [linga] if linga else None}) or []:
            h["path"] = [{"id": s["code"], "text": _registry().get(s["code"], "")} for s in h.pop("steps")]
            search.append({**h, "kind": "taddhita"})
        from core.abhyasa import dhatu_pool
        first = word.lstrip("aAiIuUeo")[:1]
        cands = [d for d in dhatu_pool() if dev_to_slp1(d["dev"])[:1] == first][:250]
        for h in vidyut({"op": "krt_reverse", "forms": sorted(forms), "dhatus": [[d["upadesha"], d["ref"]] for d in cands],
                         "lingas": [linga] if linga else None}) or []:
            h["path"] = [{"id": s["code"], "text": _registry().get(s["code"], "")} for s in h.pop("steps")]
            search.append({**h, "kind": "krdanta"})
    node = {"word": word, "word_dev": word_dev, "nominatives": {k: [dev(x) for x in v] for k, v in noms.items()},
            "meanings": [{"src": e["src"], "label": e["label"], "text": e["body"][:300]} for e in
                         (kosha_entries(word_dev, MEANING_SOURCES, 2) or [x for nd in nom_devs for x in kosha_entries(nd, MEANING_SOURCES, 2)])][:3],
            "proposals": out_props[:6], "kashika": kas, "unadi": _unadi_hits(word_dev, nom_devs), "search": search[:8],
            "lexdb": LEXDB.exists()}
    best = next((p for p in out_props if p["base"] and p["base"] != word and not p["dhatus"]), None)
    if depth > 1 and best:
        node["base_tree"] = explain(best["base"], "", depth - 1)
    return node


def engine_check(kind: str, base: str, pratyaya: str, linga: str, word: str, dhatu_ref: str = "",
                 sutras: tuple[str, ...] = (), want_forms: tuple[str, ...] = ()) -> dict[str, Any]:
    """Our engine's own attempt at the proposal: every branch it can reach, and whether one is the word."""
    import contextlib
    import io

    from engine.vikalpa import explore
    want = set(want_forms) or set((_nominatives(word, linga) or {}).get(linga, []))
    if kind == "taddhita":
        from pipelines.taddhita_loop import derive_taddhita
        key = lambda x: tuple(int(n) for n in x.split(".")[:3] if n.isdigit())  # noqa: E731
        arthas = [{"taddhitArtha": "apatya", "apatyaBeda": "gotra"}] if any((4, 1, 98) <= key(x) <= (4, 1, 112) for x in sutras) else []
        arthas += [{"taddhitArtha": a} for a in ("apatya", "asti", "vikAra", "devatA", "Seza", "Bava", "jAta")]
        runs = [(a, (lambda a=a: derive_taddhita(base, 1, 1, linga, **a))) for a in arthas]
    else:
        from core.abhyasa import KRT_VIVAKSHA_ENGINE
        from pipelines.krdanta import derive_krdanta
        viv = KRT_VIVAKSHA_ENGINE.get(pratyaya, [{}])
        runs = [(v, (lambda v=v: derive_krdanta(dhatu_ref, 1, 1, linga, **v))) for v in viv]
    tried = []
    for viv, fn in runs:
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                branches = explore(fn)
        except Exception as ex:  # noqa: BLE001 — the engine's own gap is the answer
            tried.append({"vivaksha": viv, "error": f"{type(ex).__name__}: {ex}"[:200]})
            continue
        got = []
        for b in branches:
            tag = [x.split(":", 1)[1] for t in b.state.terms for x in t.tags if x.startswith("origin_pratyaya:")]
            got.append({"form": b.surface_slp1, "form_dev": dev(b.surface_slp1), "pratyaya": tag[-1] if tag else ""})
            if b.surface_slp1 in want:
                return {"match": True, "vivaksha": viv, "form_dev": dev(b.surface_slp1), "state": b.state, "tried": tried}
        tried.append({"vivaksha": viv, "got": got})
        if any(g["pratyaya"] == pratyaya for g in got):
            break                          # the engine reached the pratyaya but not the word: that is the gap
    return {"match": False, "want_dev": [dev(w) for w in want], "tried": tried}
