"""
core/analyze.py — word and text analysis by generate-and-test (CONSTITUTION Art. 17).

Two sources *propose* readings of a surface:

- the form index (``engine/form_index``) — cells this engine has generated before;
- Vidyut's kosha (``bench/oracle_kosha``, run in the repo's ``.venv``) — an outside oracle.

A proposal becomes an answer only when the forward engine, run on it now, produces the
input string exactly (any विभाषा branch counts — ``engine.vikalpa.explore``). Nothing here
is a rule; nothing here derives. Each word gets one status:

- ``verified``    — at least one reading re-derives to the surface;
- ``split``       — a sandhi-joined word: Vidyut's Chedaka proposed the parts, the engine derived every
  part and re-joined them (``pipelines/pada_samhita``, vowel seams) into exactly the written word;
- ``avyaya``      — only an indeclinable reading (no sup survives, 2.4.82 — nothing to derive);
- ``oracle_only`` — Vidyut has readings, the engine derives none of them (Art. 18 gap, Art. 19 work item);
- ``unknown``     — nobody proposes anything (sandhi-joined, compound, or outside both lexicons).

Readings are listed avyaya first, then by verdict, each source in its own order. That is
presentation, not ranking: choosing among readings is the kāraka layer's job (ROADMAP §4.5).

Presentation/test code only: never imported by engine / sutras / phonology / pipelines.
"""
from __future__ import annotations

import json
import re
import subprocess
from functools import lru_cache
from pathlib import Path
from typing import Any

from core.transliterate import dev_to_slp1, slp1_to_dev

_ROOT = Path(__file__).resolve().parent.parent
_VENV_PY = _ROOT / ".venv" / "bin" / "python"
_DEV_WORD = re.compile(r"[\u0900-\u0963\u0970-\u097F]+")

LINGA = {"puM": "pulliṅga", "strI": "strīliṅga", "napuMsaka": "napuṃsaka"}
LINGA_DEV = {"pulliṅga": "पुं", "strīliṅga": "स्त्री", "napuṃsaka": "नपुं"}
VIBHAKTI = {"praTamA": 1, "dvitIyA": 2, "tftIyA": 3, "caturTI": 4, "paYcamI": 5,
            "zazWI": 6, "saptamI": 7, "samboDanam": 8}
VIBHAKTI_DEV = ["", "प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी", "पञ्चमी", "षष्ठी", "सप्तमी", "सम्बोधन"]
VACANA = {"eka": 1, "dvi": 2, "bahu": 3}
VACANA_DEV = ["", "एकवचन", "द्विवचन", "बहुवचन"]
PURUSHA = {"praTama": 3, "maDyama": 2, "uttama": 1}
PURUSHA_DEV = ["", "उत्तम", "मध्यम", "प्रथम"]
LAKARA = {"la~w": "laT", "li~w": "liT", "lu~w": "luT", "lf~w": "lRT", "lo~w": "loT", "la~N": "laG",
          "viDili~N": "liG", "ASIrli~N": "AsIrliG", "lu~N": "luG", "lf~N": "lRG"}
LAKARA_DEV = {"laT": "लट्", "liT": "लिट्", "luT": "लुट्", "lRT": "लृट्", "loT": "लोट्", "laG": "लङ्",
              "liG": "विधिलिङ्", "AsIrliG": "आशीर्लिङ्", "luG": "लुङ्", "lRG": "लृङ्"}
PRAYOGA = {"kartari": "kartari", "karmaRi": "karmani", "Bave": "bhave"}
PRAYOGA_DEV = {"kartari": "कर्तरि", "karmani": "कर्मणि", "bhave": "भावे"}
GANA = {"BvAdi": 1, "adAdi": 2, "juhotyAdi": 3, "divAdi": 4, "svAdi": 5, "tudAdi": 6,
        "ruDAdi": 7, "tanAdi": 8, "kryAdi": 9, "curAdi": 10}
SANADI = {"Ric": "nic", "san": "san"}


def tokens(text: str) -> list[str]:
    """Devanāgarī words in reading order (daṇḍas, digits and Latin dropped)."""
    return _DEV_WORD.findall(text)


# ── proposals ────────────────────────────────────────────────────

def _oracle(module: str, words: list[str]) -> list | None:
    """One batch through a Vidyut script in the repo's ``.venv``, or None when the oracle isn't installed."""
    if not _VENV_PY.exists():
        return None
    try:
        r = subprocess.run([str(_VENV_PY), "-m", module], cwd=_ROOT, input=json.dumps(words),
                           capture_output=True, text=True, timeout=120)
        return json.loads(r.stdout) if r.returncode == 0 else None
    except (subprocess.TimeoutExpired, json.JSONDecodeError):
        return None


def _kosha(words: list[str]) -> list[list[dict]] | None:
    """Vidyut's readings per SLP1 word."""
    return _oracle("bench.oracle_kosha", words)


def _cheda(words: list[str]) -> list[list[str]] | None:
    """Vidyut Chedaka's segmentation per SLP1 word (statistical — a proposal only)."""
    return _oracle("bench.oracle_cheda", words)


@lru_cache(maxsize=1)
def _dhatu_rows() -> dict[str, list[dict]]:
    from pipelines.dhatupatha import _envelope, _payload
    by: dict[str, list[dict]] = {}
    for e in _envelope(_payload())["entries"]:
        by.setdefault(e["upadesha_slp1"], []).append(e)
    return by


def dhatu_ids(aupadeshika: str, gana: str, artha: str) -> list[str]:
    """Vidyut's dhātu → engine pāṭha ids. Our upadeśas carry no svara, so homographs
    (शासुँ इच्छायाम् 02.0012 / शासुँ अनुशिष्टौ 02.0070) share a spelling: the artha decides
    when it can; otherwise every row of that gaṇa is tried and generation decides."""
    rows = [r for r in _dhatu_rows().get(re.sub(r"[\\^]", "", aupadeshika), [])
            if GANA.get(gana) in (None, int(r.get("gana") or 0))]
    hit = [r for r in rows if dev_to_slp1(r.get("artha_dev") or "") == artha]
    return [r["dhatupatha_id"] for r in (hit or rows)]


def _from_kosha(k: dict) -> list[dict]:
    """One Vidyut reading → engine requests (one per matching dhātu row), or a not-attempted note."""
    if k["kind"] == "subanta":
        v, n, g = VIBHAKTI.get(k["vibhakti"]), VACANA.get(k["vacana"]), LINGA.get(k["linga"])
        if not k.get("stem"):
            d = k["krdanta"]["dhatu"]
            return [{"kind": "krdanta", "not_attempted": f"kṛdanta stem ({d['clean']} + {k['krdanta']['krt']}) — "
                     "the kṛt spine is not yet an analysis target", "features": {"linga": g, "vibhakti": v, "vacana": n},
                     "lemma": d["clean"]}]
        return [{"kind": "subanta", "stem_slp1": k["stem"], "vibhakti": v, "vacana": n, "linga": g}]
    if k["kind"] == "tinanta":
        d = k["dhatu"]
        base = {"kind": "tinanta", "lakara": LAKARA.get(k["lakara"]), "prayoga": PRAYOGA.get(k["prayoga"]),
                "purusha": PURUSHA.get(k["purusha"]), "vacana": VACANA.get(k["vacana"]),
                "upasargas": d["prefixes"], "lemma": d["clean"]}
        bad = [s for s in d["sanadi"] if s not in SANADI]
        if not base["lakara"] or not base["prayoga"] or bad or len(d["sanadi"]) > 1:
            return [{**base, "not_attempted": f"{k['lakara']} / {k['prayoga']} / sanādi {d['sanadi']} — not an analysis target yet"}]
        ids = dhatu_ids(d["aupadeshika"], d["gana"], d["artha"])
        if not ids:
            return [{**base, "not_attempted": f"dhātu {d['aupadeshika']} ({d['gana']}, {d['artha']}) is not in the engine's dhātupāṭha"}]
        return [{**base, "dhatu_id": i, "sanadi": SANADI[d["sanadi"][0]] if d["sanadi"] else None} for i in ids]
    if k["kind"] == "avyaya":
        return [{"kind": "avyaya", "lemma": k["stem"]}]
    return []


def _from_index(row: dict) -> dict:
    f = row["features"]
    if row["kind"] == "subanta":
        return {"kind": "subanta", "stem_slp1": row["lemma"], "vibhakti": f["vibhakti"], "vacana": f["vacana"],
                "linga": f["linga"]}
    path_id = row["cell_key"].split("@")[1].split(":")[0]
    return {"kind": "tinanta", "dhatu_id": path_id, "lakara": f["lakara"], "prayoga": f.get("prayoga", "kartari"),
            "purusha": f["purusha"], "vacana": f["vacana"], "upasargas": [], "sanadi": None, "lemma": row["lemma"]}


def _index(slp1: str) -> list[dict]:
    from engine.form_index import lookup
    try:
        return lookup(slp1)
    except FileNotFoundError:
        return []


# ── verification ─────────────────────────────────────────────────

def _key(req: dict) -> str:
    return json.dumps({k: v for k, v in req.items() if k not in ("lemma", "source")}, sort_keys=True, ensure_ascii=False)


def rederive(req: dict):
    """Run one reading forward and return the State. asmad / yuṣmad have their own glass-box
    paradigm (7.1.27–7.2.97); everything else is the reader's request shape."""
    from tools.samsaadhanii_reader import derive_request
    if req["kind"] == "subanta" and req["stem_slp1"] in ("asmad", "yuzmad") and 1 <= req["vibhakti"] <= 7:
        from pipelines import asmad_subanta as pr
        return (pr.derive_asmad if req["stem_slp1"] == "asmad" else pr.derive_yuzmad)(req["vibhakti"], req["vacana"])
    return derive_request(req)


def _run(req: dict):
    return lambda: rederive(req)


@lru_cache(maxsize=4096)
def _ubhayapadi(dhatu_id: str) -> bool:
    from pipelines.dhatupatha import resolve_dhatu_identifier
    try:
        return resolve_dhatu_identifier(dhatu_id).get("pada_label_dev") == "उभयपदी"
    except KeyError:
        return False


@lru_cache(maxsize=8192)
def _verify(key: str, surface: str) -> tuple[str, str, str, tuple]:
    """(status, produced_dev, note, vibhāṣā choices) for one request — cached, the engine is deterministic."""
    import contextlib
    import io
    from engine.vikalpa import explore

    req = json.loads(key)
    tries = [req]
    if req["kind"] == "tinanta" and req["prayoga"] == "kartari" and _ubhayapadi(req["dhatu_id"]):
        tries += [{**req, "pada": p} for p in ("parasmai", "atmane")]   # 1.3.72: the sentence picks the pada
    first = None
    for t in tries:
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                branches = explore(_run(t))
        except Exception as e:  # noqa: BLE001 — the engine's own gap, reported as-is
            first = first or ("error", "", f"{type(e).__name__}: {e}"[:200], ())
            continue
        for b in branches:
            if b.surface_slp1 == surface:
                used = tuple((sid, chosen) for sid, chosen in b.choices)
                return "derived", b.surface_dev, f"pada {t['pada']} (ubhayapadī)" if t.get("pada") else "", used
        first = first or ("differs", " / ".join(dict.fromkeys(b.surface_dev for b in branches)), "", ())
    return first or ("error", "", "no derivation", ())


def _label(req: dict) -> str:
    if req["kind"] == "avyaya":
        return f"{slp1_to_dev(req['lemma'])} · अव्यय"
    if req["kind"] in ("subanta", "krdanta"):
        f = req.get("features", req)
        stem = slp1_to_dev(req["stem_slp1"]) if req.get("stem_slp1") else f"कृदन्त ({slp1_to_dev(req['lemma'])})"
        return f"{stem} · {LINGA_DEV.get(f['linga'], '')} · {VIBHAKTI_DEV[f['vibhakti'] or 0]} {VACANA_DEV[f['vacana'] or 0]}"
    pre = "".join(f"{slp1_to_dev(u)}-" for u in req.get("upasargas") or [])
    gana = f" ({req['dhatu_id'].split('.')[0].lstrip('0')})" if req.get("dhatu_id") else ""
    san = {"nic": " + णिच्", "san": " + सन्"}.get(req.get("sanadi") or "", "")
    return (f"{pre}{slp1_to_dev(req['lemma'])}{gana}{san} · {LAKARA_DEV.get(req['lakara'] or '', req['lakara'] or '?')} · "
            f"{PRAYOGA_DEV.get(req['prayoga'] or '', '?')} · {PURUSHA_DEV[req['purusha'] or 0]}पुरुष {VACANA_DEV[req['vacana'] or 0]}")


def _word(dev: str, kosha: list[dict] | None) -> dict[str, Any]:
    slp1 = dev_to_slp1(dev)
    reqs: dict[str, dict] = {}
    for row in _index(slp1):
        r = _from_index(row)
        reqs.setdefault(_key(r), {**r, "source": ["index"]})
    for k in kosha or []:
        for r in _from_kosha(k):
            if r["kind"] == "avyaya":
                reqs.setdefault("avyaya:" + r["lemma"], {**r, "source": ["vidyut"]})
                continue
            if r.get("not_attempted"):
                reqs.setdefault("na:" + r["not_attempted"] + _label(r), {**r, "source": ["vidyut"]})
                continue
            got = reqs.setdefault(_key(r), {**r, "source": []})
            if "vidyut" not in got["source"]:
                got["source"].append("vidyut")
    readings = []
    for key, r in reqs.items():
        out = {"label_dev": _label(r), "source": r["source"],
               "request": {k: v for k, v in r.items() if k not in ("source", "lemma", "features", "not_attempted")}}
        if r["kind"] == "avyaya":
            readings.append({**out, "status": "avyaya", "note": "avyaya — any sup is elided (2.4.82)", "request": None})
            continue
        if r.get("not_attempted"):
            readings.append({**out, "status": "not_attempted", "note": r["not_attempted"], "request": None})
            continue
        status, produced, note, choices = _verify(key, slp1)
        if status != "derived" and slp1.endswith("M"):
            status, produced, note, choices = _verify(key, slp1[:-1] + "m")
            if status == "derived":
                note = "written ं for final म् — 8.3.23 मोऽनुस्वारः (before a consonant in saṃhitā)"
        if choices and status == "derived":
            out["request"]["vibhasha"] = {sid: chosen for sid, chosen in choices}
        if status == "derived" and note.startswith("pada "):
            out["request"]["pada"] = note.split()[1]
        readings.append({**out, "status": status, "produced_dev": produced, "note": note})
    order = ["avyaya", "derived", "differs", "error", "not_attempted"]
    readings.sort(key=lambda x: order.index(x["status"]))
    status = ("verified" if any(x["status"] == "derived" for x in readings)
              else "avyaya" if any(x["status"] == "avyaya" for x in readings)
              else "oracle_only" if readings else "unknown")
    return {"word_dev": dev, "word_slp1": slp1, "status": status, "readings": readings}


def _pausal(part: str) -> str:
    """A Chedaka part as a word on its own: its final s / r is pausal visarga (8.2.66, 8.3.15)."""
    return part[:-1] + "H" if part[-1:] in ("s", "r") and len(part) > 1 else part


def _split(word: dict, parts: list[str], known: dict[str, dict]) -> dict[str, Any]:
    """A proposed segmentation, judged: every part engine-derived, every seam re-joined by the engine."""
    from pipelines.pada_samhita import join, seam_kind

    seams, acc = [], parts[0]
    for left, right in zip(parts, parts[1:]):
        kind = seam_kind(acc, right)
        seam = {"left_dev": slp1_to_dev(_pausal(left)), "right_dev": slp1_to_dev(right), "kind": kind}
        if kind == "ac":
            s = join(acc, right)
            seam |= {"status": "joined", "sutras": [t["sutra_id"] for t in s.trace if t.get("status") == "APPLIED"]}
            acc = s.flat_slp1()
        else:
            seam |= {"status": "gap", "note": f"{kind} seam — the tripāḍī across padas (8.2.66, 8.3, 8.4) is not built yet"}
            acc += right
        seams.append(seam)
    if word["word_slp1"].endswith("H") and acc[-1:] in ("s", "r"):
        acc = acc[:-1] + "H"
    info = [{"dev": slp1_to_dev(_pausal(p)), "status": known[_pausal(p)]["status"],
             "label_dev": next((r["label_dev"] for r in known[_pausal(p)]["readings"] if r["status"] in ("derived", "avyaya")), "")}
            for p in parts]
    rejoined = acc.replace("'", "") == word["word_slp1"].replace("'", "")
    return {"proposer": "vidyut-cheda", "parts": info, "seams": seams, "rejoined_dev": slp1_to_dev(acc),
            "verified": rejoined and all(s["status"] == "joined" for s in seams)
            and all(p["status"] in ("verified", "avyaya") for p in info)}


def analyze(words: list[str]) -> dict[str, Any]:
    """Every word (Devanāgarī) → status + readings, each reading with its verdict; words nobody reads
    get a Chedaka split, accepted (status ``split``) only when the engine derives every part and re-joins them."""
    kosha = _kosha([dev_to_slp1(w) for w in words])
    out = [_word(w, kosha[i] if kosha else None) for i, w in enumerate(words)]
    unknown = [w for w in out if w["status"] == "unknown"]
    cheda = _cheda([w["word_slp1"] for w in unknown]) if unknown else None
    if cheda:
        parts = sorted({_pausal(p) for ps in cheda if len(ps) > 1 for p in ps})
        pk = _kosha(parts) if parts else []
        known = {p: _word(slp1_to_dev(p), pk[i] if pk else None) for i, p in enumerate(parts)}
        for w, ps in zip(unknown, cheda):
            if len(ps) > 1:
                w["split"] = _split(w, ps, known)
                if w["split"]["verified"]:
                    w["status"] = "split"
    counts = {s: sum(1 for w in out if w["status"] == s) for s in ("verified", "split", "avyaya", "oracle_only", "unknown")}
    return {"oracle": kosha is not None, "words": out, "stats": {"total": len(out), **counts}}


def analyze_text(text: str) -> dict[str, Any]:
    """A passage → one entry per line, each a list of analysed words (line breaks kept for verse)."""
    lines = [tokens(ln) for ln in text.splitlines()]
    flat = analyze([w for ln in lines for w in ln])
    it = iter(flat["words"])
    return {**flat, "words": None, "lines": [[next(it) for _ in ln] for ln in lines if ln]}
