"""
core/abhyasa.py — अभ्यासशाला: every sanskritabhyas.in drill, answered by our engine, cross-checked.
──────────────────────────────────────────────────────────────────────────────────────────────

Plan, sources and answer-key rule: docs/ABHYASA_PLAN.md.  In short:

* a cell's answer is the **engine's** form (pipelines.subanta / tinanta / krdanta / taddhita_loop / pada_samhita);
* it is **agreed** when Vidyut (tools/abhyasa_vidyut, run under .venv) or the printed ashtadhyayi.com paradigm has it too;
* where the engine cannot derive yet (sanādi stacks, nāmadhātu, some kṛts …) the drill may use Vidyut's form, and the
  question carries that source (``sources``) so the page can say so; disagreements are kept in ``GAPS`` for the engine
  agents (also written by tools/build_abhyasa_bank.py to data/practice/abhyasa_gaps.json).

Families (sanskritabhyas menus): noun · pronoun · number · verb · krdanta · taddhita · namadhatu · sandhi · varna ·
plus ours: vakya (sentence writing, RKMVU model), pratyahara, it.
Drills: mcq (शुद्ध विकल्प चुनें) · recall (रूप का स्मरण) · match (सही मेल) · tf (सही या गलत) · odd (असमान पद) ·
table (पूर्ण रूप) · sutra (कः सूत्रः) · compose / karaka (vākya).

Presentation code: never imported by engine / sutras / phonology / pipelines.
"""
from __future__ import annotations

import contextlib
import io
import json
import random
import subprocess
import threading
import time
from functools import cache, lru_cache
from pathlib import Path
from typing import Any

from core.transliterate import dev_to_slp1, slp1_to_dev

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / "data" / "practice" / "abhyasa_bank.json"
VENV_PY = ROOT / ".venv" / "bin" / "python"

LEVELS = [
    {"id": 1, "dev": "आसानम्", "hi": "आसान", "en": "Easy"},
    {"id": 2, "dev": "मध्यमम्", "hi": "मध्यम", "en": "Medium"},
    {"id": 3, "dev": "कठिनम्", "hi": "कठिन", "en": "Hard"},
    {"id": 4, "dev": "वैयाकरणः", "hi": "वैयाकरण", "en": "Grammarian"},
]
DRILLS = {
    "mcq": {"dev": "शुद्धं विकल्पं चिनुत", "hi": "शुद्ध विकल्प चुनें", "en": "Choose the right form"},
    "recall": {"dev": "रूपं स्मरत", "hi": "रूप का स्मरण करें", "en": "Recall the form"},
    "match": {"dev": "समीचीनं मेलयत", "hi": "सही मेल बनाएँ", "en": "Match"},
    "tf": {"dev": "सत्यम् असत्यं वा", "hi": "सही या गलत बताएं", "en": "True or false"},
    "odd": {"dev": "असमानं पदं चिनुत", "hi": "असमान पद चुनें", "en": "Odd one out"},
    "table": {"dev": "पूर्णं रूपं लिखत", "hi": "पूर्ण रूप भरें", "en": "Fill the whole table"},
    "sutra": {"dev": "कः सूत्रः?", "hi": "कौन सा सूत्र?", "en": "Which sūtra?"},
    "compose": {"dev": "वाक्यं रचयत", "hi": "वाक्य बनाएँ", "en": "Write the sentence"},
    "karaka": {"dev": "कारकं चिनुत", "hi": "कारक पहचानें", "en": "Name the kāraka"},
}
FAMILIES = {   # drills a family supports, in sanskritabhyas order
    "noun": {"dev": "संज्ञा", "en": "Nouns", "drills": ["mcq", "recall", "match", "tf", "odd", "table", "sutra"]},
    "pronoun": {"dev": "सर्वनाम", "en": "Pronouns", "drills": ["mcq", "recall", "match", "tf", "odd", "table", "sutra"]},
    "number": {"dev": "संख्या", "en": "Numerals", "drills": ["mcq", "recall", "match", "tf", "table"]},
    "verb": {"dev": "क्रियापदम्", "en": "Verbs", "drills": ["mcq", "recall", "match", "tf", "odd", "table", "sutra"]},
    "krdanta": {"dev": "कृदन्तम्", "en": "Kṛdanta", "drills": ["recall", "mcq", "match", "tf"]},
    "taddhita": {"dev": "तद्धितान्तम्", "en": "Taddhitānta", "drills": ["recall", "mcq", "tf"]},
    "namadhatu": {"dev": "नामधातुः", "en": "Nāmadhātu", "drills": ["mcq", "recall", "tf", "table"]},
    "sandhi": {"dev": "सन्धिः", "en": "Sandhi", "drills": ["mcq", "recall", "tf", "sutra"]},
    "varna": {"dev": "वर्णाः", "en": "Letters", "drills": ["tf", "mcq", "recall", "match"]},
    "pratyahara": {"dev": "प्रत्याहाराः", "en": "Pratyāhāras", "drills": ["tf", "mcq", "recall"]},
    "it": {"dev": "इत्संज्ञा", "en": "it-letters", "drills": ["mcq", "recall"]},
    "vakya": {"dev": "वाक्याभ्यासः", "en": "Sentences", "drills": ["compose", "karaka"]},
}
VIBHAKTI = ["", "प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी", "पञ्चमी", "षष्ठी", "सप्तमी", "सम्बोधनम्"]
VACANA = ["", "एकवचनम्", "द्विवचनम्", "बहुवचनम्"]
PURUSHA = ["", "उत्तमपुरुषः", "मध्यमपुरुषः", "प्रथमपुरुषः"]       # engine: 1 = uttama … 3 = prathama
LINGA = {"pulliṅga": "पुंलिङ्गम्", "strīliṅga": "स्त्रीलिङ्गम्", "napuṃsaka": "नपुंसकलिङ्गम्"}
LAKARA = {"laT": "लट्", "liT": "लिट्", "luT": "लुट्", "lRT": "लृट्", "loT": "लोट्", "laG": "लङ्", "liG": "विधिलिङ्",
          "AsIrliG": "आशीर्लिङ्", "luG": "लुङ्", "lRG": "लृङ्"}
PRAYOGA = {"kartari": "कर्तरि", "karmani": "कर्मणि"}
GANA = ["", "भ्वादिः", "अदादिः", "जुहोत्यादिः", "दिवादिः", "स्वादिः", "तुदादिः", "रुधादिः", "तनादिः", "क्र्यादिः", "चुरादिः"]
UPASARGA = ["ati", "aDi", "anu", "apa", "api", "aBi", "ava", "A", "ut", "upa", "dur", "dus", "ni", "nir", "nis", "parA",
            "pari", "pra", "prati", "vi", "sam", "su"]
SANADI = {"Ric": "णिच्", "san": "सन्", "yaN": "यङ्", "yaNluk": "यङ्लुक्", "Ric+san": "णिच् + सन्", "san+Ric": "सन् + णिच्",
          "yaN+san": "यङ् + सन्", "yaN+Ric": "यङ् + णिच्"}
KRTS = ["lyuw", "anIyar", "Rvul", "tumun", "tavya", "tfc", "ktvA", "ktavatu", "kta", "Satf", "SAnac", "yat", "ac", "ap",
        "ktin", "GaY"]
KRT_DEV = {"lyuw": "ल्युट्", "anIyar": "अनीयर्", "Rvul": "ण्वुल्", "tumun": "तुमुँन्", "tavya": "तव्य", "tfc": "तृच्",
           "ktvA": "क्त्वा", "ktavatu": "क्तवतुँ", "kta": "क्त", "Satf": "शतृँ", "SAnac": "शानच्", "yat": "यत्", "ac": "अच्",
           "ap": "अप्", "ktin": "क्तिन्", "GaY": "घञ्", "Ryat": "ण्यत्", "kyap": "क्यप्", "lyap": "ल्यप्"}
TADDHITA_LISTS = {   # pratyaya → stems (sanskritabhyas lists the pratyayas; the stems are ours)
    "aR": ["upagu", "aSvapati", "vasudeva", "Siva", "aSva", "mfga", "manu", "kuru"], "aY": ["vida", "urva", "bAhu"],
    "WaY": ["akza", "Salya", "pada"], "Wak": ["akza", "Salya", "dfti", "nO"], "Qak": ["vinatA", "suparRa", "agni"],
    "tva": ["manuzya", "mUQa", "deva", "guru", "laGu"], "tal": ["manuzya", "mUQa", "deva", "guru", "jana", "bandhu"],
    "mayaw": ["mfd", "suvarRa", "kAzWa", "AnaNda", "anna"], "matup": ["Dana", "buddhi", "bala", "SrI", "gO", "BAnu"],
    "ini": ["daRqa", "Dana", "bala", "Kaqga"], "tasil": ["sarva", "kim", "yad", "tad", "idam"], "tral": ["sarva", "kim", "yad", "tad"],
    "iY": ["daSaraTa", "dakza", "vyAsa"],
}
TADDHITA_DEV = {"aR": "अण्", "aY": "अञ्", "WaY": "ठञ्", "Wak": "ठक्", "Qak": "ढक्", "tva": "त्व", "tal": "तल्",
                "mayaw": "मयट्", "matup": "मतुप्", "ini": "इनि", "tasil": "तसिल्", "tral": "त्रल्", "iY": "इञ्"}
KRT_VIVAKSHA_ENGINE = {  # kṛt → the meanings that lead the engine to it (AMENDMENT 25; as tools/exercise_audit._KRT_VIV)
    "kta": [{"kala": "BUta", "artha": "karman"}, {"kala": "BUta", "artha": "kartf"}, {"kala": "BUta", "artha": "BAva"}],
    "ktavatu": [{"kala": "BUta", "artha": "kartf"}], "ktvA": [{"kala": "pUrvakAla", "samAnakartfka": "samAnakartfka"}],
    "tumun": [{"kala": "Bavizyat", "kriyArTA": "kriyArTA"}],
    "Satf": [{"kala": "vartamAna", "samAnADikaraRa": "apraTamA"}], "SAnac": [{"kala": "vartamAna", "samAnADikaraRa": "apraTamA"}],
    "tavya": [{"krt": "kftya"}], "anIyar": [{"krt": "kftya"}], "yat": [{"krt": "kftya"}], "Ryat": [{"krt": "kftya"}],
    "kyap": [{"krt": "kftya"}], "tfc": [{"krt": "Rvultfc"}], "Rvul": [{"krt": "Rvultfc"}],
    "lyuw": [{"artha": "BAva"}], "GaY": [{"artha": "BAva"}], "ktin": [{"artha": "BAva"}], "ap": [{"artha": "BAva"}],
    "ac": [{"artha": "kartf"}],
}
NAMADHATU = [("putra", "kyac"), ("kfzRa", "kyaN"), ("putra", "kAmyac"), ("yaSas", "kAmyac"), ("mAtf", "kyac"),
             ("haMsa", "kyaN"), ("Dana", "kAmyac"), ("ojas", "kyaN"), ("Syena", "kyac"), ("samiD", "kyac"),
             ("udaka", "kyac"), ("SyAma", "kyaN")]
NAMA_DEV = {"kyac": "क्यच्", "kyaN": "क्यङ्", "kAmyac": "काम्यच्"}

POPULAR_NOUNS = [  # (stem, liṅga) — the 'easy' pool: popular stems of every ending, as sanskritabhyas's front page
    ("rAma", "pulliṅga"), ("bAlaka", "pulliṅga"), ("deva", "pulliṅga"), ("vfkza", "pulliṅga"), ("Pala", "napuṃsaka"),
    ("vana", "napuṃsaka"), ("jYAna", "napuṃsaka"), ("pustaka", "napuṃsaka"), ("latA", "strīliṅga"), ("bAlikA", "strīliṅga"),
    ("vidyA", "strīliṅga"), ("hari", "pulliṅga"), ("kavi", "pulliṅga"), ("muni", "pulliṅga"), ("mati", "strīliṅga"),
    ("nadI", "strīliṅga"), ("guru", "pulliṅga"), ("BAnu", "pulliṅga"), ("Denu", "strīliṅga"), ("vaDU", "strīliṅga"),
    ("vAri", "napuṃsaka"), ("maDu", "napuṃsaka"), ("pitf", "pulliṅga"), ("mAtf", "strīliṅga"), ("dAtf", "pulliṅga"),
    ("rAjan", "pulliṅga"), ("Atman", "pulliṅga"), ("nAman", "napuṃsaka"), ("Bagavat", "pulliṅga"), ("manas", "napuṃsaka"),
    ("vAc", "strīliṅga"), ("marut", "pulliṅga"), ("jagat", "napuṃsaka"), ("sarit", "strīliṅga"), ("go", "pulliṅga"),
]
PRONOUNS = [("sarva", "pSN"), ("viSva", "pSN"), ("Bavat", "pS"), ("tad", "pSN"), ("yad", "pSN"), ("etad", "pSN"),
            ("kim", "pSN"), ("idam", "pSN"), ("adas", "pSN"), ("asmad", "p"), ("yuzmad", "p"), ("anya", "pSN"),
            ("itara", "pSN"), ("katara", "pSN"), ("katama", "pSN"), ("uBa", "pSN"), ("pUrva", "pSN"), ("para", "pSN")]
NUMBERS = [("eka", "pSN"), ("dvi", "pSN"), ("tri", "pSN"), ("catur", "pSN"), ("paYcan", "p"), ("zaz", "p"), ("saptan", "p"),
           ("azwan", "p"), ("navan", "p"), ("daSan", "p"), ("ekAdaSan", "p"), ("viMSati", "S"), ("triMSat", "S"),
           ("catvAriMSat", "S"), ("paYcASat", "S"), ("zazwi", "S"), ("saptati", "S"), ("aSIti", "S"), ("navati", "S"),
           ("Sata", "N"), ("sahasra", "N"), ("dvizazwi", "S")]
_LG = {"p": "pulliṅga", "S": "strīliṅga", "N": "napuṃsaka", "l": "strīliṅga"}
NUM_VACANA = {"eka": (1,), "dvi": (2,), "tri": (3,), "catur": (3,)}
GAPS: list[dict[str, Any]] = []


def dev(s: str) -> str:
    return " ".join(slp1_to_dev(w) for w in s.split()) if s else ""


@contextlib.contextmanager
def _quiet():
    with contextlib.redirect_stdout(io.StringIO()):
        yield


# ── Vidyut: in-process when this interpreter has it, else one persistent .venv worker ──────────────

_VLOCK = threading.Lock()
_VSTATE: dict[str, Any] = {}


def vidyut(req: dict) -> Any:
    """One request to tools/abhyasa_vidyut; None when Vidyut is unavailable."""
    with _VLOCK:
        if "inproc" not in _VSTATE:
            try:
                from tools.abhyasa_vidyut import Vidyut
                _VSTATE["inproc"] = Vidyut()
            except Exception:  # noqa: BLE001 — no vidyut in this interpreter: use the .venv worker
                _VSTATE["inproc"] = None
        if _VSTATE["inproc"] is not None:
            try:
                return _VSTATE["inproc"].handle(req)
            except Exception:  # noqa: BLE001
                return None
        p = _VSTATE.get("proc")
        if p is None or p.poll() is not None:
            if not VENV_PY.exists():
                return None
            p = subprocess.Popen([str(VENV_PY), "-m", "tools.abhyasa_vidyut", "--serve"], cwd=ROOT, text=True,
                                 stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, bufsize=1)
            _VSTATE["proc"] = p
        try:
            p.stdin.write(json.dumps(req, ensure_ascii=False) + "\n")
            p.stdin.flush()
            line = p.stdout.readline()
            out = json.loads(line) if line else {}
        except (OSError, ValueError):
            _VSTATE.pop("proc", None)
            return None
        return out.get("ok")


# ── word pools ───────────────────────────────────────────────────────────────────────────────────

@cache
def corpus() -> dict[tuple[str, str], list[list[str]]]:
    """ashtadhyayi.com printed paradigms (shabda__data2.txt): (stem SLP1, liṅga) → 24 cells of SLP1 forms.
    Display/cross-check data (Art. 6: never an engine input). Empty when the local copy is absent."""
    path = ROOT / "data" / "reference" / "ashtadhyayi_com" / "shabda__data2.txt"
    try:
        rows = json.loads(path.read_text(encoding="utf-8"))["data"]
    except FileNotFoundError:
        return {}
    lg = {"P": "pulliṅga", "S": "strīliṅga", "N": "napuṃsaka"}
    out: dict[tuple[str, str], list[list[str]]] = {}
    for r in rows:
        if r.get("linga") not in lg:
            continue
        try:
            cells = [[dev_to_slp1(x.replace("हे ", "").strip()) for x in c.split("-") if x.strip()]
                     for c in r["forms"].split(";")]
        except Exception:  # noqa: BLE001 — a cell the transliterator cannot read is skipped
            continue
        if len(cells) == 24:
            out.setdefault((dev_to_slp1(r["word"]), lg[r["linga"]]), cells)
    return out


@cache
def noun_pool() -> list[dict[str, Any]]:
    """Every nominal stem of the shabda index (9,007), with its ending class."""
    path = ROOT / "webui" / "static" / "shabda_index.json"
    try:
        idx = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        idx = []
    out = [{"stem": r["slp"], "linga": r["l"], "dev": r["w"], "artha": r.get("a", ""), "en": r.get("ae", "")}
           for r in idx if r.get("l") in LINGA]
    return out


def _ending(stem: str) -> str:
    return "ajanta" if stem[-1] in "aAiIuUfFxXeEoO" else "halanta"


@cache
def dhatu_pool() -> list[dict[str, Any]]:
    from pipelines.dhatupatha import _envelope, _payload
    out = []
    for e in _envelope(_payload())["entries"]:
        if not e.get("dhatupatha_id"):
            continue
        out.append({"ref": e["dhatupatha_id"], "id": e.get("id") or e["upadesha_slp1"], "upadesha": e["upadesha_slp1"],
                    "dev": e.get("mula_dhatu_dev") or dev(e["upadesha_slp1"]), "gana": int(e["dhatupatha_id"].split(".")[0]),
                    "artha": e.get("artha_dev", ""), "pada": e.get("pada_label_dev", "")})
    return out


POPULAR_ROOTS = ["01.0001", "01.0381", "01.1137", "01.1143", "01.1074", "01.0051", "01.1164", "01.0979", "01.0822",
                 "01.0405", "01.0643", "01.1160", "01.0640", "01.0746", "01.1141", "01.0919", "06.0092", "04.0010",
                 "03.0010", "01.1092", "08.0010", "01.0002", "02.0001", "02.0060", "02.0002", "09.0001", "10.0001",
                 "01.0685", "01.0975", "01.1039", "06.0001", "07.0001"]


@cache
def popular_roots() -> list[dict[str, Any]]:
    by = {d["ref"]: d for d in dhatu_pool()}
    out = [by[r] for r in POPULAR_ROOTS if r in by]
    out += [by[x["ref"]] for x in bank_items("tinanta") if x["ref"] in by and by[x["ref"]] not in out]
    return out


# ── the bank (prebuilt by tools/build_abhyasa_bank.py) ──────────────────────────────────────────

@cache
def bank() -> dict[str, Any]:
    try:
        return json.loads(BANK.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {"items": {}, "meta": {}, "sutra_text": {}}


def bank_items(family: str) -> list[dict[str, Any]]:
    v = bank()["items"].get(family, [])
    return v if isinstance(v, list) else []


def sutra_text(sid: str) -> str:
    t = bank().get("sutra_text", {}).get(sid)
    if t:
        return t
    try:
        from engine import SUTRA_REGISTRY
        rec = SUTRA_REGISTRY.get(sid)
        return rec.text_dev if rec else ""
    except Exception:  # noqa: BLE001
        return ""


# ── paradigms: engine + Vidyut (+ printed corpus) per cell ────────────────────────────────────────

def _agree(engine: str | None, v: list[str] | None, c: list[str] | None, strict: bool) -> dict[str, Any] | None:
    """One cell's answer key. ``accepted`` lists every form the learner may write."""
    v, c = v or [], c or []
    srcs = []
    if engine:
        if engine in v:
            srcs.append("vidyut")
        if engine in c:
            srcs.append("corpus")
        if srcs:
            alts = [x for x in v if x in c or not c] if c else v
            return {"primary": engine, "accepted": list(dict.fromkeys([engine, *alts])), "sources": ["engine", *srcs]}
    if strict or not v:
        return None
    return {"primary": v[0], "accepted": v, "sources": ["vidyut"] + (["corpus"] if set(v) & set(c) else []),
            "engine": engine}


def _sub_state(stem: str, linga: str, vb: int, vc: int):
    """The engine's subanta derivation; asmad / yuṣmad go through their own glass-box paradigm (7.1.27–7.2.97),
    as core.analyze.rederive does."""
    if stem in ("asmad", "yuzmad") and vb <= 7:
        from pipelines import asmad_subanta as pr
        return (pr.derive_asmad if stem == "asmad" else pr.derive_yuzmad)(vb, vc)
    from pipelines.subanta import derive
    return derive(stem, vb, vc, linga=linga)


@lru_cache(maxsize=2048)
def _engine_sub(stem: str, linga: str, vb: int, vc: int) -> str | None:
    try:
        with _quiet():
            return _sub_state(stem, linga, vb, vc).flat_slp1()
    except Exception:  # noqa: BLE001 — the engine's own gap
        return None


@lru_cache(maxsize=512)
def noun_paradigm(stem: str, linga: str, strict: bool = True) -> dict[str, Any]:
    """24 cells (vibhakti-major, sambodhana last) of one nominal stem."""
    v = vidyut({"op": "subgrid", "stem": stem, "linga": linga}) or [[]] * 24
    c = corpus().get((stem, linga)) or [[]] * 24
    cells = []
    for i in range(24):
        vb, vc = i // 3 + 1, i % 3 + 1
        if not (v[i] or c[i]):
            continue
        eng = _engine_sub(stem, linga, vb, vc)
        k = _agree(eng, v[i], c[i], strict)
        if k is None:
            if eng and (v[i] or c[i]):
                GAPS.append({"family": "subanta", "request": [stem, linga, vb, vc], "engine": eng, "vidyut": v[i], "corpus": c[i]})
            continue
        cells.append({"key": f"{vb}-{vc}", "vibhakti": vb, "vacana": vc,
                      "label": f"{VIBHAKTI[vb]} {VACANA[vc]}", **k})
    return {"kind": "subanta", "stem": stem, "linga": linga, "lemma_dev": dev(stem), "linga_dev": LINGA[linga],
            "title": f"{dev(stem)} — {LINGA[linga]}", "cells": cells, "rows": VIBHAKTI[1:], "cols": VACANA[1:]}


@cache
def verified_tin() -> dict[tuple[str, str, str], dict[str, list[str]]]:
    """(dhātupāṭha id, lakāra, prayoga) → cells already derived by the engine and found among Vidyut's forms: the bank,
    then the local form index (data/index/forms.db + bench/oracle/practice_verified.json). Some gaṇas take the engine
    minutes per lakāra; these tables keep a question instant."""
    out: dict[tuple[str, str, str], dict[str, list[str]]] = {}
    for x in bank_items("tinanta"):
        out[(x["ref"], x["lakara"], x["prayoga"])] = x["cells"]
    try:
        from core.practice import _rows
        rows = _rows("tinanta", None, None)
    except Exception:  # noqa: BLE001 — the form index is local (gitignored)
        rows = []
    db_lak = {"vidhiliG": "liG", "ASIrliG": "AsIrliG"}
    banked = set(out)
    for r in rows:
        f = r["features"]
        key = (r["cell_key"].split("@")[1].split(":")[0], db_lak.get(f["lakara"], f["lakara"]), f.get("prayoga", "kartari"))
        if key in banked:
            continue
        cell = out.setdefault(key, {}).setdefault(f"{f['purusha']}-{f['vacana']}", [])
        if r["surface_slp1"] not in cell:
            cell.append(r["surface_slp1"])
    return out


@lru_cache(maxsize=512)
def verb_paradigm(ref: str, lakara: str, prayoga: str = "kartari", pada: str = "", sanadi: str = "",
                  prefix: str = "", strict: bool = True, budget: float = 10.0) -> dict[str, Any]:
    """Nine cells (prathama → uttama × eka → bahu) of one dhātu in one lakāra. Live engine derivation stops after
    ``budget`` seconds (some gaṇa-2 roots take ~5 s a cell); the cells left are skipped, or Vidyut's when not strict."""
    from pipelines.tinanta import derive as tin_derive
    d = next((x for x in dhatu_pool() if x["ref"] == ref), None)
    if d is None:
        raise LookupError(f"unknown dhātu {ref}")
    san = [s for s in sanadi.split("+") if s]
    pre = [p for p in prefix.split("+") if p]
    known = verified_tin().get((ref, lakara, prayoga)) if not (san or pre or pada) else None
    if known and len(known) >= 6:
        cells = [{"key": k, "purusha": int(k[0]), "vacana": int(k[2]), "label": f"{PURUSHA[int(k[0])]} {VACANA[int(k[2])]}",
                  "primary": v[0], "accepted": v, "sources": ["engine", "vidyut"]}
                 for k, v in sorted(known.items(), key=lambda kv: (-int(kv[0][0]), kv[0][2]))]
        return {"kind": "tinanta", "ref": ref, "lakara": lakara, "prayoga": prayoga, "pada": pada, "sanadi": sanadi,
                "prefix": prefix, "lemma_dev": d["dev"], "gana": d["gana"], "artha": d["artha"],
                "title": f"{d['dev']} — {GANA[d['gana']]} · {LAKARA[lakara]} · {PRAYOGA.get(prayoga, prayoga)}",
                "cells": cells, "rows": [PURUSHA[3], PURUSHA[2], PURUSHA[1]], "cols": VACANA[1:]}
    v = vidyut({"op": "tingrid", "upadesha": d["upadesha"], "path_id": ref, "lakara": lakara, "prayoga": prayoga,
                "pada": pada or None, "sanadi": san, "prefixes": pre})
    v = v if isinstance(v, list) else [[]] * 9
    engine_can = len(san) <= 1 and (not san or san[0] in ("Ric", "san"))
    kw: dict[str, Any] = {}
    if pada and prayoga == "kartari":
        kw["pada"] = pada
    if pre:
        kw["upasargas"] = pre
    if san:
        kw[{"Ric": "nic_recipe", "san": "san_recipe"}.get(san[0], "x")] = True
    cells = []
    deadline = time.monotonic() + budget
    for i, (pu, vc) in enumerate((p, c) for p in (3, 2, 1) for c in (1, 2, 3)):
        eng = None
        if engine_can and time.monotonic() < deadline:
            try:
                with _quiet():
                    eng = tin_derive(d["id"], lakara, prayoga, pu, vc, **kw).flat_slp1()
            except Exception:  # noqa: BLE001
                eng = None
        k = _agree(eng, v[i], None, strict)
        if k is None:
            if eng and v[i]:
                GAPS.append({"family": "tinanta", "request": [ref, lakara, prayoga, pada, sanadi, prefix, pu, vc],
                             "engine": eng, "vidyut": v[i]})
            continue
        cells.append({"key": f"{pu}-{vc}", "purusha": pu, "vacana": vc, "label": f"{PURUSHA[pu]} {VACANA[vc]}", **k})
    head = "+".join(pre)
    title = f"{(dev(head) + ' + ') if head else ''}{d['dev']}{(' + ' + SANADI.get(sanadi, sanadi)) if sanadi else ''}"
    return {"kind": "tinanta", "ref": ref, "lakara": lakara, "prayoga": prayoga, "pada": pada, "sanadi": sanadi,
            "prefix": prefix, "lemma_dev": d["dev"], "gana": d["gana"], "artha": d["artha"],
            "title": f"{title} — {GANA[d['gana']]} · {LAKARA[lakara]} · {PRAYOGA.get(prayoga, prayoga)}",
            "cells": cells, "rows": [PURUSHA[3], PURUSHA[2], PURUSHA[1]], "cols": VACANA[1:]}


def namadhatu_paradigm(stem: str, pratyaya: str, lakara: str = "laT") -> dict[str, Any]:
    v = vidyut({"op": "namadhatu", "stem": stem, "pratyaya": pratyaya, "lakara": lakara})
    v = v if isinstance(v, list) else [[]] * 9
    cells = [{"key": f"{pu}-{vc}", "purusha": pu, "vacana": vc, "label": f"{PURUSHA[pu]} {VACANA[vc]}",
              "primary": v[i][0], "accepted": v[i], "sources": ["vidyut"]}
             for i, (pu, vc) in enumerate((p, c) for p in (3, 2, 1) for c in (1, 2, 3)) if v[i]]
    return {"kind": "namadhatu", "stem": stem, "pratyaya": pratyaya, "lakara": lakara,
            "title": f"{dev(stem)} + {NAMA_DEV[pratyaya]} — {LAKARA[lakara]}", "cells": cells,
            "rows": [PURUSHA[3], PURUSHA[2], PURUSHA[1]], "cols": VACANA[1:],
            "note": "नामधातुः यन्त्रे अद्यापि न — Vidyut's forms (the engine does not derive nāmadhātus yet)."}


# ── picking a word for a family under the filters ────────────────────────────────────────────────

def _noun_candidates(family: str, level: int, f: dict[str, Any]) -> list[tuple[str, str]]:
    lg = f.get("linga") or ""
    if family == "pronoun":
        cand = [(s, _LG[c]) for s, cs in PRONOUNS for c in dict.fromkeys(cs) if c in _LG]
        cand = [x for x in cand if level >= 3 or x[0] in ("sarva", "tad", "asmad", "yuzmad", "Bavat", "kim", "yad", "etad")]
    elif family == "number":
        cand = [(s, _LG[c]) for s, cs in NUMBERS for c in cs]
        cand = [x for x in cand if level >= 3 or x[0] in ("eka", "dvi", "tri", "catur", "paYcan", "zaz", "daSan", "Sata")]
    elif level <= 2 and not f.get("anta_letter") and not f.get("stem"):
        cand = list(POPULAR_NOUNS) if level == 2 else [x for x in POPULAR_NOUNS if x[0][-1] in "aAiI"]
    else:
        cand = [(r["stem"], r["linga"]) for r in noun_pool()]
    if f.get("stem"):
        cand = [x for x in cand if x[0] == f["stem"]] or [(f["stem"], lg or "pulliṅga")]
    if lg:
        cand = [x for x in cand if x[1] == lg]
    if f.get("anta") in ("ajanta", "halanta"):
        cand = [x for x in cand if _ending(x[0]) == f["anta"]]
    if f.get("anta_letter"):
        cand = [x for x in cand if x[0].endswith(f["anta_letter"])]
    return cand


def _verb_choice(rng: random.Random, level: int, f: dict[str, Any]) -> dict[str, Any]:
    pool = popular_roots() if (level <= 2 or f.get("popular")) else dhatu_pool()
    if f.get("dhatu"):
        pool = [d for d in dhatu_pool() if d["ref"] == f["dhatu"] or d["upadesha"] == f["dhatu"]] or pool
    if f.get("gana"):
        pool = [d for d in pool if d["gana"] == int(f["gana"])] or [d for d in dhatu_pool() if d["gana"] == int(f["gana"])]
    d = rng.choice(pool)
    lakaras = f.get("lakara") or (["laT", "loT", "laG", "lRT"] if level == 1 else
                                  ["laT", "loT", "laG", "lRT", "liG", "luT"] if level == 2 else list(LAKARA))
    lakaras = lakaras if isinstance(lakaras, list) else [lakaras]
    prayoga = f.get("prayoga") or ("karmani" if level == 4 and rng.random() < .3 else "kartari")
    upas = f.get("upasarga") or ""
    if upas == "any":
        upas = rng.choice(UPASARGA)
    san = f.get("sanadi") or ""
    if san == "any":
        san = rng.choice(list(SANADI))
    return {"ref": d["ref"], "lakara": rng.choice(lakaras), "prayoga": prayoga, "pada": f.get("pada") or "",
            "sanadi": san, "prefix": upas}


def paradigm_for(family: str, rng: random.Random, level: int, f: dict[str, Any]) -> dict[str, Any]:
    strict = not f.get("vidyut_fallback")
    for _ in range(12):
        if family in ("noun", "pronoun", "number"):
            cand = _noun_candidates(family, level, f)
            if not cand:
                raise LookupError("इन विकल्पों से कोई शब्द नहीं मिला — no word matches these filters")
            stem, lg = rng.choice(cand)
            p = noun_paradigm(stem, lg, strict)
            if family == "number" and stem in NUM_VACANA:
                p = {**p, "cells": [c for c in p["cells"] if c["vacana"] in NUM_VACANA[stem]]}
        elif family == "verb":
            spec = _verb_choice(rng, level, f)
            needs_vidyut = bool(spec["sanadi"]) and spec["sanadi"] not in ("Ric", "san")
            p = verb_paradigm(**spec, strict=strict and not needs_vidyut)
            if len(p["cells"]) < 3 and strict and (spec["sanadi"] or spec["prefix"] or spec["prayoga"] != "kartari"):
                p = verb_paradigm(**spec, strict=False)      # the engine is not ready here: Vidyut's forms, badged
        elif family == "namadhatu":
            stem, pr = rng.choice(NAMADHATU)
            p = namadhatu_paradigm(stem, pr, f.get("lakara") if isinstance(f.get("lakara"), str) else "laT")
        else:
            raise ValueError(family)
        if f.get("vibhakti") and family in ("noun", "pronoun"):
            p = {**p, "focus": [c for c in p["cells"] if c["vibhakti"] == int(f["vibhakti"])]}
        if len(p["cells"]) >= 3:
            return p
    raise LookupError("यन्त्रेण पर्याप्तानि रूपाणि न सिद्धानि — the engine has too few agreed forms here; "
                      "relax the filters or allow Vidyut's forms")


# ── questions ────────────────────────────────────────────────────────────────────────────────────

def _cells_by_form(cells: list[dict]) -> dict[str, list[str]]:
    by: dict[str, list[str]] = {}
    for c in cells:
        for a in c["accepted"]:
            by.setdefault(a, []).append(c["label"])
    return by


def _opt(slp: str, by: dict[str, list[str]] | None = None) -> dict[str, Any]:
    return {"slp1": slp, "dev": dev(slp), "labels": (by or {}).get(slp, [])}


def _near(cells: list[dict], t: dict, level: int) -> list[dict]:
    if level < 3:
        return cells
    keys = ("vibhakti", "vacana", "purusha")
    near = [c for c in cells if c is not t and any(c.get(k) is not None and c.get(k) == t.get(k) for k in keys)]
    return near if len(near) >= 3 else cells


def paradigm_question(p: dict[str, Any], drill: str, rng: random.Random, level: int) -> dict[str, Any]:
    cells = p["cells"]
    pool = p.get("focus") or cells
    by = _cells_by_form(cells)
    head = {"title": p["title"], "paradigm": p, "note": p.get("note", "")}
    if drill in ("mcq", "recall"):
        t = rng.choice(pool)
        wrong = list(dict.fromkeys(c["primary"] for c in _near(cells, t, level) if c["primary"] not in t["accepted"]))
        rng.shuffle(wrong)
        opts = [_opt(x, by) for x in [*wrong[:3], t["primary"]]]
        rng.shuffle(opts)
        return {**head, "prompt": t["label"], "cell": t, "accepted": t["accepted"],
                "accepted_dev": [dev(a) for a in t["accepted"]], "sources": t["sources"],
                "options": opts if drill == "mcq" else []}
    if drill == "tf":
        stmts = []
        for t in rng.sample(pool, min(5, len(pool))):
            truth = rng.random() < .5
            shown = t
            if not truth:
                others = [c for c in cells if not set(c["accepted"]) & set(t["accepted"])]
                shown = rng.choice(others) if others else t
                truth = shown is t
            stmts.append({"form": _opt(shown["primary"]), "label": t["label"], "answer": truth,
                          "correct_dev": dev(t["primary"]), "sources": t["sources"]})
        return {**head, "statements": stmts}
    if drill == "match":
        uniq, seen = [], set()
        for c in rng.sample(cells, len(cells)):
            if c["primary"] not in seen and len(by.get(c["primary"], [])) == 1:
                seen.add(c["primary"])
                uniq.append(c)
        pairs = uniq[:5]
        right = [c["label"] for c in pairs]
        rng.shuffle(right)
        return {**head, "pairs": [{"form": _opt(c["primary"]), "label": c["label"]} for c in pairs], "labels": right}
    if drill == "odd":
        attrs = ["vacana", "vibhakti"] if p["kind"] == "subanta" else ["vacana", "purusha"]
        for _ in range(30):
            attr = rng.choice(attrs)
            val = rng.choice(sorted({c[attr] for c in cells}))
            same = [c for c in cells if c[attr] == val]
            other = [c for c in cells if c[attr] != val]
            # a form that also fills a cell with ``val`` (रामाभ्याम्) cannot be the odd one
            same = [c for c in same if len({x[attr] for x in cells if c["primary"] in x["accepted"]}) == 1]
            other = [c for c in other if val not in {x[attr] for x in cells if c["primary"] in x["accepted"]}]
            if len(same) >= 3 and other:
                three = rng.sample(same, 3)
                odd = rng.choice(other)
                opts = [*three, odd]
                rng.shuffle(opts)
                what = {"vacana": VACANA, "vibhakti": VIBHAKTI, "purusha": PURUSHA}[attr][val]
                return {**head, "options": [{**_opt(c["primary"]), "label": c["label"]} for c in opts],
                        "answer": odd["primary"], "reason": f"शेषाणि {what} — the other three are {what}"}
        return {**paradigm_question(p, "mcq", rng, level), "drill": "mcq"}
    if drill == "table":
        return {**head, "cells": [{"key": c["key"], "label": c["label"], "accepted": c["accepted"],
                                   "accepted_dev": [dev(a) for a in c["accepted"]], "sources": c["sources"]} for c in cells]}
    if drill == "sutra":
        return sutra_question(p, rng)
    raise ValueError(f"drill {drill!r} not for paradigms")


def _trace_for(p: dict[str, Any], cell: dict[str, Any]) -> list[dict]:
    from core.trace_view import enrich_trace
    if p["kind"] == "subanta":
        with _quiet():
            st = _sub_state(p["stem"], p["linga"], cell["vibhakti"], cell["vacana"])
    else:
        from pipelines.tinanta import derive as tin_derive
        d = next(x for x in dhatu_pool() if x["ref"] == p["ref"])
        kw: dict[str, Any] = {"pada": p["pada"]} if p.get("pada") and p["prayoga"] == "kartari" else {}
        if p.get("prefix"):
            kw["upasargas"] = p["prefix"].split("+")
        if p.get("sanadi") in ("Ric", "san"):
            kw[{"Ric": "nic_recipe", "san": "san_recipe"}[p["sanadi"]]] = True
        with _quiet():
            st = tin_derive(d["id"], p["lakara"], p["prayoga"], cell["purusha"], cell["vacana"], **kw)
    return enrich_trace(list(st.trace))


def sutra_question(p: dict[str, Any], rng: random.Random) -> dict[str, Any]:
    """Which sūtra made this change? Only from cells where the engine's form is the agreed answer."""
    from core.trace_view import filter_surface_changed
    cells = [c for c in p["cells"] if "engine" in c["sources"]]
    rng.shuffle(cells)
    for cell in cells[:6]:
        steps = [s for s in filter_surface_changed(_trace_for(p, cell))
                 if s.get("sutra_id") and not s["sutra_id"].startswith("__") and s.get("_sutra_text_dev")]
        if len(steps) < 2:
            continue
        step = rng.choice(steps)
        sid = step["sutra_id"]
        pool = {s["sutra_id"]: s["_sutra_text_dev"] for s in steps if s["sutra_id"] != sid}
        if len(pool) < 3:
            from engine import SUTRA_REGISTRY
            pada = sid.rsplit(".", 1)[0] + "."
            near = [r for r in SUTRA_REGISTRY.values() if r.sutra_id.startswith(pada) and r.text_dev and r.sutra_id != sid]
            for r in rng.sample(near, min(8, len(near))):
                pool.setdefault(r.sutra_id, r.text_dev)
        opts = [{"sutra_id": k, "text_dev": v} for k, v in list(pool.items())[:3]] + [{"sutra_id": sid, "text_dev": step["_sutra_text_dev"]}]
        rng.shuffle(opts)
        return {"title": p["title"], "paradigm": p, "prompt": cell["label"], "cell": cell,
                "before_dev": step.get("form_before_dev", ""), "after_dev": step.get("form_after_dev", ""),
                "options": opts, "answer_sutra": sid, "sources": cell["sources"]}
    raise LookupError("no surface-changing sūtra step in the engine's derivation of this word")


def _krt_rows(rng: random.Random, level: int, f: dict[str, Any]) -> tuple[dict, list[dict]]:
    """Kṛts of one dhātu: the bank's engine+Vidyut-agreed items (popular roots), else Vidyut's forms (badged)."""
    by_root: dict[str, list[dict]] = {}
    for x in bank_items("krdanta"):
        if level >= x.get("level", 2) or level >= 3:
            by_root.setdefault(x["ref"], []).append(x)
    if f.get("gana"):
        by_root = {k: v for k, v in by_root.items() if int(k.split(".")[0]) == int(f["gana"])}
    use_bank = by_root and f.get("popular", True) and not f.get("upasarga") and not f.get("sanadi")
    if use_bank:
        ref = rng.choice(sorted(by_root))
        rows = [{"krt": x["krt"], "label": KRT_DEV.get(x["krt"], x["krt_dev"]), "primary": x["forms"][0],
                 "accepted": x["forms"], "sources": ["engine", "vidyut"], "steps": x.get("steps", [])} for x in by_root[ref]]
        d = next(x for x in dhatu_pool() if x["ref"] == ref)
        return {"ref": ref, "dev": d["dev"], "gana": d["gana"], "artha": d["artha"]}, rows
    d = rng.choice([x for x in (popular_roots() if f.get("popular", True) else dhatu_pool())
                    if not f.get("gana") or x["gana"] == int(f["gana"])])
    pre = [] if not f.get("upasarga") else [rng.choice(UPASARGA) if f["upasarga"] == "any" else f["upasarga"]]
    san = [] if not f.get("sanadi") else (rng.choice(list(SANADI)) if f["sanadi"] == "any" else f["sanadi"]).split("+")
    krts = KRTS + (["lyap"] if pre else [])
    v = vidyut({"op": "krt", "upadesha": d["upadesha"], "path_id": d["ref"], "krts": krts, "sanadi": san, "prefixes": pre}) or {}
    rows = []
    for k in krts:
        forms = (v.get(k) or {}).get("pum") or (v.get(k) or {}).get("napum") or []
        if forms:
            rows.append({"krt": k, "label": KRT_DEV.get(k, k), "primary": forms[0], "accepted": forms, "sources": ["vidyut"],
                         "stri": (v.get(k) or {}).get("stri") or []})
    head = (dev("+".join(pre)) + " + " if pre else "") + d["dev"] + (" + " + SANADI.get("+".join(san), "+".join(san)) if san else "")
    return {"ref": d["ref"], "dev": head, "gana": d["gana"], "artha": d["artha"],
            "note": "विद्युत्-रूपाणि — the engine's kṛdanta check for this root is pending (see the bank for engine-agreed roots)"}, rows


def krdanta_question(drill: str, rng: random.Random, level: int, f: dict[str, Any]) -> dict[str, Any]:
    root, rows = _krt_rows(rng, level, f)
    if len(rows) < 2:
        raise LookupError("no kṛdanta forms for this root")
    title = f"{root['dev']} — {GANA[root['gana']]} · {root['artha']}"
    p = {"kind": "krdanta", "title": title, "cells": [{**r, "key": r["krt"]} for r in rows], "rows": [], "cols": []}
    head = {"title": title, "paradigm": p, "note": root.get("note", "")}
    if drill == "match":
        pairs = rng.sample(rows, min(5, len(rows)))
        labels = [r["label"] for r in pairs]
        rng.shuffle(labels)
        return {**head, "pairs": [{"form": _opt(r["primary"]), "label": r["label"]} for r in pairs], "labels": labels}
    if drill == "tf":
        stmts = []
        for r in rng.sample(rows, min(5, len(rows))):
            truth = rng.random() < .5
            shown = r if truth else rng.choice([x for x in rows if x is not r])
            stmts.append({"form": _opt(shown["primary"]), "label": f"{root['dev']} + {r['label']}",
                          "answer": shown is r or shown["primary"] in r["accepted"], "correct_dev": dev(r["primary"]),
                          "sources": r["sources"]})
        return {**head, "statements": stmts}
    t = rng.choice(rows)
    wrong = [r["primary"] for r in rows if r["primary"] not in t["accepted"]]
    rng.shuffle(wrong)
    opts = [_opt(x) for x in [*dict.fromkeys(wrong[:3]), t["primary"]]]
    rng.shuffle(opts)
    return {**head, "prompt": f"{root['dev']} + {t['label']}", "cell": t, "accepted": t["accepted"],
            "accepted_dev": [dev(a) for a in t["accepted"]], "sources": t["sources"], "steps": t.get("steps", []),
            "options": opts if drill == "mcq" else []}


def taddhita_question(drill: str, rng: random.Random, level: int, f: dict[str, Any]) -> dict[str, Any]:
    """stem + pratyaya = form. Engine-agreed items from the bank first; the sanskritabhyas pratyaya lists via Vidyut."""
    rows = [{"stem": x["stem"], "p": x["pratyaya"], "primary": x["forms"][0], "accepted": x["forms"],
             "sources": ["engine", "vidyut"], "steps": x.get("steps", [])} for x in bank_items("taddhita")]
    want = f.get("pratyaya")
    if want or level >= 2 or len(rows) < 4:
        names = [want] if want else list(TADDHITA_LISTS)
        for name in rng.sample(names, min(4, len(names))):
            for stem in rng.sample(TADDHITA_LISTS[name], min(3, len(TADDHITA_LISTS[name]))):
                v = vidyut({"op": "taddhita", "stem": stem, "names": [name]}) or {}
                if v.get(name) and not any(r["stem"] == stem and r["p"] == name for r in rows):
                    rows.append({"stem": stem, "p": name, "primary": v[name][0], "accepted": v[name], "sources": ["vidyut"]})
    if want:
        rows = [r for r in rows if r["p"] == want] or rows
    if len(rows) < 2:
        raise LookupError("no taddhita forms")
    for r in rows:
        r["label"] = f"{dev(r['stem'])} + {TADDHITA_DEV.get(r['p'], dev(r['p']))}"
    head = {"title": "तद्धितान्तम्", "paradigm": {"kind": "taddhita", "cells": rows}}
    if drill == "tf":
        stmts = []
        for r in rng.sample(rows, min(5, len(rows))):
            truth = rng.random() < .5
            shown = r if truth else rng.choice([x for x in rows if x is not r])
            stmts.append({"form": _opt(shown["primary"]), "label": r["label"], "answer": shown["primary"] in r["accepted"],
                          "correct_dev": dev(r["primary"]), "sources": r["sources"]})
        return {**head, "statements": stmts}
    t = rng.choice(rows)
    wrong = [r["primary"] for r in rows if r["primary"] not in t["accepted"]]
    rng.shuffle(wrong)
    opts = [_opt(x) for x in [*dict.fromkeys(wrong[:3]), t["primary"]]]
    rng.shuffle(opts)
    return {**head, "prompt": t["label"], "cell": t, "accepted": t["accepted"], "accepted_dev": [dev(a) for a in t["accepted"]],
            "sources": t["sources"], "steps": t.get("steps", []), "options": opts if drill == "mcq" else []}


def sandhi_question(drill: str, rng: random.Random, level: int, f: dict[str, Any]) -> dict[str, Any]:
    items = [x for x in bank_items("sandhi") if x["level"] <= max(level, 1) or level == 4]
    if f.get("rule"):
        items = [x for x in items if x["rule"] == f["rule"]] or items
    if not items:
        raise LookupError("sandhi bank is empty — run tools/build_abhyasa_bank.py --only sandhi")
    src_of = lambda x: ["engine", "vidyut"] if x.get("check") == "vidyut-sandhi" else ["engine"]  # noqa: E731
    if drill == "tf":
        stmts = []
        for x in rng.sample(items, min(5, len(items))):
            truth = rng.random() < .5 or not x["wrong"]
            shown = x["out"][0] if truth else rng.choice(x["wrong"])
            stmts.append({"form": {"slp1": shown, "dev": x["out_dev"][0] if truth else dev(shown)},
                          "label": f"{x['a_dev']} + {x['b_dev']}", "answer": truth, "correct_dev": x["out_dev"][0],
                          "sources": src_of(x)})
        return {"title": "सन्धिः", "statements": stmts}
    x = rng.choice(items)
    if drill == "sutra" and x.get("steps"):
        sid = x["steps"][-1][0]
        others = sorted({s for y in bank_items("sandhi") for s in [y["steps"][-1][0]] if y.get("steps") and s != sid})
        opts = [{"sutra_id": s, "text_dev": sutra_text(s)} for s in rng.sample(others, min(3, len(others)))]
        opts.append({"sutra_id": sid, "text_dev": sutra_text(sid)})
        rng.shuffle(opts)
        return {"title": "सन्धिः", "prompt": f"{x['a_dev']} + {x['b_dev']} → {x['out_dev'][0]}", "options": opts,
                "answer_sutra": sid, "steps": x["steps"], "sources": src_of(x)}
    opts = [{"slp1": x["out"][0], "dev": x["out_dev"][0]}] + [{"slp1": w, "dev": dev(w)} for w in x["wrong"][:3]]
    rng.shuffle(opts)
    return {"title": "सन्धिः", "prompt": f"{x['a_dev']} + {x['b_dev']} = ?", "accepted": x["out"], "accepted_dev": x["out_dev"],
            "options": opts if drill == "mcq" else [], "rule_dev": x["rule_dev"], "steps": x["steps"], "sources": src_of(x)}


# ── letters: svara-yukta vyañjana, saṃyukta vyañjana, lipis; pratyāhāra; it ───────────────────────

_VOWELS = ["a", "A", "i", "I", "u", "U", "f", "F", "x", "e", "E", "o", "O"]
_CONS = list("kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh")
LIPIS = {"Brahmi": "ब्राह्मी", "Grantha": "ग्रन्थ", "Tirhuta": "मिथिलाक्षर", "Sharada": "शारदा", "Siddham": "सिद्धम्"}


def varna_question(drill: str, rng: random.Random, level: int, f: dict[str, Any]) -> dict[str, Any]:
    mode = f.get("mode") or ("svara" if level == 1 else rng.choice(["svara", "samyukta"] + (["lipi"] if level >= 2 else [])))

    def item() -> tuple[str, str, str]:
        if mode == "samyukta":
            a, b = rng.choice(_CONS), rng.choice("yrvmnkt" if level < 3 else _CONS)
            return f"{slp1_to_dev(a)} + {slp1_to_dev(b + 'a')}", a + b + "a", "samyukta"
        c, v = rng.choice(_CONS), rng.choice(_VOWELS)
        return f"{slp1_to_dev(c)} + {slp1_to_dev(v)}", c + v, "svara"

    if mode == "lipi":
        lipi = f.get("lipi") or rng.choice(list(LIPIS))
        letters = rng.sample(_VOWELS[:9] + [c + "a" for c in _CONS], 5)
        tr = {x: (vidyut({"op": "lipi", "text": x, "to": [lipi]}) or {}).get(lipi, "") for x in letters}
        t = letters[0]
        opts = [{"slp1": x, "dev": slp1_to_dev(x), "glyph": tr[x]} for x in letters[:4]]
        rng.shuffle(opts)
        return {"title": f"लिपिः — {LIPIS[lipi]}", "prompt": tr[t], "prompt_is_glyph": True, "options": opts,
                "accepted": [t], "accepted_dev": [slp1_to_dev(t)], "sources": ["vidyut-lipi"]}
    if drill == "tf":
        stmts = []
        for _ in range(5):
            q, ans, _k = item()
            truth = rng.random() < .5
            shown = ans if truth else ans[:-1] + rng.choice([v for v in _VOWELS if v != ans[-1]])
            stmts.append({"form": {"slp1": shown, "dev": slp1_to_dev(shown)}, "label": q, "answer": shown == ans,
                          "correct_dev": slp1_to_dev(ans), "sources": ["engine"]})
        return {"title": "स्वरयुक्तव्यञ्जनम्" if mode == "svara" else "संयुक्तव्यञ्जनम्", "statements": stmts}
    if drill == "match":
        pairs, seen = [], set()
        while len(pairs) < 5:
            q, ans, _k = item()
            if ans not in seen:
                seen.add(ans)
                pairs.append({"form": {"slp1": ans, "dev": slp1_to_dev(ans)}, "label": q})
        labels = [p["label"] for p in pairs]
        rng.shuffle(labels)
        return {"title": "वर्णाः", "pairs": pairs, "labels": labels}
    q, ans, _k = item()
    wrong = list(dict.fromkeys(ans[:-1] + v for v in rng.sample(_VOWELS, 6) if ans[:-1] + v != ans))[:3]
    opts = [{"slp1": x, "dev": slp1_to_dev(x)} for x in [*wrong, ans]]
    rng.shuffle(opts)
    return {"title": "वर्णाः", "prompt": f"{q} = ?", "accepted": [ans], "accepted_dev": [slp1_to_dev(ans)],
            "options": opts if drill == "mcq" else [], "sources": ["engine"]}


def pratyahara_question(drill: str, rng: random.Random, level: int, f: dict[str, Any]) -> dict[str, Any]:
    items = [x for x in bank_items("varna") if x["level"] <= max(1, min(level, 2))] or bank_items("varna")
    if not items:
        raise LookupError("pratyāhāra bank empty")
    x = rng.choice(items)
    allv = _VOWELS + _CONS
    if drill == "tf":
        stmts = []
        for y in rng.sample(items, min(5, len(items))):
            letter = rng.choice(y["members"] if rng.random() < .5 else allv)
            stmts.append({"form": {"slp1": letter, "dev": slp1_to_dev(letter)}, "label": f"∈ {y['name_dev']}",
                          "answer": letter in y["members"], "correct_dev": " ".join(y["members_dev"]), "sources": ["engine"]})
        return {"title": "प्रत्याहाराः (1.1.71)", "statements": stmts}
    if drill == "mcq":
        inside = rng.choice(x["members"])
        outside = rng.sample([l for l in allv if l not in x["members"]], 3)
        opts = [{"slp1": l, "dev": slp1_to_dev(l)} for l in [inside, *outside]]
        rng.shuffle(opts)
        return {"title": "प्रत्याहाराः (1.1.71)", "prompt": f"{x['name_dev']} — कः वर्णः अन्तर्गतः?", "options": opts,
                "accepted": [inside], "accepted_dev": [slp1_to_dev(inside)], "sources": ["engine"],
                "explain": " ".join(x["members_dev"])}
    return {"title": "प्रत्याहाराः (1.1.71)", "prompt": f"{x['name_dev']} — सर्वे वर्णाः", "set_answer": x["members"],
            "accepted_dev": [" ".join(x["members_dev"])], "sources": ["engine"]}


def it_question(drill: str, rng: random.Random, level: int, f: dict[str, Any]) -> dict[str, Any]:
    items = [x for x in bank_items("it") if x["its"]]
    if not items:
        raise LookupError("it bank empty")
    x = rng.choice(items)
    right = " ".join(r["letters_dev"] for r in x["its"])
    if drill == "recall":
        return {"title": "इत्संज्ञा (1.3.2–1.3.9)", "prompt": f"{x['upadesha_dev']} — इतः के? (letters, space-separated)",
                "accepted_dev": [right], "its": x["its"], "residue_dev": x["residue_dev"], "sources": ["engine"]}
    others = list(dict.fromkeys(" ".join(r["letters_dev"] for r in y["its"]) for y in items if y["its"] and y is not x))
    opts = [o for o in rng.sample(others, min(8, len(others))) if o != right][:3] + [right]
    rng.shuffle(opts)
    return {"title": "इत्संज्ञा (1.3.2–1.3.9)", "prompt": f"{x['upadesha_dev']} — इतः के?",
            "options": [{"dev": o, "slp1": o} for o in opts], "accepted_dev": [right], "its": x["its"],
            "residue_dev": x["residue_dev"], "sources": ["engine"]}


# ── vākya ────────────────────────────────────────────────────────────────────────────────────────

def vakya() -> dict[str, Any]:
    return bank()["items"].get("vakya") or {"lessons": []}


def vakya_question(drill: str, rng: random.Random, level: int, f: dict[str, Any]) -> dict[str, Any]:
    V = vakya()
    lessons = [L for L in V["lessons"] if L["sentences"] and (f.get("lesson") == L["id"] or
                                                              (not f.get("lesson") and L["level"] <= max(level, 1)))]
    if not lessons:
        raise LookupError("no sentence lessons in the bank — run tools/build_abhyasa_bank.py --only vakya")
    L = rng.choice(lessons) if not f.get("lesson") else lessons[0]
    s = L["sentences"][f["index"] % len(L["sentences"])] if isinstance(f.get("index"), int) else rng.choice(L["sentences"])
    lesson = {k: L[k] for k in ("id", "title", "deva", "about", "sutras")}
    lesson["sutra_text"] = {sid: sutra_text(sid) for sid in L["sutras"]}
    if drill == "karaka":
        nouns = [w for w in s["words"] if w["kind"] != "verb"]
        w = rng.choice(nouns)
        roles = list(V["karaka"])
        opts = [{"role": r, "dev": V["karaka"][r]["dev"], "vibhakti": VIBHAKTI[V["karaka"][r]["vibhakti"]]} for r in roles]
        k = V["karaka"][w["role"]]
        return {"title": f"{L['deva']} — {L['title']}", "lesson": lesson, "sentence_dev": " ".join(dev(x["form"]) for x in s["words"]) + "।",
                "en": s["en"], "word_dev": dev(w["form"]), "options": opts, "answer_role": w["role"],
                "why": [{"sutra": k["role_sutra"], "text": sutra_text(k["role_sutra"])},
                        {"sutra": k["case_sutra"], "text": sutra_text(k["case_sutra"])}],
                "sources": ["engine", "vidyut"]}
    return {"title": f"{L['deva']} — {L['title']}", "lesson": lesson, "id": s["id"], "en": s["en"],
            "words": [{"role": w["role"], "kind": w["kind"]} for w in s["words"]], "sources": ["engine", "vidyut"]}


def grade_compose(sentence_id: str, answer_slp1: list[str]) -> dict[str, Any]:
    """Word order free, no sandhi. Each gold word matched against the learner's words; a wrong word is placed in its
    paradigm and explained by the kāraka sūtra + vibhakti sūtra (or puruṣa/vacana for the verb)."""
    V = vakya()
    s = next((x for L in V["lessons"] for x in L["sentences"] if x["id"] == sentence_id), None)
    if s is None:
        raise LookupError(sentence_id)
    left = [a.strip() for a in answer_slp1 if a.strip()]
    notes, ok = [], True
    tables = V["tables"]

    def where(form: str) -> tuple[str, str] | None:
        for lemma, t in tables["nouns"].items():
            for key, forms in t["cells"].items():
                if form in forms:
                    vb, vc = map(int, key.split("-"))
                    return lemma, f"{VIBHAKTI[vb]} {VACANA[vc]}"
        for lemma, laks in tables["verbs"].items():
            for lak, cells in laks.items():
                for key, forms in cells.items():
                    if form in forms:
                        pu, vc = map(int, key.split("-"))
                        return lemma, f"{LAKARA[lak]} {PURUSHA[pu]} {VACANA[vc]}"
        return None

    for w in s["words"]:
        hit = next((a for a in left if a in w["alts"]), None)
        if hit:
            left.remove(hit)
            notes.append({"status": "ok", "got_dev": dev(hit), "role": w["role"]})
            continue
        ok = False
        same = next((a for a in left if (where(a) or ("",))[0] == w["lemma"]), None)
        if w["kind"] == "verb":
            need = f"{LAKARA[w['lakara']]} {PURUSHA[w['purusha']]} {VACANA[w['vacana']]}"
            why = [V["purusha_sutras"][str(w["purusha"])]]
        else:
            k = V["karaka"][w["role"]]
            need = f"{VIBHAKTI[w['vibhakti']]} {VACANA[w['vacana']]}"
            why = [k["role_sutra"], k["case_sutra"]] + ([V["anabhihite"]] if w["role"] != "karta" else [])
        if same:
            left.remove(same)
            notes.append({"status": "wrong", "got_dev": dev(same), "got_is": where(same)[1], "need": need,
                          "role": w["role"], "sutras": [{"id": x, "text": sutra_text(x)} for x in why]})
        else:
            notes.append({"status": "missing", "role": w["role"], "need": need,
                          "sutras": [{"id": x, "text": sutra_text(x)} for x in why]})
    for a in left:
        ok = False
        notes.append({"status": "extra", "got_dev": dev(a), "got_is": (where(a) or ("", "?"))[1]})
    return {"ok": ok, "notes": notes, "answer_dev": " ".join(dev(w["form"]) for w in s["words"]) + "।",
            "words": [{"form_dev": dev(w["form"]), "alts_dev": [dev(a) for a in w["alts"]], "role": w["role"],
                       "role_dev": V["karaka"].get(w["role"], {}).get("dev", "क्रिया"),
                       "what": (f"{LAKARA[w['lakara']]} · {PURUSHA[w['purusha']]} · {VACANA[w['vacana']]}" if w["kind"] == "verb"
                                else f"{VIBHAKTI[w['vibhakti']]} · {VACANA[w['vacana']]} · {LINGA.get(w['linga'], '')}"),
                       "sutras": ([{"id": V["karaka"][w["role"]]["role_sutra"], "text": sutra_text(V["karaka"][w["role"]]["role_sutra"])},
                                   {"id": V["karaka"][w["role"]]["case_sutra"], "text": sutra_text(V["karaka"][w["role"]]["case_sutra"])}]
                                  if w["kind"] != "verb" else
                                  [{"id": V["purusha_sutras"][str(w["purusha"])], "text": sutra_text(V["purusha_sutras"][str(w["purusha"])])}])}
                      for w in s["words"]]}


# ── entry points ─────────────────────────────────────────────────────────────────────────────────

def catalog() -> dict[str, Any]:
    meta = bank().get("meta", {})
    return {"levels": LEVELS, "drills": DRILLS, "families": FAMILIES, "family_order": list(FAMILIES), "lakara": LAKARA, "prayoga": PRAYOGA,
            "gana": GANA, "upasarga": [{"slp1": u, "dev": dev(u)} for u in UPASARGA], "sanadi": SANADI,
            "linga": LINGA, "vibhakti": VIBHAKTI, "krt": KRT_DEV, "taddhita": TADDHITA_DEV, "lipi": LIPIS,
            "sandhi_rules": sorted({(x["rule"], x["rule_dev"]) for x in bank_items("sandhi")}),
            "vakya_lessons": [{k: L[k] for k in ("id", "level", "title", "deva")} | {"n": len(L["sentences"])}
                              for L in vakya()["lessons"]],
            "bank": {"generated_at": meta.get("generated_at"), "engine_commit": meta.get("engine_commit"),
                     "counts": meta.get("counts", {})},
            "vidyut": vidyut({"op": "ping"}) == "pong"}


def question(family: str, drill: str, level: int = 1, filters: dict[str, Any] | None = None,
             seed: int | None = None) -> dict[str, Any]:
    f = dict(filters or {})
    rng = random.Random(seed)
    if family not in FAMILIES:
        raise ValueError(f"unknown family {family!r}")
    if drill not in FAMILIES[family]["drills"]:
        drill = FAMILIES[family]["drills"][0]
    if family in ("noun", "pronoun", "number", "verb", "namadhatu"):
        q = paradigm_question(paradigm_for(family, rng, level, f), drill, rng, level)
    else:
        q = {"krdanta": krdanta_question, "taddhita": taddhita_question, "sandhi": sandhi_question,
             "varna": varna_question, "pratyahara": pratyahara_question, "it": it_question,
             "vakya": vakya_question}[family](drill, rng, level, f)
    return {"family": family, "drill": drill, "level": level, "seed": seed, **q}


@cache
def _form_index() -> dict[str, list[tuple[str, str, int]]]:
    """Printed form → (stem, liṅga, cell index) over the ashtadhyayi.com paradigms (display lookup only)."""
    idx: dict[str, list[tuple[str, str, int]]] = {}
    for (stem, lg), cells in corpus().items():
        for i, forms in enumerate(cells):
            for f in forms:
                idx.setdefault(f, []).append((stem, lg, i))
    return idx


def guess_linga(stem: str) -> str:
    """The stem's liṅga: the printed paradigm's, else what a kośa entry says (स्त्री / पुं / नपुं), else its ending."""
    for lg in LINGA:
        if (stem, lg) in corpus():
            return lg
    try:
        from core.vyutpatti import kosha_entries
        for e in kosha_entries(dev(stem), ("apte-hi", "vcp", "skd"), 3):
            head = e["body"][:40]
            for mark, lg in (("नपुं", "napuṃsaka"), ("क्ली", "napuṃsaka"), ("स्त्री", "strīliṅga"), ("पुं", "pulliṅga")):
                if mark in head:
                    return lg
    except Exception:  # noqa: BLE001 — no lexicon: fall through to the ending
        pass
    return "strīliṅga" if stem[-1:] in ("A", "I", "U") else "pulliṅga"


def search(q: str, linga: str = "") -> dict[str, Any]:
    """शब्द खोजें: list matches, which word/cell an inflected form is, and the stem to build a table for."""
    q = q.strip()
    slp = dev_to_slp1(q) if any("\u0900" <= ch <= "\u097f" for ch in q) else q
    slp = slp.replace(" ", "")
    form_of = [{"stem": s, "stem_dev": dev(s), "linga": lg, "linga_dev": LINGA[lg],
                "cell": f"{VIBHAKTI[i // 3 + 1]} {VACANA[i % 3 + 1]}"} for s, lg, i in _form_index().get(slp, [])][:8]
    nouns = [r for r in noun_pool() if r["stem"].startswith(slp)][:40]
    roots = [{"ref": d["ref"], "dev": d["dev"], "gana": GANA[d["gana"]], "artha": d["artha"]}
             for d in dhatu_pool() if dev_to_slp1(d["dev"]) == slp or d["upadesha"].rstrip("~") == slp][:8]
    stem = slp
    if form_of and not any(r["stem"] == slp for r in nouns):
        stem = form_of[0]["stem"]
    return {"query": q, "slp1": slp, "dev": dev(slp), "form_of": form_of, "nouns": nouns, "roots": roots,
            "stem": stem, "stem_dev": dev(stem), "linga": linga or guess_linga(stem)}


def lists(family: str, q: str = "", anta: str = "", linga: str = "", limit: int = 200) -> list[dict[str, Any]]:
    """सूचियाँ: searchable word lists (SLP1 or Devanāgarī query)."""
    ql = dev_to_slp1(q) if q and any("\u0900" <= ch <= "\u097f" for ch in q) else q
    if family in ("noun", "pronoun", "number"):
        if family == "noun":
            rows = [{"stem": r["stem"], "linga": r["linga"], "dev": r["dev"], "artha": r["artha"]} for r in noun_pool()]
        else:
            src = PRONOUNS if family == "pronoun" else NUMBERS
            rows = [{"stem": s, "linga": _LG[c], "dev": dev(s), "artha": ""} for s, cs in src for c in dict.fromkeys(cs)]
        if ql:
            rows = [r for r in rows if r["stem"].startswith(ql)]
        if anta in ("ajanta", "halanta"):
            rows = [r for r in rows if _ending(r["stem"]) == anta]
        elif anta:
            rows = [r for r in rows if r["stem"].endswith(anta)]
        if linga:
            rows = [r for r in rows if r["linga"] == linga]
        return rows[:limit]
    if family in ("verb", "krdanta"):
        rows = dhatu_pool()
        if ql:
            rows = [d for d in rows if d["upadesha"].startswith(ql) or dev_to_slp1(d["dev"]).startswith(ql)]
        return [{"ref": d["ref"], "dev": d["dev"], "gana": GANA[d["gana"]], "artha": d["artha"], "pada": d["pada"]}
                for d in rows[:limit]]
    if family == "namadhatu":
        return [{"stem": s, "pratyaya": p, "dev": f"{dev(s)} + {NAMA_DEV[p]}"} for s, p in NAMADHATU]
    return []
