"""
webui/search.py — the ONE search used by every lookup box (stem / dhātu / rūpa), GET /api/search.

Index: śabda (static/shabda_index.json), dhātu (pipelines.dhatupatha), rūpa (data/index/forms.db, display only).
Query: Devanāgarī or Latin (SLP1 / IAST / Harvard-Kyoto / plain); the script is detected, the selector is only a hint.
Both sides are reduced to a coarse *fold* (no case, length, aspiration, retroflex/palatal, anusvāra/visarga/anunāsika
distinctions) so "phala", "Pala", "फल", "phalam~" all meet. Rank: exact > normalised-equal > prefix > substring >
meaning > near (edit distance <= 1, or 2 for long words). Tools layer: display only, never read by the engine.
"""
from __future__ import annotations

import json
import re
import sqlite3
import unicodedata
from functools import lru_cache
from pathlib import Path

from flask import Blueprint, jsonify, request

_ROOT = Path(__file__).resolve().parent.parent
bp = Blueprint("search", __name__)

_SLP = str.maketrans({**{c: "" for c in "MH~'"}, "A": "a", "I": "i", "U": "u", "F": "r", "f": "r", "X": "l", "x": "l",
                      "E": "ai", "O": "au", "K": "k", "G": "g", "C": "c", "J": "j", "T": "t", "D": "d", "P": "p",
                      "B": "b", "w": "t", "W": "t", "q": "d", "Q": "d", "N": "n", "Y": "n", "R": "n", "S": "s",
                      "z": "s", "L": "d", "V": "v"})
_DIGRAPH = re.compile(r"(?<=[kgcjtdpbs])h")


def fold_slp1(s: str) -> str:
    """SLP1 -> coarse fold."""
    return re.sub(r"[^a-z]", "", s.translate(_SLP).lower())


def fold_latin(s: str) -> str:
    """Plain Latin / IAST / HK (diacritics already lowercase-safe) -> the same coarse fold."""
    s = unicodedata.normalize("NFD", s.lower().replace("ṃ", "m").replace("ḥ", "h"))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = _DIGRAPH.sub("", s).replace("aa", "a").replace("ii", "i").replace("uu", "u")
    s = s.replace("ṛ", "r").replace("w", "v").replace("y", "y")
    return re.sub(r"[^a-z]", "", s.translate(str.maketrans({"E": "ai", "O": "au"})))


_FINE = str.maketrans({**{c: "" for c in "MH~'"}, "A": "a", "I": "i", "U": "u", "F": "f", "X": "x"})
_IAST = str.maketrans({"ā": "A", "ī": "I", "ū": "U", "ṛ": "f", "ṝ": "F", "ḷ": "x", "ṃ": "M", "ḥ": "H", "ñ": "Y",
                       "ṅ": "N", "ṭ": "w", "ḍ": "q", "ṇ": "R", "ś": "S", "ṣ": "z"})
_ASP = {"kh": "K", "gh": "G", "ch": "C", "jh": "J", "th": "T", "dh": "D", "ph": "P", "bh": "B", "sh": "S"}


def fine_slp1(s: str) -> str:
    """SLP1 minus vowel length, anusvāra/visarga/anunāsika; consonants keep their identity."""
    return s.translate(_FINE)


def latin_to_slp1(s: str) -> str:
    """Best guess for lowercase IAST / HK / plain Latin -> SLP1 (digraph aspirates; ph -> P)."""
    s = s.translate(_IAST)
    return re.sub("|".join(_ASP), lambda m: _ASP[m.group()], s)


def _has_dev(s: str) -> bool:
    return any("ऀ" <= c <= "ॿ" for c in s)


def query_forms(q: str) -> tuple[set[str], set[str], str, bool]:
    """-> (coarse folds, fine keys, SLP1 guess, is_devanagari)."""
    q = q.strip()
    if _has_dev(q):
        from core.transliterate import dev_to_slp1
        slp = dev_to_slp1(re.sub("[ँ]", "", q))
        c, f = ({fold_slp1(slp)} if len(q) > 1 else set()), {fine_slp1(slp)}
        if "क" <= q[-1] <= "ह" and slp.endswith("a"):    # bare consonant: the user is still typing
            c.add(fold_slp1(slp[:-1]) + "$"); f.add(fine_slp1(slp[:-1]) + "$")
        return c, f, slp, True
    c, f = {fold_latin(q)}, {fine_slp1(latin_to_slp1(q.lower() if q.islower() else q))}
    c.add(fold_latin(q).replace("ri", "r"))   # krishna ~ kRSNa
    if re.search(r"[A-Z]", q):          # may be SLP1 as typed
        c.add(fold_slp1(q)); f.add(fine_slp1(q))
    return {x for x in c if x}, {x for x in f if x}, q, False


@lru_cache(maxsize=1)
def _index() -> list[dict]:
    ix: list[dict] = []
    for i, d in enumerate(json.loads((_ROOT / "webui/static/shabda_index.json").read_text(encoding="utf-8"))):
        ix.append({"type": "shabda", "dev": d["w"], "slp": d["slp"], "id": i, "linga": d.get("lc") or d["l"],
                   "gloss": " ".join(x for x in (d.get("a"), d.get("ae")) if x), "gloss_en": d.get("ae", "")})
    from pipelines.dhatupatha import _envelope, _payload
    for e in _envelope(_payload())["entries"]:
        ix.append({"type": "dhatu", "dev": e.get("mula_dhatu_dev", ""), "slp": e.get("upadesha_slp1", ""),
                   "alt": [e.get("citation_dhatu_slp1", ""), e.get("raw_dhatu_after_it_lopa_slp1", ""),
                           e.get("dhatupatha_id", ""), e.get("id", "")],
                   "id": e.get("dhatupatha_id"), "gana": e.get("gana_label_dev", ""),
                   "gloss": " ".join(x for x in (e.get("artha_dev"), e.get("artha_en")) if x), "gloss_en": e.get("artha_en", "")})
    try:   # rūpa: distinct surfaces, one display row each
        con = sqlite3.connect(f"file:{_ROOT / 'data/index/forms.db'}?mode=ro", uri=True)
        seen = set()
        for slp, dev, kind, lemma, feat in con.execute("select surface_slp1,surface_dev,kind,lemma,features from forms"):
            if slp in seen:
                continue
            seen.add(slp)
            f = json.loads(feat)
            ix.append({"type": "rupa", "dev": dev, "slp": slp, "id": lemma, "gloss": "", "gloss_en": "",
                       "info": f"{'tiṅanta' if kind == 'tinanta' else 'subanta'} of {lemma} · " + " ".join(map(str, f.values()))})
        con.close()
    except sqlite3.Error:
        pass
    for r in ix:
        r["fold"] = fold_slp1(r["slp"])
        r["ffine"] = fine_slp1(r["slp"])
        r["affine"] = [fine_slp1(a) for a in r.get("alt", []) if a]
        r["afold"] = [fold_slp1(a) for a in r.get("alt", []) if a]
        r["gl"] = r["gloss"].lower()
    return ix


def _dist(a: str, b: str, cap: int) -> int:
    if abs(len(a) - len(b)) > cap:
        return cap + 1
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


_RANK = {"exact": 0, "normalised": 1, "prefix": 2, "substring": 3, "meaning": 4, "near": 5}
_TYPE = {"shabda": 0, "dhatu": 1, "rupa": 2}


def search(q: str, kind: str = "all", limit: int = 30) -> list[dict]:
    folds, fines, slp, dev = query_forms(q)
    q0 = q.strip()
    if not folds and not q0:
        return []
    kinds = {"all"} if kind in ("", "all") else set(kind.split(","))
    ql = q0.lower()
    out = []
    spaced = " " in q0
    for r in _index():
        if "all" not in kinds and r["type"] not in kinds:
            continue
        best = None   # tier score; a match only on the coarse fold costs +0.5
        if not spaced:
            fk = [r["ffine"], *r["affine"]]
            keys = [r["fold"], *r["afold"]]
            if q0 in (r["dev"], r["slp"]) or q0 in r.get("alt", []):
                best = (0, "exact")
            else:
                for tier, name, fn in ((1, "normalised", lambda k, f: k == f), (2, "prefix", lambda k, f: k.startswith(f)),
                                       (3, "substring", lambda k, f: f in k)):
                    if any(fn(k, f.rstrip("$")) for f in fines if tier > 1 or f[-1] != "$" for k in fk):
                        best = (tier, name)
                        break
                    if r["type"] != "rupa" and any(fn(k, f.rstrip("$")) for f in folds if len(f) > 1 and (tier > 1 or f[-1] != "$") for k in keys):
                        best = (tier + 0.5, name)
                        break
                if dev and not best and q0 in r["dev"]:
                    best = (3, "substring")
                if not best and r["type"] == "shabda" and len(r["ffine"]) > 2 and any(f.startswith(r["ffine"]) for f in fines if f[-1] != "$"):
                    best = (2.9, "stem-of")      # धनम् -> धन
        if not best and len(q0) >= 3 and ql in r["gl"]:
            best = (4, "meaning")
        if best:
            out.append((best[0], len(r["fold"]), _TYPE[r["type"]], r, best[1]))
    if len(out) < limit and folds and max(len(f.rstrip('$')) for f in folds) >= 3:   # ponytail: full scan, fine at ~100k rows
        cap = 2 if max(len(f.rstrip('$')) for f in folds) >= 6 else 1
        for r in _index():
            if ("all" not in kinds and r["type"] not in kinds) or (r["type"] == "rupa" and kinds != {"rupa"}):
                continue   # near-scan of the 90k rūpas only when asked for rūpas alone
            d = min(_dist(f.rstrip('$'), r["fold"], cap) for f in folds)
            if d <= cap and not any(r is o[3] for o in out):
                out.append((5 + d, len(r["fold"]), _TYPE[r["type"]], r, "near"))
    out.sort(key=lambda t: t[:3])
    res = []
    for _, _, _, r, m in out[:limit]:
        res.append({k: r[k] for k in ("type", "dev", "slp", "id") } | {"match": m} | {
            k: r[k] for k in ("linga", "gana", "info") if k in r} | {"gloss": r["gloss"][:160]})
    return res


@bp.get("/api/search")
def api_search():
    kind = request.args.get("kind", "all")
    lim = min(int(request.args.get("limit", 30)), 100000)
    return jsonify(search(request.args.get("q", ""), kind, lim))
