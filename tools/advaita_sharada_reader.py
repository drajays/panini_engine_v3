"""
tools/advaita_sharada_reader.py — /reader service for Advaita Sharada: Prasthānatrayī-bhāṣya, prakaraṇas, stotras.
─────────────────────────────────────────────────────────────────────────────────────────────

Two sources, each used for what it is:

* **Text and structure** — Advaita Sharada (Sringeri), local cache from
  ``tools.fetch_advaita_sharada``: mūla, avatārikā, bhāṣya and the
  Ānandagiri-ṭīkā aligned to bhāṣya passages. "All rights reserved": read
  locally, every passage links back to its page.
* **Word analyses** — Tamal Maharaj's word-level reader (CC BY 4.0, from
  ``tools.fetch_prasthanatrayi_words``): every mūla word with padaccheda,
  grammar and gloss; the bhāṣya as a surface-form dictionary.

The analyses are hypotheses. Each grammar string is rewritten as a Saṃsādhanī
tag and judged by ``samsaadhanii_reader.verify`` — the engine re-derives the
attested pada or the word is not ✓ (Art. 17). Where the string names no gaṇa,
the dhātupāṭha's candidate gaṇas are tried and the one whose derivation reaches
the attested form is kept (analysis proposes, generation verifies).

Tools layer (CONSTITUTION Art. 6): reads ``data/reference/``; nothing under
``engine/``, ``sutras/`` or ``pipelines/`` imports it.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from functools import lru_cache

from core.transliterate import dev_to_slp1
from tools import samsaadhanii_reader as _rd
from tools.fetch_advaita_sharada import RAW as AS_RAW, RIGHTS
from tools.fetch_prasthanatrayi_words import ATTRIBUTION as WORDS_ATTRIBUTION, RAW as WORDS_RAW
from tools.samsaadhanii_tags import GANA, LAKARA, _dhatu_index, _upasarga

PREFIX = "as:"
TEXT_ATTRIBUTION = (f"Text: Advaita Sharada, advaitasharada.sringeri.net — {RIGHTS} Local reading copy; "
                    f"each passage links to its page.")
ATTRIBUTION = TEXT_ATTRIBUTION + " " + WORDS_ATTRIBUTION

# Advaita Sharada slug → Tamal deposit work key.
WORDS_KEY = {
    "aitareya-bhashya": "Aitareya", "brahmasutra-bhashya": "BS", "brihadaranyaka-bhashya": "Brha",
    "chandogya-bhashya": "Chandogya", "bhagavadgita-bhashya": "Gita", "isha-bhashya": "Isha",
    "kathaka-bhashya": "Kathaka", "kena-pada-bhashya": "Kena_pada", "kena-vakya-bhashya": "Kena_vakya",
    "mandukya-karika-bhashya": "Mandukya", "mundaka-bhashya": "Mundaka", "prashna-bhashya": "Prashna",
    "taittiriya-bhashya": "Taitiriya",
}
# The site's own sections (its सम्पादनालय "विभागः" list), in its order.
GROUPS = {
    "prasthanatraya-bhashya": "प्रस्थानत्रयभाष्याणि", "shankara-prakarana": "शाङ्कराः प्रकरणग्रन्थाः",
    "shankara-stotra": "शाङ्कराणि स्तोत्राणि", "itara-prakarana": "इतरे प्रकरणग्रन्थाः", "itara-grantha": "इतरे ग्रन्थाः",
}
_SLUG = re.compile(r"^[a-z0-9-]+$")


def available() -> bool:
    return any(p.name != "cite-maps-index.json" for p in AS_RAW.glob("*.json"))


@lru_cache(maxsize=48)
def _doc(slug: str) -> dict:
    path = AS_RAW / f"{slug}.json"
    if not _SLUG.match(slug) or slug == "cite-maps-index" or not path.is_file():
        raise KeyError(slug)
    return json.loads(path.read_text(encoding="utf-8"))


def _slug(uid: str) -> str:
    if not uid.startswith(PREFIX):
        raise KeyError(uid)
    return uid[len(PREFIX):]


def ref_of(mula_id: str) -> str:
    """``BR_C01_S05_V16`` → ``1.5.16`` (the deposit's verse key)."""
    return ".".join(str(int(n)) for n in re.findall(r"\d+", mula_id.split("_", 1)[1]))


# ── Passage grouping: each mūla with what precedes and comments on it ──────

@lru_cache(maxsize=64)
def _verses(slug: str, chunk: str) -> tuple[dict, ...]:
    page = next((p for p in _doc(slug)["pages"] if p["chunk"] == chunk), None)
    if page is None:
        raise KeyError(f"{slug}/{chunk}")
    tika = {v["code"]: v for v in page["vyakhya"]}
    # a reading item is a mūla unit; a work with no mūla (Vedāntasāra, Advaitasiddhi …) is read paragraph by paragraph
    kinds = Counter(u["kind"] for p in _doc(slug)["pages"] for u in p["units"])
    anchor = "mula" if kinds["mula"] else max(("prose", "bhashya"), key=lambda k: kinds[k])
    out: list[dict] = []
    pending: list[dict] = []
    cur = None
    for u in page["units"]:
        p = {**u, "tika": [{"code": c, "title": v["title"], "slug": v["slug"], "rows": v["aligned"][u["id"]]}
                           for c, v in tika.items() if u["id"] in v["aligned"]]}
        if u["kind"] == anchor:
            cur = {"id": u["id"], "ref": ref_of(u["id"]), "mula": p, "pre": pending, "post": []}
            out.append(cur)
            pending = []
        elif cur and (u["id"].lower().startswith(cur["id"].lower() + "_") or u["kind"] in ("bhashya", "colophon")
                      and u["kind"] != anchor):
            cur["post"].append(p)
        else:
            pending.append(p)
    if out and pending:
        out[-1]["post"].extend(pending)
    return tuple(out)


def catalogue() -> list[dict]:
    docs = []
    for path in sorted(AS_RAW.glob("*.json")):
        try:
            docs.append(_doc(path.stem))
        except KeyError:
            continue
    order = list(GROUPS)
    docs.sort(key=lambda d: order.index(d.get("group")) if d.get("group") in order else len(order))
    return [{"id": PREFIX + d["slug"], "source": "advaita_sharada", "group": d.get("group"),
             "group_label": GROUPS.get(d.get("group"), ""), "book": d["title"], "label": d["title"],
             "words": d["slug"] in WORDS_KEY, "chapters": [p["chunk"] for p in d["pages"]]} for d in docs]


def verses(uid: str, chapter: str) -> list[dict]:
    return [{"sloka": v["id"], "ref": v["ref"], "text": v["mula"]["text"].split("\n")}
            for v in _verses(_slug(uid), chapter)]


# ── Grammar string → Saṃsādhanī tag → engine verdict ──────────────────────

_VIB = {"प्रथमा": 1, "द्वितीया": 2, "तृतीया": 3, "चतुर्थी": 4, "पञ्चमी": 5, "षष्ठी": 6, "सप्तमी": 7,
        "सम्बोधन": 8, "सम्बोधनम्": 8}
_VAC = {"एक": "एक", "एकवचन": "एक", "द्वि": "द्वि", "द्विवचन": "द्वि", "बहु": "बहु", "बहुवचन": "बहु"}
_LIN = {"पुं": "पुं", "पुंलिङ्ग": "पुं", "पुंल्लिङ्ग": "पुं", "पुल्लिङ्ग": "पुं", "स्त्री": "स्त्री",
        "स्त्रीलिङ्ग": "स्त्री", "नपुं": "नपुं", "नपुंसक": "नपुं", "नपुंसकलिङ्ग": "नपुं"}
_LAK = {**{k: k for k in LAKARA}, "लिङ्": "विधिलिङ्"}
_PUR = {"प्रथमपुरुष": "प्र", "प्रथम": "प्र", "प्र.पु.": "प्र", "मध्यमपुरुष": "म", "मध्यम": "म", "म.पु.": "म",
        "उत्तमपुरुष": "उ", "उत्तम": "उ", "उ.पु.": "उ"}
_PADA = {"परस्मैपद": "परस्मैपदी", "परस्मै": "परस्मैपदी", "पर": "परस्मैपदी",
         "आत्मनेपद": "आत्मनेपदी", "आत्मने": "आत्मनेपदी"}
_GANA_NAME = {k.rstrip("ः"): k for k in GANA}
_GANA_BY_NO = {v: k for k, v in GANA.items()}
_SANADI = {"णिच्": "णिच्", "णिजन्त": "णिच्", "सन्": "सन्", "सनन्त": "सन्"}
_KRT_AVYAYA = {"क्त्वा": "क्त्वा", "क्त्वान्त": "क्त्वा", "ल्यप्": "ल्यप्", "ल्यबन्त": "ल्यप्",
               "तुमुन्": "तुमुन्", "तुमुन्नन्त": "तुमुन्", "णमुल्": "णमुल्"}
_DIGITS = str.maketrans("०१२३४५६७८९", "0123456789")


def _tokens(s: str) -> list[str]:
    return [t for t in re.split(r"[·\s,;()=/]+", s) if t]


@lru_cache(maxsize=1)
def _ganas_of() -> dict[str, list[int]]:
    _by_upadesha, by_raw = _dhatu_index()
    out: dict[str, set[int]] = {}
    for (dev, g) in by_raw:
        if isinstance(g, int):
            out.setdefault(dev, set()).add(g)
    return {k: sorted(v) for k, v in out.items()}


def _gana_hint(toks: list[str]) -> int | None:
    for t in toks:
        t2 = t.translate(_DIGITS)
        if t2.isdigit() and 1 <= int(t2) <= 10:
            return int(t2)
        base = re.sub(r"(गणः|गण|ः)$", "", t)
        if base in _GANA_NAME:
            return GANA[_GANA_NAME[base]]
    return None


def tags_for(g: str) -> tuple[str, list[str], str | None]:
    """(kind, candidate Saṃsādhanī tags, unresolved reason) for one ``+``-part of a grammar string."""
    g = re.split(r"\s+—\s+", g.strip())[0]
    toks = _tokens(g)
    vib = next((_VIB[t] for t in toks if t in _VIB), None)
    vac = next((_VAC[t] for t in toks if t in _VAC), None)
    lak = next((_LAK[t] for t in toks if t in _LAK), None)
    if "√" in g and lak and vib is None:
        m = re.search(r"√\s*([^\s·(,+]+)", g)
        dhatu = m.group(1) if m else ""
        pur = next((_PUR[t] for t in toks if t in _PUR), None)
        pada = next((_PADA[t] for t in toks if t in _PADA), "")
        prayoga = "कर्मणि" if "कर्मणि" in toks else "भावे" if "भावे" in toks else "कर्तरि"
        sanadi = next((_SANADI[t] for t in toks if t in _SANADI), None)
        ups: list[str] = []
        for t in re.split(r"[\s·,;()+\-√=]+", g):
            if t and t != dhatu and _upasarga(t) and t not in ups:
                ups.append(t)
        if not dhatu or not pur or not vac:
            return "tinanta", [], "grammar string lacks dhātu / puruṣa / vacana"
        hint = _gana_hint(toks)
        ganas = [hint] if hint else _ganas_of().get(dhatu, [])
        if not ganas:
            return "tinanta", [], f"dhātu {dhatu} not in the dhātupāṭha index"
        head = "_".join(ups + [dhatu])
        pre = [sanadi] if sanadi else []
        return "tinanta", [f"{head}{{{';'.join(pre + [prayoga, lak, pur, vac, pada, _GANA_BY_NO[n]])}}}"
                           for n in ganas], None
    if "अव्यय" in toks and vib is None:
        stem = next((t for t in toks if t != "अव्यय"), "")
        return "avyaya", [f"{stem}{{अव्य}}"], None
    krt = next((_KRT_AVYAYA[t] for t in toks if t in _KRT_AVYAYA), None)
    if krt and vib is None:
        return "krdanta", [f"{toks[0].lstrip('√')}{{कृत्_प्रत्ययः:{krt}}}"], None
    if vib is not None:
        stem = toks[0].replace("-", "")
        if stem.startswith("√"):
            return "subanta", [], "kṛdanta stem not given (only the dhātu)"
        lins = [_LIN[x] for t in toks for x in t.split("/") if x in _LIN] or ["पुं", "नपुं", "स्त्री"]
        if stem in ("अस्मद्", "युष्मद्"):
            lins = ["पुं"]
        if not vac:
            return "subanta", [], "no vacana"
        return "subanta", [f"{stem}{{{lin};{vib};{vac}}}" for lin in dict.fromkeys(lins)], None
    return "none", [], None


def _attested(p: str) -> str:
    return p.replace("-", "").replace("ऽ", "").strip()


@lru_cache(maxsize=16384)
def _judge(p: str, g: str) -> str:
    kind, tags, why = tags_for(g)
    word = _attested(p)
    if why:
        return json.dumps({"kind": kind, "engine": {"status": "unresolved", "note": why, "sutras": []}},
                          ensure_ascii=False)
    if not tags:
        return json.dumps({"kind": kind, "engine": {"status": "not_attempted", "sutras": []}}, ensure_ascii=False)
    best = None
    for tag in tags:
        v = _rd.verify(kind, tag, dev_to_slp1(word))
        v["tag"] = tag
        if v["status"] == "derived":
            if len(tags) > 1 and kind == "tinanta":
                v["note"] = ((v.get("note") or "") + f" gaṇa {tag.rsplit(';', 1)[-1].rstrip('}')} "
                             "inferred: the dhātupāṭha row whose derivation reaches the text").strip()
            best = v
            break
        if best is None or (best["status"] in ("error", "unresolved") and v["status"] == "differs"):
            best = v
    return json.dumps({"kind": kind, "engine": best}, ensure_ascii=False)


def analyse(p: str, g: str, m: str = "", c: str = "") -> list[dict]:
    """One analysed word → its ``+``-parts, each with an engine verdict."""
    ps, gs = p.split(" + "), g.split(" + ")
    if len(ps) != len(gs):
        ps, gs = [p], [g]
    out = []
    for pp, gg in zip(ps, gs):
        j = json.loads(_judge(pp.strip(), gg.strip()))
        out.append({"p": pp.strip(), "word_dev": _attested(pp), "g": gg.strip(), **j})
    return out


@lru_cache(maxsize=1)
def _mula_words() -> dict[str, dict[str, list[dict]]]:
    out: dict[str, dict[str, list[dict]]] = {}
    for f in WORDS_RAW.glob("prasthan-words-*.json"):
        out.update(json.loads(f.read_text(encoding="utf-8")))
    return out


@lru_cache(maxsize=1)
def _bhashya_dict() -> dict[str, dict]:
    path = WORDS_RAW / "bhasya-words-ALL.json"
    return json.loads(path.read_text(encoding="utf-8")).get("ALL", {}) if path.is_file() else {}


def _clean_token(t: str) -> str:
    return re.sub(r"[।॥|,;:!?‘’“”'\"()\[\]\-—–०-९0-9]+", "", t).strip()


def _spans(lines: list[str], words: list[dict]) -> list[list[dict]]:
    """Mūla lines as segments; each whitespace token is matched in order to its analysed word."""
    i, out = 0, []
    for line in lines:
        segs = []
        for tok in re.split(r"(\s+)", line):
            key = None
            if tok.strip() and i < len(words) and _clean_token(tok) == _clean_token(words[i]["w"]):
                key, i = i, i + 1
            segs.append({"text": tok, "key": key})
        out.append(segs)
    return out


def verse(uid: str, chapter: str, sloka: str) -> dict:
    slug = _slug(uid)
    v = next((x for x in _verses(slug, chapter) if x["id"] == sloka), None)
    if v is None:
        raise KeyError(f"{uid} {chapter} {sloka}")
    raw = _mula_words().get(WORDS_KEY.get(slug, ""), {}).get(v["ref"], []) if v["mula"]["kind"] == "mula" else []
    words = [{"i": i, "w": w["w"], "p": w["p"], "g": w["g"], "m": w.get("m", ""), "c": w.get("c", ""),
              "parts": analyse(w["p"], w["g"])} for i, w in enumerate(raw)]
    lines = v["mula"]["text"].split("\n")
    # yuṣmad / asmad are judged in their pāda (8.1.20–26): text-ordered parts, a sandhi token per analysed word
    seq = [{"anvaya_no": "", "sandhied_word": w["w"] if j == 0 else "", "word_dev": p["word_dev"],
            "kind": p["kind"], "engine": p["engine"]} for w in words for j, p in enumerate(w["parts"])]
    for k, s in enumerate(seq, 1):
        s["anvaya_no"] = str(k)
    _rd._enclitic_pass(lines, {"1": seq})
    counts = {"derived": 0, "differs": 0, "error": 0, "unresolved": 0, "not_attempted": 0}
    for w in words:
        for part in w["parts"]:
            counts[part["engine"]["status"]] += 1
    page = next(p for p in _doc(slug)["pages"] if p["chunk"] == chapter)
    return {
        "source": "advaita_sharada", "unit": uid, "chapter": chapter, "sloka": sloka, "ref": v["ref"],
        "url": f"{page['url']}#{sloka}", "text": lines, "spans": _spans(lines, words), "words": words,
        "anchor_kind": v["mula"]["kind"], "pre": v["pre"], "mula": v["mula"], "post": v["post"], "counts": counts,
        # one pseudo-sentence of all parts, so the Vidyut cross-check attaches like any reader verse
        "sentences": [{"words": [p for w in words for p in w["parts"]]}],
        "attribution": ATTRIBUTION if slug in WORDS_KEY else TEXT_ATTRIBUTION,
    }


def coverage(uid: str, chapter: str) -> dict:
    """Whole-chapter tally of the mūla words + gap list, for the learner's gap view."""
    counts = {"derived": 0, "differs": 0, "error": 0, "unresolved": 0, "not_attempted": 0}
    gaps = []
    for v in verses(uid, chapter):
        r = verse(uid, chapter, v["sloka"])
        for w in r["words"]:
            for p in w["parts"]:
                st = p["engine"]["status"]
                counts[st] += 1
                if st in ("differs", "error", "unresolved"):
                    gaps.append({"sloka": v["ref"], "word": p["word_dev"], "status": st,
                                 "produced": p["engine"].get("produced_dev"), "note": p["engine"].get("note")})
    return {"counts": counts, "gaps": gaps}


def bhashya_word(surface: str) -> dict:
    """A bhāṣya word looked up in the deposit's surface dictionary, then judged by the engine."""
    s = _clean_token(surface)
    e = _bhashya_dict().get(s)
    if not e:
        return {"surface": s, "found": False}
    return {"surface": s, "found": True, "p": e.get("p", ""), "g": e.get("g", ""), "m": e.get("m", ""),
            "c": e.get("c", ""), "parts": analyse(e.get("p", ""), e.get("g", ""))}


def search(uid: str, q: str, limit: int = 80) -> list[dict]:
    """Substring search over mūla, bhāṣya and ṭīkā of one work (Devanāgarī)."""
    q = (q or "").strip()
    if not q:
        return []
    slug, hits = _slug(uid), []
    for page in _doc(slug)["pages"]:
        for v in _verses(slug, page["chunk"]):
            for p in [*v["pre"], v["mula"], *v["post"]]:
                texts = [p.get("text", "")] + [r["text"] for t in p["tika"] for r in t["rows"]]
                hit = next((t for t in texts if q in t), None)
                if hit is None:
                    continue
                j = hit.find(q)
                hits.append({"chapter": page["chunk"], "sloka": v["id"], "ref": v["ref"], "kind": p["kind"],
                             "word": hit[max(0, j - 20): j + len(q) + 20]})
                if len(hits) >= limit:
                    return hits
                break
    return hits
