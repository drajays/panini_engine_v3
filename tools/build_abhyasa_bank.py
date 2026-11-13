"""
tools/build_abhyasa_bank.py — the अभ्यासशाला answer bank: engine derivations, cross-checked with Vidyut.

    .venv/bin/python -m tools.build_abhyasa_bank                    # every family (~30–60 min, serial, niced)
    .venv/bin/python -m tools.build_abhyasa_bank --only sandhi,varna # some families; the rest are kept from the old bank

Writes ``data/practice/abhyasa_bank.json`` (SLP1 forms, committed) and ``data/practice/abhyasa_gaps.json``
(every cell where the engine's form is not among Vidyut's: a work queue for the engine agents).

Rules (docs/ABHYASA_PLAN.md §3): the answer is the engine's form; an item enters the bank only when Vidyut has it too
(``check: "vidyut"``), or — for families Vidyut cannot check (sandhi, pratyāhāra, it-saṃjñā) — from the engine
alone with its sūtra path (``check: "engine"``). Needs the repo's ``.venv`` (engine + vidyut in one interpreter).
Presentation tooling: never imported by engine / sutras / phonology / pipelines.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import random
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

OUT = ROOT / "data" / "practice" / "abhyasa_bank.json"
GAPS = ROOT / "data" / "practice" / "abhyasa_gaps.json"
LEXICON = ROOT / "data" / "practice" / "vakya_lexicon.json"

FAMILIES = ("varna", "it", "sandhi", "subanta", "tinanta", "krdanta", "taddhita", "vakya")
DB_LAKARA = {"vidhiliG": "liG", "ASIrliG": "AsIrliG"}          # forms.db spellings → tinanta.derive keys
GAPS_OUT: list[dict[str, Any]] = []
SUTRA_TEXT: dict[str, str] = {}


def log(*a: Any) -> None:
    print(time.strftime("%H:%M:%S"), *a, file=sys.stderr, flush=True)


@contextlib.contextmanager
def quiet():
    with contextlib.redirect_stdout(io.StringIO()):
        yield


def dev(slp1: str) -> str:
    from core.transliterate import slp1_to_dev
    return " ".join(slp1_to_dev(w) for w in slp1.split())


def gap(family: str, request: dict, engine: Any, vidyut: Any, note: str = "") -> None:
    GAPS_OUT.append({"family": family, "request": request, "engine": engine, "vidyut": vidyut, "note": note})


def steps_of(trace: list[dict]) -> list[list[str]]:
    """Surface-changing sūtra steps: [sūtra id, before (Dev), after (Dev)]."""
    from core.trace_view import enrich_trace, filter_surface_changed
    out = []
    for s in filter_surface_changed(enrich_trace(list(trace))):
        sid = s.get("sutra_id") or ""
        if not sid or sid.startswith("__") or not s.get("_sutra_text_dev"):
            continue
        SUTRA_TEXT.setdefault(sid, s["_sutra_text_dev"])
        out.append([sid, s.get("form_before_dev", ""), s.get("form_after_dev", "")])
    return out


def path_ok(steps: list[list[str]], vidyut_paths: list[set[str]]) -> bool:
    """Every surface-changing engine sūtra is also on (some) Vidyut path (core/practice.path_ok_keys rule)."""
    ours = {s[0] for s in steps}
    return bool(ours) and any(ours <= p for p in vidyut_paths)


# ── Vidyut, in-process (tools/abhyasa_vidyut.Vidyut) ─────────────────────────────────────────────

from tools.abhyasa_vidyut import Vidyut  # noqa: E402


# ── families ────────────────────────────────────────────────────────────────────────────────────

PRATYAHARAS = [  # (name, first letter, closing it-letter); level 1 = the ones a beginner meets first
    ("ac", "a", "c", 1), ("hal", "h", "l", 1), ("ik", "i", "k", 1), ("ak", "a", "k", 1), ("ec", "e", "c", 1),
    ("eN", "e", "N", 1), ("yaR", "y", "R", 1), ("al", "a", "l", 1), ("uk", "u", "k", 2), ("Ec", "E", "c", 2),
    ("aw", "a", "w", 2), ("am", "a", "m", 2), ("aS", "a", "S", 2), ("yam", "y", "m", 2), ("Yam", "Y", "m", 2),
    ("Nam", "N", "m", 2), ("Jaz", "J", "z", 2), ("Baz", "B", "z", 2), ("jaS", "j", "S", 2), ("baS", "b", "S", 2),
    ("JaS", "J", "S", 2), ("haS", "h", "S", 2), ("vaS", "v", "S", 2), ("Jay", "J", "y", 2), ("Kay", "K", "y", 2),
    ("may", "m", "y", 2), ("yay", "y", "y", 2), ("cay", "c", "y", 2), ("Kar", "K", "r", 2), ("car", "c", "r", 2),
    ("Sar", "S", "r", 2), ("yar", "y", "r", 2), ("Jar", "J", "r", 2), ("Sal", "S", "l", 2), ("Jal", "J", "l", 2),
    ("ral", "r", "l", 2), ("val", "v", "l", 2), ("Cav", "C", "v", 2),
]


def build_varna() -> list[dict]:
    """1.1.71 ādir antyena sahetā, computed by phonology.pratyahara over the Māheśvara-sūtras."""
    from phonology.maheshvara import ordered_phoneme_sequence
    from phonology.pratyahara import build_pratyahara
    order = {p: i for i, p in enumerate(dict.fromkeys(ordered_phoneme_sequence()))}
    out = []
    for name, start, it, level in PRATYAHARAS:
        try:
            members = sorted(build_pratyahara(start, it), key=lambda p: order.get(p, 99))
        except ValueError:
            continue
        out.append({"id": f"pr:{name}", "name": name, "name_dev": dev(name), "members": members,
                    "members_dev": [dev(m) for m in members], "level": level, "sutra": "1.1.71", "check": "engine"})
    return out


IT_JOBS = {
    "krt": ["Rvul", "tfc", "ktvA", "ktavatu", "Satf", "SAnac", "GaY", "lyuw", "Kac", "kvip", "Ryat", "anIyar",
            "tumun", "ktin", "Rini", "kvasu", "lyap", "Ramul", "kAnac", "Sa"],
    "taddhita": ["aR", "iY", "Wak", "WaY", "Qak", "cPaY", "matup", "mayaw", "tasil", "tral", "Ca", "yat", "tal",
                 "Pak", "Ryat", "vati", "tarap", "tamap", "izWan", "Iyasun"],
    "sup": ["su~", "jas", "Sas", "wA", "Ne", "Nasi~", "Nas", "Ni", "Am", "Ow", "Bis", "Byas", "sup"],
    "tin": ["tip", "tas", "Ji", "sip", "Tas", "mip", "vas", "mas", "ta", "AtAm", "Ja", "TAs", "iw", "mahiN"],
}
IT_DHATUS = ["BU", "qupacaz", "qukfY", "gamx~", "dfSi~r", "eDa~", "wunadi~", "YimidA~", "SIN", "dIN", "kzuBa~",
             "Ricakz", "RIY", "hfY", "yaja~", "vada~", "Bidi~r", "ruDi~r", "qudAY", "Sru", "Yizva\\pa~", "tanu~",
             "krIY", "cura~", "kfza~", "mfjU~", "vfDu~", "SAsu~", "Divi~", "kramu~"]


def build_it() -> list[dict]:
    """1.3.2–1.3.9 through pipelines.it_prakarana, one upadeśa at a time (as tools/it_report)."""
    from engine.it_samjna import it_records
    from phonology.joiner import slp1_to_devanagari
    from phonology.varna import parse_slp1_upadesha_sequence
    from pipelines.it_prakarana import run_it_prakarana
    from tools.it_report import _dhatu_state, _pratyaya_state
    jobs = [("dhatu", d) for d in IT_DHATUS] + [(k, u) for k, us in IT_JOBS.items() for u in us]
    out = []
    for kind, up in jobs:
        try:
            with quiet():
                st = _dhatu_state(up) if kind == "dhatu" else _pratyaya_state(up, kind)
                upadesha = (st.terms[0].meta.get("upadesha_slp1") or up).strip()
                st = run_it_prakarana(st)
        except Exception as ex:  # noqa: BLE001
            log("it skip", up, type(ex).__name__, str(ex)[:80])
            continue
        t = st.terms[0]
        recs = [{"letters_dev": r["letters_dev"], "sutra": r.get("sutra") or "", "name": r.get("name") or "",
                 "name_dev": r.get("name_dev") or ""} for r in it_records(t)]
        for r in recs:
            if r["sutra"]:
                from engine import SUTRA_REGISTRY
                rec = SUTRA_REGISTRY.get(r["sutra"])
                if rec and rec.text_dev:
                    SUTRA_TEXT.setdefault(r["sutra"], rec.text_dev)
        out.append({"id": f"it:{kind}:{up}", "kind": kind, "upadesha": upadesha,
                    "upadesha_dev": slp1_to_devanagari(parse_slp1_upadesha_sequence(upadesha)),
                    "residue_dev": slp1_to_devanagari(t.varnas) or "∅", "its": recs,
                    "level": 3 if kind in ("dhatu", "sup", "tin") else 4, "check": "engine"})
    return out


SANDHI_PAIRS = [  # (left, right) padas — vowel seams the engine's 6.1 ac-sandhi pool handles today
    ("deva", "Alaya"), ("vidyA", "arTI"), ("hima", "Alaya"), ("ravi", "indra"), ("BAnu", "udaya"), ("kavi", "ISa"),
    ("mahA", "ASaya"), ("sura", "ari"), ("parama", "arTa"), ("SrI", "ISa"), ("guru", "upadeSa"), ("pitf", "fRa"),
    ("deva", "indra"), ("rAma", "ISvara"), ("mahA", "utsava"), ("gaNgA", "udaka"), ("sUrya", "udaya"), ("hita", "upadeSa"),
    ("mahA", "fzi"), ("deva", "fzi"), ("rAja", "fzi"), ("parama", "ISvara"), ("sadA", "eva"), ("tava", "eva"),
    ("deva", "ESvarya"), ("mahA", "ozaDi"), ("vana", "ozaDi"), ("mahA", "Ozaja"), ("jala", "oGa"), ("eka", "eka"),
    ("iti", "AdI"), ("devI", "Agamana"), ("prati", "eka"), ("iti", "atra"), ("su", "Agata"), ("anu", "aya"),
    ("maDu", "ari"), ("pitf", "AjYA"), ("nadI", "udaka"), ("vaDU", "Agamana"), ("yadi", "api"), ("asti", "atra"),
    ("nE", "aka"), ("pO", "aka"), ("hare", "ava"), ("vizRo", "ava"), ("te", "atra"),
    ("vane", "asmin"), ("ko", "api"), ("sO", "api"), ("tO", "api"), ("deva", "Ayatana"), ("mAtf", "arTa"),
    ("guru", "AjYA"), ("pustaka", "Alaya"), ("muni", "indra"), ("laGu", "Urmi"), ("na", "iti"),
]
SANDHI_RULE = {  # the ac-sandhi sūtra that decides the seam → (label, Dev label, level)
    "6.1.101": ("dIrGa", "सवर्णदीर्घः", 1), "6.1.87": ("guRa", "गुणः", 1), "6.1.88": ("vfdDi", "वृद्धिः", 2),
    "6.1.77": ("yaR", "यण्", 2), "6.1.78": ("ayAdi", "अयादिः", 2), "6.1.109": ("pUrvarUpa", "पूर्वरूपम्", 3),
    "6.1.94": ("pararUpa", "पररूपम्", 3), "6.1.125": ("prakftiBAva", "प्रकृतिभावः", 3), "6.1.89": ("vfdDi", "वृद्धिः", 3),
    "6.1.97": ("pararUpa", "पररूपम्", 3), "6.1.111": ("ut", "उत्", 3),
}
_LONG = {"a": "A", "i": "I", "u": "U", "f": "F", "A": "A", "I": "I", "U": "U", "F": "F"}
_GUNA = {"a": "a", "A": "a", "i": "e", "I": "e", "u": "o", "U": "o", "f": "ar", "F": "ar"}
_VRDDHI = {"a": "A", "i": "E", "I": "E", "u": "O", "U": "O", "f": "Ar", "e": "E", "o": "O"}
_YAN = {"i": "y", "I": "y", "u": "v", "U": "v", "f": "r", "F": "r"}


def _wrong_joins(a: str, b: str) -> list[str]:
    """Plausible wrong answers (display only — every one is checked to be NOT an accepted answer)."""
    x, y, rest = a[-1], b[0], b[1:]
    head = a[:-1]
    c = [a + b, a + " " + b, head + _LONG.get(x, x) + rest, head + _GUNA.get(y, y) + rest,
         head + _VRDDHI.get(y, y) + rest, head + _YAN.get(x, x) + b, head + _GUNA.get(x, x) + b,
         head + _VRDDHI.get(x, x) + rest, a + rest]
    return list(dict.fromkeys(w for w in c if w))


def build_sandhi(V: Vidyut) -> list[dict]:
    from pipelines.pada_samhita import join
    out = []
    for a, b in SANDHI_PAIRS:
        try:
            with quiet():
                s = join(a, b)
        except Exception as ex:  # noqa: BLE001 — consonant seams: 8.x across padas is not built yet
            log("sandhi skip", a, b, str(ex)[:60])
            continue
        res = s.flat_slp1().replace(" ", "")
        ok = V.split_back(res, a, b)
        if ok is False and "6.1.109" in {t.get("sutra_id") for t in s.trace}:
            ok = V.split_back(res.replace(a, a + "'", 1), a, b)   # written with avagraha: हरेऽव
        if ok is False:
            gap("sandhi", {"left": a, "right": b}, res, None, "Vidyut's sandhi rules cannot split the engine's join back")
            continue
        st = steps_of(s.trace)
        rule = next((SANDHI_RULE[x[0]] for x in st if x[0] in SANDHI_RULE), None)
        if rule is None:
            applied = [t.get("sutra_id") for t in s.trace if t.get("status") == "APPLIED"]
            rule = next((SANDHI_RULE[x] for x in applied if x in SANDHI_RULE), ("anya", "अन्यः", 3))
        wrong = [w for w in _wrong_joins(a, b) if w.replace(" ", "") != res]
        accepted = ([a + "'" + res[len(a):]] if rule[0] == "pUrvarUpa" and res.startswith(a) else []) + [res]
        wrong = [w for w in dict.fromkeys(wrong) if w.replace(" ", "") not in accepted][:6]
        out.append({"id": f"sandhi:{a}+{b}", "a": a, "b": b, "a_dev": dev(a), "b_dev": dev(b), "out": accepted,
                    "out_dev": [dev(x.replace("'", "")) if "'" not in x else dev(x[:x.index("'")]) + "ऽ" + dev(x[x.index("'") + 1:])
                                for x in accepted],
                    "rule": rule[0], "rule_dev": rule[1], "level": rule[2], "steps": st,
                    "wrong": wrong, "wrong_dev": [dev(w) for w in wrong],
                    "check": "vidyut-sandhi" if ok else "engine"})
    return out


# subanta: lemma, liṅgas, group, level (forms.db lemmas are added from the verified index)
SUB_LIVE = [
    ("bAla", ["pulliṅga"], "noun", 1), ("bAlikA", ["strīliṅga"], "noun", 1), ("kanyA", ["strīliṅga"], "noun", 1),
    ("sItA", ["strīliṅga"], "noun", 1), ("nfpa", ["pulliṅga"], "noun", 1), ("aSva", ["pulliṅga"], "noun", 1),
    ("mfga", ["pulliṅga"], "noun", 1), ("odana", ["pulliṅga"], "noun", 1), ("jala", ["napuṃsaka"], "noun", 1),
    ("kzIra", ["napuṃsaka"], "noun", 1), ("puzpa", ["napuṃsaka"], "noun", 1), ("patra", ["napuṃsaka"], "noun", 1),
    ("grAma", ["pulliṅga"], "noun", 1), ("nagara", ["napuṃsaka"], "noun", 1), ("gfha", ["napuṃsaka"], "noun", 1),
    ("udyAna", ["napuṃsaka"], "noun", 1), ("Asana", ["napuṃsaka"], "noun", 1), ("ratha", ["pulliṅga"], "noun", 1),
    ("hasta", ["pulliṅga"], "noun", 1), ("lekhanI", ["strīliṅga"], "noun", 2), ("pitf", ["pulliṅga"], "noun", 2),
    ("mAtf", ["strīliṅga"], "noun", 2), ("dAtf", ["pulliṅga"], "noun", 2), ("vAri", ["napuṃsaka"], "noun", 2),
    ("maDu", ["napuṃsaka"], "noun", 2), ("sADu", ["pulliṅga"], "noun", 2), ("rAjan", ["pulliṅga"], "noun", 3),
    ("Atman", ["pulliṅga"], "noun", 3), ("nAman", ["napuṃsaka"], "noun", 3), ("manas", ["napuṃsaka"], "noun", 3),
    ("vAc", ["strīliṅga"], "noun", 3), ("marut", ["pulliṅga"], "noun", 3), ("jagat", ["napuṃsaka"], "noun", 3),
    ("Bagavat", ["pulliṅga"], "noun", 3), ("sarit", ["strīliṅga"], "noun", 3), ("vidvas", ["pulliṅga"], "noun", 4),
    ("asmad", ["pulliṅga"], "pronoun", 2), ("yuzmad", ["pulliṅga"], "pronoun", 2),
    ("tad", ["pulliṅga", "strīliṅga", "napuṃsaka"], "pronoun", 2), ("yad", ["pulliṅga", "strīliṅga", "napuṃsaka"], "pronoun", 3),
    ("etad", ["pulliṅga", "strīliṅga", "napuṃsaka"], "pronoun", 3), ("kim", ["pulliṅga", "strīliṅga", "napuṃsaka"], "pronoun", 3),
    ("idam", ["pulliṅga", "strīliṅga", "napuṃsaka"], "pronoun", 4), ("adas", ["pulliṅga", "strīliṅga", "napuṃsaka"], "pronoun", 4),
    ("Bavat", ["pulliṅga"], "pronoun", 3), ("sarva", ["strīliṅga", "napuṃsaka"], "pronoun", 2),
    ("eka", ["strīliṅga", "napuṃsaka"], "numeral", 3), ("dvi", ["strīliṅga", "napuṃsaka"], "numeral", 3),
    ("tri", ["pulliṅga", "strīliṅga", "napuṃsaka"], "numeral", 3), ("catur", ["pulliṅga", "strīliṅga", "napuṃsaka"], "numeral", 3),
    ("paYcan", ["pulliṅga"], "numeral", 3), ("zaz", ["pulliṅga"], "numeral", 3), ("saptan", ["pulliṅga"], "numeral", 4),
    ("azwan", ["pulliṅga"], "numeral", 4), ("navan", ["pulliṅga"], "numeral", 4), ("daSan", ["pulliṅga"], "numeral", 4),
]
SARVANAMA_DB = {"sarva", "viSva", "uBa", "uBaya", "anya", "anyatara", "itara", "katara", "katama", "yatara", "yatama",
                "tatara", "tatama", "ekatara", "ekatama", "tva", "tvat", "nema", "sima", "pUrva", "para", "avara",
                "dakziRa", "uttara", "apara", "aDara", "sama", "priya-viSva"}
RARE_DB = {"katara", "katama", "yatara", "yatama", "tatara", "tatama", "ekatara", "ekatama", "tva", "tvat", "nema",
           "sima", "dvyaha-pUrva", "tryaha-pUrva", "mAsa-pUrva", "priya-viSva", "anyatara", "nirjara"}
NUMERAL_DB = {"eka", "dvi", "dvitIya", "praTama"}


def _anta(stem: str) -> str:
    return stem[-1]


def _sub_level(lemma: str, group: str) -> int:
    if lemma in RARE_DB:
        return 4
    if group == "pronoun":
        return 2 if lemma == "sarva" else 3
    if group == "numeral":
        return 3
    return 1 if _anta(lemma) in "aA" else 2 if _anta(lemma) in "iIuUfF" else 3


def _paradigm_from_db(kind: str) -> dict[tuple, dict]:
    """Verified forms.db cells: {(lemma, linga|ref, …): {cell: [forms]}} (empty when the local index is absent)."""
    try:
        from core.practice import _rows
        rows = _rows(kind, None, None)
    except Exception as ex:  # noqa: BLE001 — forms.db is local (gitignored); fall back to live derivation
        log("forms.db unavailable:", ex)
        return {}
    out: dict[tuple, dict] = {}
    for r in rows:
        f = r["features"]
        if kind == "subanta":
            key = (r["lemma"], f.get("linga"))
            cell = f"{f['vibhakti']}-{f['vacana']}"
        else:
            ref = r["cell_key"].split("@")[1].split(":")[0]
            key = (r["lemma"], ref, f["lakara"], f.get("prayoga", "kartari"))
            cell = f"{f['purusha']}-{f['vacana']}"
        out.setdefault(key, {}).setdefault(cell, [])
        if r["surface_slp1"] not in out[key][cell]:
            out[key][cell].append(r["surface_slp1"])
    return out


def _vac_ok(lemma: str, vac: int) -> bool:
    if lemma == "eka":
        return vac == 1
    if lemma == "dvi":
        return vac == 2
    if lemma in ("tri", "catur", "paYcan", "zaz", "saptan", "azwan", "navan", "daSan"):
        return vac == 3
    return True


def derive_sub_table(V: Vidyut, lemma: str, linga: str, *, with_steps: bool = True) -> dict:
    from pipelines.subanta import derive
    cells, steps = {}, {}
    for vb in range(1, 9):
        for vc in (1, 2, 3):
            if not _vac_ok(lemma, vc) or (lemma in ("asmad", "yuzmad") and vb == 8):
                continue
            req = {"stem": lemma, "linga": linga, "vibhakti": vb, "vacana": vc}
            try:
                with quiet():
                    st = derive(lemma, vb, vc, linga=linga)
                ours = st.flat_slp1()
            except Exception as ex:  # noqa: BLE001
                gap("subanta", req, f"{type(ex).__name__}: {ex}"[:120], None)
                continue
            forms, paths = V.sub(lemma, linga, vb, vc)
            if not forms:
                continue
            if ours not in forms:
                gap("subanta", req, ours, sorted(forms))
                continue
            cells[f"{vb}-{vc}"] = [ours]
            if with_steps:
                s = steps_of(st.trace)
                if path_ok(s, paths):
                    steps[f"{vb}-{vc}"] = s
    return {"cells": cells, "steps": steps}


def build_subanta(V: Vidyut, limit: int | None) -> list[dict]:
    out = []
    for (lemma, linga), cells in sorted(_paradigm_from_db("subanta").items()):
        group = "pronoun" if lemma in SARVANAMA_DB else "numeral" if lemma in NUMERAL_DB else "noun"
        if len(cells) < 8:
            continue
        out.append({"id": f"sub:{lemma}:{linga}", "kind": "subanta", "group": group, "lemma": lemma,
                    "lemma_dev": dev(lemma), "linga": linga, "anta": _anta(lemma), "level": _sub_level(lemma, group),
                    "cells": cells, "steps": {}, "source": "forms.db", "check": "vidyut"})
    have = {(x["lemma"], x["linga"]) for x in out}
    for lemma, lingas, group, level in SUB_LIVE[:limit]:
        for linga in lingas:
            if (lemma, linga) in have:
                continue
            t = derive_sub_table(V, lemma, linga)
            log("subanta", lemma, linga, len(t["cells"]), "cells")
            if len(t["cells"]) >= 3:
                out.append({"id": f"sub:{lemma}:{linga}", "kind": "subanta", "group": group, "lemma": lemma,
                            "lemma_dev": dev(lemma), "linga": linga, "anta": _anta(lemma), "level": level,
                            **t, "source": "live", "check": "vidyut"})
    return out


TIN_ROOTS = [  # (dhātupāṭha id, level of its kartari laṭ/loṭ/laṅ/lṛṭ) — ids, not upadeśas: homographs (asa~, jYA, zu …)
    ("01.0001", 1), ("01.0381", 1), ("01.1137", 1), ("01.1143", 1), ("01.1074", 1), ("01.0051", 1), ("01.1164", 1),
    ("01.0979", 1), ("01.0822", 1), ("01.0405", 1), ("01.0643", 1), ("01.1160", 1), ("01.0640", 1), ("01.0746", 1),
    ("01.1141", 1), ("01.0919", 1), ("01.1049", 1), ("01.1046", 1), ("01.0685", 2), ("01.0002", 2), ("01.0574", 2),
    ("01.1130", 2), ("01.0863", 2), ("01.1077", 2), ("01.1151", 2), ("02.0001", 3), ("02.0060", 3), ("02.0002", 3),
    ("02.0039", 3), ("02.0040", 3), ("02.0044", 3), ("02.0059", 3), ("02.0026", 3), ("03.0001", 3), ("03.0010", 3),
    ("03.0011", 3), ("03.0002", 3), ("04.0001", 3), ("04.0010", 2), ("04.0091", 3), ("05.0001", 3), ("05.0005", 3),
    ("01.1092", 3), ("05.0016", 3), ("06.0001", 3), ("06.0092", 2), ("06.0160", 3), ("06.0078", 3), ("06.0149", 3),
    ("07.0001", 3), ("07.0002", 3), ("07.0003", 3), ("07.0007", 3), ("08.0010", 3), ("08.0001", 3), ("09.0001", 3),
    ("09.0043", 3), ("09.0071", 3), ("10.0001", 3), ("10.0002", 3),
]
TIN_LAKARAS = ["laT", "loT", "laG", "lRT", "liG", "luT", "liT", "luG", "AsIrliG", "lRG"]


def _tin_level(base: int, gana: int, lakara: str, prayoga: str, pada: str | None) -> int:
    lv = base
    if lakara in ("liG", "luT"):
        lv = max(lv, 2)
    if lakara in ("liT", "luG", "AsIrliG", "lRG"):
        lv = max(lv, 3)
    if gana != 1:
        lv = max(lv, 3)
    if pada == "atmane":
        lv = max(lv, 2)
    if prayoga != "kartari":
        lv = 4
    return lv


def build_tinanta(V: Vidyut, limit: int | None) -> list[dict]:
    from pipelines.dhatupatha import resolve_dhatu_identifier
    from pipelines.tinanta import derive as tin_derive
    db = _paradigm_from_db("tinanta")
    out = []
    for up, base in TIN_ROOTS[:limit]:
        try:
            row = resolve_dhatu_identifier(up)
        except KeyError:
            log("tinanta: unknown root", up)
            continue
        ref, upa = row.get("dhatupatha_id"), row["upadesha_slp1"]
        if not ref:
            log("tinanta: no pāṭha id for", up)
            continue
        gana = int(ref.split(".")[0])
        meta = {"lemma": upa, "ref": ref, "lemma_dev": row.get("mula_dhatu_dev") or dev(upa), "gana": gana,
                "gana_dev": row.get("gana_label_dev", ""), "artha_dev": row.get("artha_dev", ""),
                "pada_label_dev": row.get("pada_label_dev", "")}
        for lak in TIN_LAKARAS:
            cells = {}
            for (lemma, r, flak, pray), c in db.items():
                if r == ref and DB_LAKARA.get(flak, flak) == lak and pray == "kartari":
                    cells = c
            src = "forms.db"
            if not cells:          # live: engine + Vidyut per cell
                src = "live"
                for pu in (3, 2, 1):
                    for vc in (1, 2, 3):
                        req = {"dhatu": ref, "lakara": lak, "purusha": pu, "vacana": vc}
                        try:
                            with quiet():
                                ours = tin_derive(row.get("id") or upa, lak, "kartari", pu, vc).flat_slp1()
                        except Exception as ex:  # noqa: BLE001
                            gap("tinanta", req, f"{type(ex).__name__}: {ex}"[:120], None)
                            continue
                        forms, _ = V.tin(upa, ref, lak, pu, vc)
                        if not forms:
                            continue
                        if ours not in forms:
                            gap("tinanta", req, ours, sorted(forms))
                            continue
                        cells[f"{pu}-{vc}"] = [ours]
            if len(cells) >= 5:
                out.append({"id": f"tin:{ref}:{lak}:kartari", "kind": "tinanta", **meta, "lakara": lak,
                            "prayoga": "kartari", "level": _tin_level(base, gana, lak, "kartari", None),
                            "cells": cells, "source": src, "check": "vidyut"})
        log("tinanta", up, ref)
    return out


KRT_VIVAKSHA = {  # the meaning that leads to each kṛt (AMENDMENT 25: a kṛt is chosen by meaning, never named)
    "ktvA": ({"kala": "pUrvakAla", "samAnakartfka": "samAnakartfka"}, "pulliṅga", True, 2),
    "tumun": ({"kala": "Bavizyat", "kriyArTA": "kriyArTA"}, "pulliṅga", True, 2),
    "kta": ({"kala": "BUta", "artha": "karman"}, "pulliṅga", False, 2),
    "ktavatu": ({"kala": "BUta", "artha": "kartf"}, "pulliṅga", False, 2),
    "Satf": ({"kala": "vartamAna", "samAnADikaraRa": "apraTamA"}, "pulliṅga", False, 3),
    "kftya": ({"krt": "kftya"}, "pulliṅga", False, 3),
    "Rvultfc": ({"krt": "Rvultfc"}, "pulliṅga", False, 3),
    "lyuw": ({"artha": "BAva"}, "napuṃsaka", False, 3),
    "GaY": ({"artha": "BAva"}, "pulliṅga", False, 3),
    "ktin": ({"artha": "BAva"}, "strīliṅga", False, 3),
}
KRT_ROOTS = ["01.1137", "01.0381", "08.0010", "01.0001", "01.1143", "01.1074", "01.1077", "03.0010", "01.1092",
             "09.0043", "01.1049", "01.1046", "01.1164", "06.0092", "01.0051", "01.1141", "01.0979", "01.0643", "01.0746",
             "01.0919", "10.0001", "01.0002", "01.1130", "01.1151"]
KRT_DEV = {"ktvA": "क्त्वा", "tumun": "तुमुन्", "kta": "क्त", "ktavatu": "क्तवतु", "Satf": "शतृ", "SAnac": "शानच्",
           "tavya": "तव्य", "tavyat": "तव्यत्", "anIyar": "अनीयर्", "yat": "यत्", "Ryat": "ण्यत्", "kyap": "क्यप्",
           "lyuw": "ल्युट्", "GaY": "घञ्", "ktin": "क्तिन्", "tfc": "तृच्", "Rvul": "ण्वुल्", "lyap": "ल्यप्",
           "kelimar": "केलिमर्", "ac": "अच्", "ap": "अप्"}
KRT_LEVEL = {"ktvA": 2, "tumun": 2, "kta": 2, "ktavatu": 2}


def _explore(fn: Callable[[], Any]):
    from engine.vikalpa import explore
    with quiet():
        return explore(fn)


def _origin(state, prefix: str = "origin_pratyaya:") -> str:
    tags = [x for t in state.terms for x in t.tags if x.startswith(prefix)]
    return tags[-1].split(":", 1)[1] if tags else ""


def build_krdanta(V: Vidyut, limit: int | None) -> list[dict]:
    from pipelines.dhatupatha import resolve_dhatu_identifier
    from pipelines.krdanta import derive_krdanta, derive_krdanta_stem
    out = []
    for up in KRT_ROOTS[:limit]:
        try:
            row = resolve_dhatu_identifier(up)
        except KeyError:
            continue
        ref, upa = row.get("dhatupatha_id"), row["upadesha_slp1"]
        if not ref:
            continue
        rid = row.get("id") or upa
        found: dict[str, dict] = {}
        for label, (viv, linga, avyaya, _lv) in KRT_VIVAKSHA.items():
            req = {"dhatu": ref, "vivaksha": viv, "linga": linga}
            if avyaya:
                fn = (lambda viv=viv: _stem_state(derive_krdanta_stem, rid, viv))
            else:
                fn = (lambda viv=viv, linga=linga: derive_krdanta(rid, 1, 1, linga, **viv))
            try:
                branches = _explore(fn)
            except Exception as ex:  # noqa: BLE001
                gap("krdanta", req, f"{type(ex).__name__}: {ex}"[:120], None)
                continue
            for b in branches:
                krt = _origin(b.state)
                if not krt or krt in found:
                    continue
                ours = b.surface_slp1.replace(" ", "")
                forms, paths = V.krt(upa, ref, krt)
                if not forms:
                    continue
                if ours not in forms:
                    gap("krdanta", {**req, "krt": krt}, ours, sorted(forms))
                    continue
                st = steps_of(b.state.trace)
                found[krt] = {"id": f"krt:{ref}:{krt}", "kind": "krdanta", "lemma": upa, "ref": ref,
                              "lemma_dev": row.get("mula_dhatu_dev") or dev(upa), "gana": int(ref.split(".")[0]),
                              "krt": krt, "krt_dev": KRT_DEV.get(krt, dev(krt)), "avyaya": avyaya, "linga": linga,
                              "vivaksha": viv, "forms": [ours], "steps": st if path_ok(st, paths) else [],
                              "level": KRT_LEVEL.get(krt, 3), "check": "vidyut"}
        out.extend(found.values())
        log("krdanta", up, sorted(found))
    return out


def _stem_state(_derive_stem, rid: str, viv: dict):
    """An avyaya kṛt (ktvā, tumun) as its stem, as ``derive_krdanta_stem`` makes it but keeping the State (trace, vikalpa
    choices): the engine does not yet run 1.1.40 + 2.4.82 sup-luk for kṛt avyayas, so the declined word is wrong
    (gatvAH). The stem stops before the tripāḍī; Vidyut rejects any stem a tripāḍī rule would still change."""
    from engine import origin
    from pipelines.krdanta import build_dhatu_state
    from tools.autonomy_report import run_autonomously
    s = build_dhatu_state(rid, **viv)
    s.phase = "upadesha"
    st = run_autonomously(s, "", rid, 300, stop_before_tripadi=True).state
    st.terms[-1].tags |= set(origin.record_from_terms(st.terms))
    return st


TADDHITA_JOBS = [  # (stem, vivakṣā taddhitArtha, level)
    ("upagu", "apatya", 3), ("daSaraTa", "apatya", 3), ("vasudeva", "apatya", 3), ("garga", "apatya", 4),
    ("aSvapati", "apatya", 4), ("dakza", "apatya", 3), ("kuru", "apatya", 4), ("Siva", "apatya", 3),
    ("Dana", "asti", 3), ("buddhi", "asti", 3), ("bala", "asti", 3), ("SrI", "asti", 3), ("gO", "asti", 4),
    ("mfd", "vikAra", 3), ("suvarRa", "vikAra", 4), ("agni", "devatA", 4), ("indra", "devatA", 4),
    ("grAma", "Seza", 4), ("rAzwra", "Seza", 4), ("mATura", "Bava", 4),
]


def build_taddhita(V: Vidyut, limit: int | None) -> list[dict]:
    from pipelines.taddhita_loop import derive_taddhita
    out = []
    for stem, artha, level in TADDHITA_JOBS[:limit]:
        req = {"stem": stem, "taddhitArtha": artha}
        try:
            branches = _explore(lambda stem=stem, artha=artha: derive_taddhita(stem, 1, 1, "pulliṅga", taddhitArtha=artha))
        except Exception as ex:  # noqa: BLE001
            gap("taddhita", req, f"{type(ex).__name__}: {ex}"[:120], None)
            continue
        seen = set()
        for b in branches:
            tad = _origin(b.state)
            ours = b.surface_slp1.replace(" ", "")
            if not tad or (tad, ours) in seen:
                continue
            seen.add((tad, ours))
            forms, paths = V.taddhita(stem, tad)
            if ours not in forms:
                gap("taddhita", {**req, "pratyaya": tad}, ours, sorted(forms),
                    "Vidyut lists one branch of an optional rule at times (e.g. 8.4.45 vā)" if forms else "")
                continue
            st = steps_of(b.state.trace)
            out.append({"id": f"tad:{stem}:{tad}", "kind": "taddhita", "stem": stem, "stem_dev": dev(stem),
                        "artha": artha, "pratyaya": tad, "pratyaya_dev": dev(tad), "forms": [ours],
                        "steps": st if path_ok(st, paths) else [], "level": level, "check": "vidyut"})
        log("taddhita", stem, artha, sorted(seen))
    return out


# ── vākya (sentence composition) ────────────────────────────────────────────────────────────────

def _en_np(n: dict, vac: int, pron: dict | None = None) -> str:
    if pron:
        return pron["en"][str(vac)]
    if n.get("proper"):
        return n["en"]
    if n.get("mass"):
        return n["en"]
    return {1: "the " + n["en"], 2: "the two " + (n["enPl"] or n["en"]), 3: "the " + (n["enPl"] or n["en"])}[vac]


def _en_verb(v: dict, lakara: str, person: int, vac: int) -> str:
    e = v["en"]
    third_sg = person == 3 and vac == 1
    return {"laT": e["s"] if third_sg else e["base"], "laG": e["past"], "lRT": "will " + e["base"],
            "loT": e["base"], "liG": "should " + e["base"]}[lakara]


def build_vakya(V: Vidyut, n_per_lesson: int = 30) -> dict:
    from pipelines.dhatupatha import resolve_dhatu_identifier
    from pipelines.tinanta import derive as tin_derive
    lex = json.loads(LEXICON.read_text(encoding="utf-8"))
    nouns = {n["id"]: n for n in lex["nouns"]}
    prons = {p["purusha"]: p for p in lex["pronouns"]}
    lakaras = sorted({la for L in lex["lessons"] for la in L["lakaras"]})
    tables_n: dict[str, dict] = {}
    for n in [*lex["nouns"], *lex["pronouns"]]:
        tables_n[n["id"]] = {"linga": n["linga"], **derive_sub_table(V, n["id"], n["linga"], with_steps=False)}
        log("vakya noun", n["id"], len(tables_n[n["id"]]["cells"]))
    tables_v: dict[str, dict] = {}
    for v in lex["verbs"]:
        row = resolve_dhatu_identifier(v["id"])
        ref, upa = row["dhatupatha_id"], row["upadesha_slp1"]
        kw = {"pada": v["pada"]} if v.get("pada") else {}
        cells: dict[str, dict] = {}
        for lak in lakaras:
            for pu in (1, 2, 3):
                for vc in (1, 2, 3):
                    try:
                        with quiet():
                            ours = tin_derive(row.get("id") or upa, lak, "kartari", pu, vc, **kw).flat_slp1()
                    except Exception as ex:  # noqa: BLE001
                        gap("tinanta", {"dhatu": ref, "lakara": lak, "purusha": pu, "vacana": vc}, str(ex)[:120], None)
                        continue
                    forms, _ = V.tin(upa, ref, lak, pu, vc, pada=v.get("pada"))
                    if forms and ours in forms:
                        cells.setdefault(lak, {})[f"{pu}-{vc}"] = [ours]
                    elif forms:
                        gap("tinanta", {"dhatu": ref, "lakara": lak, "purusha": pu, "vacana": vc}, ours, sorted(forms))
        tables_v[v["id"]] = {"ref": ref, "lemma_dev": row.get("mula_dhatu_dev") or dev(upa), "cells": cells}
        log("vakya verb", v["id"], {k: len(c) for k, c in cells.items()})

    def pick_noun(rng, types, used, vac_choices):
        cands = [n for n in lex["nouns"] if set(n["types"]) & set(types) and n["id"] not in used]
        if not cands:
            return None, None
        n = rng.choice(cands)
        vac = 1 if n.get("proper") or n.get("mass") else rng.choice(vac_choices)
        return n, vac

    lessons = []
    for L in lex["lessons"]:
        sents, i, tries = [], 0, 0
        while len(sents) < n_per_lesson and tries < n_per_lesson * 8:
            tries += 1
            rng = random.Random(f"{L['id']}-{i}-{tries}")
            frame = rng.choice(L["frames"])
            verbs = [v for v in lex["verbs"] if frame in v["frames"]]
            if not verbs:
                continue
            v = rng.choice(verbs)
            lak, person, vac = rng.choice(L["lakaras"]), rng.choice(L["persons"]), rng.choice(L["vacanas"])
            words, en, used = [], {}, set()
            if person in (1, 2):
                p = prons[person]
                cell = tables_n[p["id"]]["cells"].get(f"1-{vac}")
                if not cell:
                    continue
                words.append({"form": cell[0], "alts": cell, "lemma": p["id"], "kind": "pronoun", "role": "karta",
                              "vibhakti": 1, "vacana": vac, "linga": p["linga"]})
                en["K"] = _en_np({}, vac, p)
            else:
                types = v.get("karta") or (["human", "animal"] if frame in ("INTRANS", "MOTION", "LOC") else ["human"])
                n, kv = pick_noun(rng, types, used, L["vacanas"])
                if not n:
                    continue
                vac = kv
                cell = tables_n[n["id"]]["cells"].get(f"1-{vac}")
                if not cell:
                    continue
                used.add(n["id"])
                words.append({"form": cell[0], "alts": cell, "lemma": n["id"], "kind": "noun", "role": "karta",
                              "vibhakti": 1, "vacana": vac, "linga": n["linga"]})
                en["K"] = _en_np(n, vac)
            ok = True
            for role in lex["frames"][frame]["roles"][1:]:
                types = v.get(role) or {"adhikarana": ["place"], "karman": ["thing"]}.get(role, ["thing"])
                n, rv = pick_noun(rng, types, used, [1] if L["id"] in ("v1", "v2", "v3") else [1, 1, 2, 3])
                if not n:
                    ok = False
                    break
                vib = lex["karaka"][role]["vibhakti"]
                cell = tables_n[n["id"]]["cells"].get(f"{vib}-{rv}")
                if not cell:
                    ok = False
                    break
                used.add(n["id"])
                words.append({"form": cell[0], "alts": cell, "lemma": n["id"], "kind": "noun", "role": role,
                              "vibhakti": vib, "vacana": rv, "linga": n["linga"]})
                en[role] = _en_np(n, rv)
            vcell = tables_v[v["id"]]["cells"].get(lak, {}).get(f"{person}-{vac}")
            if not ok or not vcell:
                continue
            words.append({"form": vcell[0], "alts": vcell, "lemma": v["id"], "kind": "verb", "role": "kriya",
                          "lakara": lak, "purusha": person, "vacana": vac})
            tmpl = lex["frames"][frame]["en"]
            verb_en = _en_verb(v, lak, person, vac)
            sent = tmpl.replace("{V}", verb_en).format(**{k: val for k, val in en.items()})
            if lak == "loT":
                sent = "Let " + tmpl.replace("{K} {V}", "{K} " + v["en"]["base"]).format(**en)
            sent = sent[0].upper() + sent[1:]
            key = " ".join(w["form"] for w in words)
            if any(s["key"] == key for s in sents):
                continue
            sents.append({"id": f"{L['id']}-{len(sents) + 1:02d}", "en": sent, "frame": frame, "key": key, "words": words})
            i += 1
        lessons.append({**{k: L[k] for k in ("id", "level", "title", "deva", "about", "sutras", "frames", "lakaras")},
                        "sentences": [{k: s[k] for k in ("id", "en", "frame", "words")} for s in sents]})
        log("vakya lesson", L["id"], len(sents))
    for sid in {s for L in lex["lessons"] for s in L["sutras"]} | {x for k in lex["karaka"].values()
                                                                   for x in (k["role_sutra"], k["case_sutra"])} \
            | set(lex["purusha_sutras"].values()) | {lex["anabhihite"]}:
        _register_text(sid)
    return {"lessons": lessons, "karaka": lex["karaka"], "anabhihite": lex["anabhihite"],
            "purusha_sutras": lex["purusha_sutras"],
            "nouns": {n["id"]: {"en": n["en"], "linga": n["linga"], "dev": dev(n["id"])} for n in lex["nouns"]}
            | {p["id"]: {"en": p["en"]["1"], "linga": p["linga"], "dev": dev(p["id"])} for p in lex["pronouns"]},
            "verbs": {v["id"]: {"en": v["en"]["base"], "dev": tables_v[v["id"]]["lemma_dev"], "ref": tables_v[v["id"]]["ref"]}
                      for v in lex["verbs"]},
            "tables": {"nouns": {k: {"linga": t["linga"], "cells": t["cells"]} for k, t in tables_n.items()},
                       "verbs": {k: t["cells"] for k, t in tables_v.items()}}}


def _register_text(sid: str) -> None:
    from engine import SUTRA_REGISTRY
    rec = SUTRA_REGISTRY.get(sid)
    if rec and rec.text_dev:
        SUTRA_TEXT.setdefault(sid, rec.text_dev)


# ── main ────────────────────────────────────────────────────────────────────────────────────────

def _write(bank: dict, out_path: Path, done: list[str], commit: str, old_gaps: list[dict]) -> None:
    """Write the bank and the gap list after every family, so a late failure loses nothing."""
    try:
        import vidyut
        vv = getattr(vidyut, "__version__", "")
    except ImportError:
        vv = ""
    bank["meta"] = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "engine_commit": commit,
                    "vidyut_version": vv, "families_built": sorted(set(bank.get("meta", {}).get("families_built", [])) | set(done)),
                    "counts": {k: (len(v) if isinstance(v, list) else sum(len(L["sentences"]) for L in v["lessons"]))
                               for k, v in bank["items"].items()},
                    "doc": "docs/ABHYASA_PLAN.md"}
    bank["sutra_text"] = dict(sorted(SUTRA_TEXT.items()))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(bank, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    rebuilt = set(done) | ({"tinanta"} if "vakya" in done else set())
    kept = [g for g in old_gaps if g["family"] not in rebuilt]
    GAPS.write_text(json.dumps({"_doc": "Cells where the engine's form is not among Vidyut's (or the engine raised). "
                                        "Work queue for engine agents; see docs/ABHYASA_PLAN.md §6.",
                                "generated_at": bank["meta"]["generated_at"], "engine_commit": commit,
                                "gaps": kept + GAPS_OUT}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log("wrote", out_path, bank["meta"]["counts"], "gaps:", len(kept) + len(GAPS_OUT))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", default="", help="comma-separated families: " + ",".join(FAMILIES))
    ap.add_argument("--limit", type=int, default=None, help="first N lemmas/roots per family (smoke runs)")
    ap.add_argument("--sentences", type=int, default=30, help="sentences per vākya lesson")
    ap.add_argument("--out", default=str(OUT))
    args = ap.parse_args(argv)
    only = [f for f in args.only.split(",") if f] or list(FAMILIES)
    import sutras  # noqa: F401 — registry
    out_path = Path(args.out)
    bank = json.loads(out_path.read_text(encoding="utf-8")) if out_path.exists() else {}
    bank.setdefault("items", {})
    SUTRA_TEXT.update(bank.get("sutra_text", {}))
    old_gaps = json.loads(GAPS.read_text(encoding="utf-8")).get("gaps", []) if GAPS.exists() else []
    V = Vidyut()
    builders: dict[str, Callable[[], Any]] = {
        "varna": build_varna, "it": build_it, "sandhi": lambda: build_sandhi(V),
        "subanta": lambda: build_subanta(V, args.limit), "tinanta": lambda: build_tinanta(V, args.limit),
        "krdanta": lambda: build_krdanta(V, args.limit), "taddhita": lambda: build_taddhita(V, args.limit),
        "vakya": lambda: build_vakya(V, args.sentences),
    }
    commit = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    done: list[str] = []
    for fam in only:
        t = time.time()
        log("building", fam)
        bank["items"][fam] = builders[fam]()
        done.append(fam)
        _write(bank, out_path, done, commit, old_gaps)
        log(f"{fam}: {bank['meta']['counts'][fam]} items in {time.time() - t:.0f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
