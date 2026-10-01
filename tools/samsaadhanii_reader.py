"""
tools/samsaadhanii_reader.py — e-reader service: Saṃsādhanī annotation, Pāṇinian verification.
─────────────────────────────────────────────────────────────────────────────────────────────────

Backs the web UI's ``/reader`` page. Texts and word annotations come from the
Saṃsādhanī e-reader snapshot (``tools.fetch_samsaadhanii_ereaders --all``,
source #17, Tier-4). The annotation is treated as a **hypothesis**; the
engine is the judge:

* tiṅanta / subanta — the tagged inputs are handed to ``derive()``; the word
  is marked *derived* only if the sūtra chain regenerates the attested form.
* kāraka relations — mapped to the saṃjñā sūtra (1.4.23 ff.) and the
  vibhakti-vidhāyaka sūtra (2.3.x). Where the head is a tiṅanta, 2.3.1
  अनभिहिते decides whether the kāraka is expressed by the lakāra (3.4.69) and
  so takes prathamā (2.3.46) — a Pāṇinian check of the tagged vibhakti.
* samāsa labels — mapped to the samāsa-vidhāyaka sūtra.

Every sūtra text shown is read from ``SUTRA_REGISTRY``, never retyped. This
module is tools-layer (CONSTITUTION Art. 6): it reads ``data/reference/``;
nothing under ``engine/``, ``sutras/`` or ``pipelines/`` imports it.
"""
from __future__ import annotations

import contextlib
import io
import json
import re
from tools import kosha as _kosha
from functools import lru_cache
from pathlib import Path

from core.transliterate import dev_to_slp1
from tools.fetch_samsaadhanii_ereaders import RAW, _clean, _slug, units
from tools.samsaadhanii_tags import (
    SubantaCell, TinantaCell, classify_morph, parse_krdanta_tag,
    parse_subanta_tag, parse_tinanta_tag, align_subanta_linga,
)

ATTRIBUTION = (
    "Word analyses: Saṃsādhanī e-readers, University of Hyderabad "
    "(github.com/samsaadhanii/ereaders, GPL-2.0). Each ✓ is re-derived by the engine."
)

# ── Relation label → Pāṇinian sūtras ──────────────────────────────────────
# Labels are normalised by dropping ``_``, ``-`` and ZWNJ (the corpus spells
# अभिहित_कर्ता / अभिहितकर्ता, नञ्-तत्पुरुषः / नञ्_तत्पुरुषः alike).
RELATION_SUTRAS: dict[str, list[str]] = {
    "कर्ता": ["1.4.54"], "कर्म": ["1.4.49"], "करणम्": ["1.4.42", "2.3.18"],
    "सम्प्रदानम्": ["1.4.32", "2.3.13"], "अपादानम्": ["1.4.24", "2.3.28"],
    "अधिकरणम्": ["1.4.45", "2.3.36"], "कालाधिकरणम्": ["1.4.45", "2.3.36"],
    "देशाधिकरणम्": ["1.4.45", "2.3.36"], "विषयाधिकरणम्": ["1.4.45", "2.3.36"],
    "षष्ठीसम्बन्धः": ["2.3.50"], "सम्बोध्यः": ["2.3.47"], "हेतुः": ["2.3.23"],
    "निर्धारणम्": ["2.3.41"], "प्रयोजककर्ता": ["1.4.55"],
    "अभिहितकर्ता": ["3.4.69"], "अभिहितकर्म": ["3.4.69"],
    "पूर्वकालः": ["3.4.21"], "वर्तमानसमानकालः": ["3.2.124"], "तुमुन्कर्म": ["3.3.10"],
    "भावलक्षणसप्तमीपूर्वकालः": ["2.3.37"],
    "तत्पुरुषः": ["2.1.22"], "षष्ठीतत्पुरुषः": ["2.1.22", "2.2.8"],
    "द्वितीयातत्पुरुषः": ["2.1.22", "2.1.24"], "तृतीयातत्पुरुषः": ["2.1.22", "2.1.30"],
    "चतुर्थीतत्पुरुषः": ["2.1.22", "2.1.36"], "पञ्चमीतत्पुरुषः": ["2.1.22", "2.1.37"],
    "सप्तमीतत्पुरुषः": ["2.1.22", "2.1.40"], "नञ्तत्पुरुषः": ["2.1.22", "2.2.6"],
    "उपपदतत्पुरुषः": ["2.1.22", "2.2.19"], "प्रादितत्पुरुषः": ["2.1.22", "2.2.18"],
    "कर्मधारयः": ["1.2.42"], "बहुव्रीहिः": ["2.2.24"], "द्वन्द्वः": ["2.2.29"],
    "इतरेतरद्वन्द्वः": ["2.2.29"], "अव्ययीभावः": ["2.1.6"],
}
# Fixed vibhakti for kāraka / śeṣa relations (2.3.x), when not abhihita.
_FIXED_VIBHAKTI = {
    "करणम्": (3, "2.3.18"), "सम्प्रदानम्": (4, "2.3.13"), "अपादानम्": (5, "2.3.28"),
    "अधिकरणम्": (7, "2.3.36"), "कालाधिकरणम्": (7, "2.3.36"), "देशाधिकरणम्": (7, "2.3.36"),
    "विषयाधिकरणम्": (7, "2.3.36"), "षष्ठीसम्बन्धः": (6, "2.3.50"), "सम्बोध्यः": (8, "2.3.47"),
}
KIND_SUTRAS = {"avyaya": ["1.1.37", "2.4.82"], "samasa_member": ["1.2.46", "2.4.71"]}
_SAMASA_MARK = ("तत्पुरुषः", "कर्मधारयः", "बहुव्रीहिः", "द्वन्द्वः", "अव्ययीभावः")


def _dash(s) -> str:
    t = (s or "").strip()
    return "" if t in ("", "-", "--") else t


def _norm_label(s: str) -> str:
    return re.sub(r"[_\-\u200c]", "", s.strip())


@lru_cache(maxsize=None)
def _sutra(sid: str) -> dict:
    import sutras  # noqa: F401
    from engine import SUTRA_REGISTRY

    rec = SUTRA_REGISTRY.get(sid)
    return {"id": sid, "text_dev": rec.text_dev if rec else ""}


# ── Snapshot access ────────────────────────────────────────────────────────

def available() -> bool:
    return (RAW / "books.json").is_file()


@lru_cache(maxsize=1)
def catalogue() -> list[dict]:
    if not available():
        return []
    cat = json.loads((RAW / "books.json").read_text(encoding="utf-8"))
    out = []
    for book, p1, p2 in units(cat):
        uid = _slug(book, p1, p2)
        if not (RAW / f"{uid}.analysis.json").is_file():
            continue
        out.append({"id": uid, "book": book, "part1": p1, "part2": p2,
                    "label": " / ".join(x for x in (book, p1, p2) if x),
                    "chapters": chapters(uid)})
    return out


@lru_cache(maxsize=12)
def _rows(uid: str) -> dict[tuple[str, str], list[dict]]:
    path = RAW / f"{uid}.analysis.json"
    if RAW.resolve() not in path.resolve().parents:
        raise KeyError(uid)
    by: dict[tuple[str, str], list[dict]] = {}
    for r in json.loads(path.read_text(encoding="utf-8")):
        by.setdefault((r["chaptno"], r["slokano"]), []).append(r)
    return by


@lru_cache(maxsize=12)
def _slokas(uid: str) -> dict[tuple[str, str], list[str]]:
    path = RAW / f"{uid}.slokas.json"
    if not path.is_file():
        return {}
    return {(s["chaptno"], s["slokano"]): [p.strip() for p in s["sparts"]]
            for s in json.loads(path.read_text(encoding="utf-8"))}


def chapters(uid: str) -> list[str]:
    return sorted({c for c, _ in _rows(uid)}, key=_num_key)


def _num_key(s: str) -> tuple:
    return tuple(int(x) if x.isdigit() else 0 for x in re.split(r"[^0-9]+", s.strip()) if x) or (0,)


def verses(uid: str, chapter: str) -> list[dict]:
    keys = sorted({s for c, s in _rows(uid) if c == chapter}, key=_num_key)
    text = _slokas(uid)
    return [{"sloka": s, "text": text.get((chapter, s), [])} for s in keys]


# ── Engine verification ───────────────────────────────────────────────────

@contextlib.contextmanager
def _quiet():
    with contextlib.redirect_stdout(io.StringIO()):
        yield


@lru_cache(maxsize=4096)
def _derive_tinanta(key: str, fields: str) -> tuple[str, str, str]:
    """(status, produced_slp1, produced_dev) — cached on the cell key."""
    from pipelines.tinanta import derive

    c = TinantaCell(**json.loads(fields))
    try:
        with _quiet():
            s = derive(c.dhatu_id, c.lakara, c.prayoga, c.purusha, c.vacana, **c.derive_kwargs())
        return "ok", s.flat_slp1(), s.flat_dev()
    except Exception as e:  # noqa: BLE001 — surfaced to the reader as-is
        return "error", "", f"{type(e).__name__}: {e}"[:200]


@lru_cache(maxsize=8192)
def _derive_subanta(stem: str, v: int, vac: int, linga: str) -> tuple[str, str, str]:
    from pipelines.subanta import derive

    try:
        with _quiet():
            if stem == "asmad" and 1 <= v <= 7:  # dedicated glass-box paradigm (7.1.27–7.2.97)
                from pipelines.asmad_subanta import derive_asmad
                s = derive_asmad(v, vac)
            else:
                s = derive(stem, v, vac, linga=linga)
        return "ok", s.flat_slp1(), s.flat_dev()
    except Exception as e:  # noqa: BLE001
        return "error", "", f"{type(e).__name__}: {e}"[:200]


def tinanta_request(c: TinantaCell) -> dict:
    return {"kind": "tinanta", **{k: v for k, v in c.as_dict().items() if k != "tag"}}


def subanta_request(c: SubantaCell) -> dict:
    return {"kind": "subanta", "stem_slp1": c.stem_slp1, "vibhakti": c.vibhakti,
            "vacana": c.vacana, "linga": c.linga}


def verify(kind: str, tag: str, word_slp1: str) -> dict:
    """Engine verdict for one annotated word."""
    out: dict = {"status": "not_attempted", "sutras": [_sutra(s) for s in KIND_SUTRAS.get(kind, [])]}
    if kind == "tinanta":
        c = parse_tinanta_tag(tag)
        out["inputs"] = c.as_dict()
    elif kind == "subanta":
        c = parse_subanta_tag(tag)
        c = align_subanta_linga(c, word_slp1)
        out["inputs"] = c.as_dict()
    else:
        out["note"] = {"avyaya": "avyaya — sup is attached and elided (2.4.82)",
                       "samasa_member": "samāsa member — internal sup elided (2.4.71)",
                       "krdanta": "kṛdanta — vidhāyaka sūtra shown; the kṛt spine is not yet a reader target"}.get(kind, "")
        if kind == "krdanta":
            c = parse_krdanta_tag(tag)
            out["inputs"] = c.as_dict()
            if c.vidhana_sutra:
                out["sutras"] = [_sutra(c.vidhana_sutra)]
            if c.unresolved:
                out["note"] = c.unresolved
        return out
    if c.unresolved:
        out.update(status="unresolved", note=c.unresolved)
        return out
    if kind == "tinanta":
        fields = json.dumps({k: v for k, v in c.as_dict().items()}, ensure_ascii=False, sort_keys=True)
        st, slp, dev = _derive_tinanta(c.key(), fields)
        out["request"] = tinanta_request(c)
    else:
        st, slp, dev = _derive_subanta(c.stem_slp1, c.vibhakti, c.vacana, c.linga)
        out["request"] = subanta_request(c)
    if st == "error":
        out.update(status="error", note=dev)
    else:
        out.update(status="derived" if slp == word_slp1 else "differs",
                   produced_slp1=slp, produced_dev=dev)
    return out


def derive_request(req: dict):
    """Re-run a reader request (from ``verify()['request']``) and return the State."""
    if req.get("kind") == "tinanta":
        from pipelines.tinanta import derive

        fields = {k: req.get(k) for k in TinantaCell.__dataclass_fields__ if k != "tag"}
        c = TinantaCell(tag="", **fields)
        c.upasargas = list(c.upasargas or [])
        return derive(c.dhatu_id, c.lakara, c.prayoga, int(c.purusha), int(c.vacana), **c.derive_kwargs())
    if req.get("kind") == "subanta":
        from pipelines.subanta import derive

        return derive(req["stem_slp1"], int(req["vibhakti"]), int(req["vacana"]),
                      linga=req.get("linga") or "pulliṅga")
    raise ValueError(f"unknown request kind {req.get('kind')!r}")


# ── Kāraka / samāsa relations ─────────────────────────────────────────────

def _relation(raw: str) -> dict | None:
    first = (raw or "").split(";")[0].strip()
    if first in ("", "-"):
        return None
    label, _, target = first.partition(",")
    key = _norm_label(label)
    return {"label": label.strip(), "key": key, "target": target.strip(),
            "sutras": [_sutra(s) for s in RELATION_SUTRAS.get(key, [])]}


def vibhakti_check(rel: dict, word: dict, head: dict | None) -> dict | None:
    """Does the tagged vibhakti follow from the kāraka by 2.3.x?"""
    sub = (word.get("engine") or {}).get("inputs") or {}
    v = sub.get("vibhakti")
    if word["kind"] != "subanta" or not v:
        return None
    key = rel["key"]
    if key in _FIXED_VIBHAKTI:
        exp, sid = _FIXED_VIBHAKTI[key]
        why = f"{rel['label']} → {sid}"
    elif key in ("कर्ता", "कर्म") and head and head["kind"] == "tinanta":
        prayoga = ((head.get("engine") or {}).get("inputs") or {}).get("prayoga")
        if not prayoga:
            return None
        abhihita = (key == "कर्ता" and prayoga == "kartari") or (key == "कर्म" and prayoga == "karmani")
        if abhihita:
            exp, sid = 1, "2.3.46"
            why = f"{rel['label']} expressed by the lakāra ({prayoga}, 3.4.69) → 2.3.1 blocks, 2.3.46 prathamā"
        else:
            exp, sid = (3, "2.3.18") if key == "कर्ता" else (2, "2.3.2")
            why = f"{rel['label']} unexpressed (2.3.1 अनभिहिते, verb {prayoga}) → {sid}"
    else:
        return None
    return {"expected": exp, "found": v, "ok": v == exp, "sutra": _sutra(sid), "why": why}


# ── Kāraka tree (SCL-style: verb at the root, dependents hang down) ────────

def karaka_tree(words: list[dict]) -> dict:
    """Dependents point at their head via ``kaaraka_sambandha``. The verb's
    ``अभिहित_*`` tag is a comment on 3.4.69, not a second parent — skip it so
    the tiṅanta stays the root (same geometry as Saṃsādhanī's Graphviz)."""
    ids = {w["anvaya_no"] for w in words if w.get("anvaya_no")}
    parent: dict[str, str] = {}
    edges: list[dict] = []
    for w in words:
        rel = w.get("relation")
        hid = (rel or {}).get("target")
        if not rel or hid not in ids or hid == w["anvaya_no"]:
            continue
        if w["kind"] == "tinanta" and rel["key"].startswith("अभिहित"):
            continue
        parent[w["anvaya_no"]] = hid
        edges.append({
            "dep": w["anvaya_no"], "head": hid, "label": rel["label"],
            "key": rel["key"], "samasa": any(m in rel["key"] for m in _SAMASA_MARK),
            "sutras": [s["id"] for s in rel.get("sutras") or []],
        })
    children: dict[str, list[str]] = {}
    for dep, head in parent.items():
        children.setdefault(head, []).append(dep)
    for kids in children.values():
        kids.sort(key=_num_key)
    kind_of = {w["anvaya_no"]: w["kind"] for w in words if w.get("anvaya_no")}
    roots = sorted((a for a in kind_of if a not in parent),
                   key=lambda a: (kind_of[a] != "tinanta", _num_key(a)))
    return {"roots": roots, "children": children, "edges": edges, "parent": parent}


# ── Verse assembly ────────────────────────────────────────────────────────

def verse(uid: str, chapter: str, sloka: str) -> dict:
    rows = _rows(uid).get((chapter, sloka))
    if rows is None:
        raise KeyError(f"{uid} {chapter}.{sloka}")
    sentences: dict[str, list[dict]] = {}
    for r in rows:
        word_dev, surface = _clean(r.get("word") or "")
        if word_dev in (".", "") and (r.get("morph_in_context") or "-") == "-":
            continue
        kind, tag = classify_morph(r.get("morph_in_context") or "")
        w = {
            "sentno": r.get("sentno"), "anvaya_no": r.get("anvaya_no"), "poem": r.get("poem"),
            "word": r.get("word"), "word_dev": word_dev, "text_surface": surface,
            "sandhied_word": _dash(r.get("sandhied_word")), "bgcolor": (r.get("bgcolor") or "").strip(),
            "morph": r.get("morph_in_context"), "kind": kind,
            "relation_raw": r.get("kaaraka_sambandha"), "relation": _relation(r.get("kaaraka_sambandha")),
            "possible_relations": _dash(r.get("possible_relations")),
            "samasa": _dash(r.get("samAsa")), "prayoga": _dash(r.get("prayoga")),
            "sarvanama": _dash(r.get("sarvanAma")), "name_class": _dash(r.get("name_classification")),
            "hindi": _dash(r.get("hindi_meaning")), "english": _dash(r.get("english_meaning")),
        }
        w["engine"] = verify(kind, tag, dev_to_slp1(word_dev))
        w["kosha"] = _kosha.lookup(word_dev, limit=3)
        sentences.setdefault(str(r.get("sentno")), []).append(w)

    out_sents, counts = [], {"derived": 0, "differs": 0, "error": 0, "unresolved": 0, "not_attempted": 0}
    for sentno, words in sentences.items():
        by_anvaya = {w["anvaya_no"]: w for w in words}
        for w in words:
            counts[w["engine"]["status"]] += 1
            rel = w["relation"]
            if rel:
                w["vibhakti_check"] = vibhakti_check(rel, w, by_anvaya.get(rel["target"]))
        out_sents.append({
            "sentno": sentno,
            "words": words,
            "anvaya": sorted(words, key=lambda w: _num_key(w["anvaya_no"] or "0")),
            "tree": karaka_tree(words),
        })
    padas = _slokas(uid).get((chapter, sloka), [])
    return {"unit": uid, "chapter": chapter, "sloka": sloka,
            "text": padas, "spans": _verse_spans(padas, out_sents),
            "sentences": out_sents, "counts": counts, "attribution": ATTRIBUTION}


def coverage(uid: str, chapter: str) -> dict:
    """Whole-chapter tally + gap list (differs/error/unresolved), for the learner's gap view."""
    counts = {"derived": 0, "differs": 0, "error": 0, "unresolved": 0, "not_attempted": 0}
    gaps = []
    for v in verses(uid, chapter):
        r = verse(uid, chapter, v["sloka"])
        for s in r["sentences"]:
            for w in s["words"]:
                st = w["engine"]["status"]
                counts[st] += 1
                if st in ("differs", "error", "unresolved"):
                    gaps.append({"sloka": v["sloka"], "word": w["word_dev"], "status": st,
                                 "produced": w["engine"].get("produced_dev"), "note": w["engine"].get("note")})
    return {"counts": counts, "gaps": gaps}


def _verse_spans(padas: list[str], sentences: list[dict]) -> list[list[dict]]:
    """Split each pāda into clickable sandhied-word spans (keys = ``sent|anvaya_no``)."""
    by: dict[str, list[str]] = {}
    for si, sent in enumerate(sentences):
        for w in sent["words"]:
            sw = w.get("sandhied_word") or ""
            if sw:
                by.setdefault(sw, []).append(f"{si}|{w['anvaya_no']}")
    out = []
    for pada in padas:
        hits: list[tuple[int, int, str]] = []
        for sw in sorted(by, key=len, reverse=True):
            start = 0
            while True:
                j = pada.find(sw, start)
                if j < 0:
                    break
                hits.append((j, j + len(sw), sw))
                start = j + max(len(sw), 1)
        hits.sort()
        segs, last = [], 0
        for a, b, sw in hits:
            if a < last:
                continue
            if a > last:
                segs.append({"text": pada[last:a], "keys": []})
            segs.append({"text": sw, "keys": by[sw]})
            last = b
        if last < len(pada):
            segs.append({"text": pada[last:], "keys": []})
        out.append(segs or [{"text": pada, "keys": []}])
    return out


def search(uid: str, q: str, limit: int = 80) -> list[dict]:
    """Gavēṣikā-style search over one book's word annotations (no derivation)."""
    q = (q or "").strip()
    if not q:
        return []
    hits = []
    for (ch, sl), rows in _rows(uid).items():
        for r in rows:
            blob = " ".join(_dash(r.get(k)) for k in
                            ("word", "sandhied_word", "morph_in_context", "hindi_meaning",
                             "english_meaning", "kaaraka_sambandha"))
            if q not in blob:
                continue
            hits.append({
                "chapter": ch, "sloka": sl, "word": r.get("word"),
                "morph": r.get("morph_in_context"), "anvaya_no": r.get("anvaya_no"),
                "hindi": _dash(r.get("hindi_meaning")),
            })
            if len(hits) >= limit:
                return hits
    return hits


# ── Export ────────────────────────────────────────────────────────────────

_STATUS_DEV = {"derived": "✓ सिद्धम्", "differs": "✗ भिन्नम्", "error": "! त्रुटिः",
               "unresolved": "? अनिर्णीतम्", "not_attempted": "—"}


def export_rows(v: dict) -> list[list]:
    """Horizontal table, one row per field — Saṃsādhanī's XLSX layout plus
    the engine's rows."""
    fields = [
        ("Word", lambda w: w["word"]), ("anvaya_no", lambda w: w["anvaya_no"]),
        ("morph_in_context", lambda w: w["morph"]), ("kaaraka_sambandha", lambda w: w["relation_raw"]),
        ("hindi_meaning", lambda w: w.get("hindi") or ""),
        ("samAsa", lambda w: w.get("samasa") or ""),
        ("possible_relations", lambda w: w.get("possible_relations") or ""),
        ("engine_status", lambda w: _STATUS_DEV[w["engine"]["status"]]),
        ("engine_form", lambda w: w["engine"].get("produced_dev", "")),
        ("pāṇinian_sūtras", lambda w: " ".join(s["id"] for s in
                                               (w["relation"] or {}).get("sutras", []) + w["engine"]["sutras"])),
        ("vibhakti_check", lambda w: "" if not w.get("vibhakti_check") else
            ("✓ " if w["vibhakti_check"]["ok"] else "✗ ") + w["vibhakti_check"]["sutra"]["id"]),
    ]
    rows = []
    for name, get in fields:
        row = [name]
        for s in v["sentences"]:
            row += [get(w) or "" for w in s["anvaya"]] + [f"#{len(s['anvaya'])}" if name == "Word" else ""]
        rows.append(row)
    return rows


def export_xlsx(v: dict) -> bytes:
    from openpyxl import Workbook

    wb = Workbook()
    ws = wb.active
    ws.title = f"{v['chapter']}_{v['sloka']}"
    for row in export_rows(v):
        ws.append(row)
    ws.append([])
    ws.append([ATTRIBUTION])
    buf = io.BytesIO()
    wb.save(buf)
    return buf.getvalue()


def data_root() -> Path:
    return RAW
