"""अभ्यासशाला (docs/ABHYASA_PLAN.md): sanskritabhyas.in parity, the answer-key rule, the engine contract, the firewall."""
from __future__ import annotations

import inspect
import json
import re
from pathlib import Path

import pytest

from core import abhyasa as A

ROOT = Path(__file__).resolve().parents[2]


def _fake(vb: int, vc: int) -> str:
    """A distinct, well-formed SLP1 form per cell."""
    return "ka" + "kgcjtdpb"[vb - 1] + "aiu"[vc - 1]


def _no_vidyut(monkeypatch):
    monkeypatch.setattr(A, "vidyut", lambda req: None)


# ── parity with sanskritabhyas.in's menus and drill types ─────────────────────────────────────────

def test_catalog_has_every_sanskritabhyas_family_and_drill():
    fams = A.FAMILIES
    for f in ("noun", "pronoun", "number", "verb", "krdanta", "taddhita", "namadhatu", "sandhi", "varna"):
        assert f in fams, f
    for d in ("mcq", "recall", "match", "tf", "odd"):
        assert d in fams["noun"]["drills"] and d in fams["verb"]["drills"], d
    assert [lv["hi"] for lv in A.LEVELS] == ["आसान", "मध्यम", "कठिन", "वैयाकरण"]
    assert len(A.UPASARGA) == 22 and {"Ric", "san", "yaN", "yaNluk"} <= set(A.SANADI)
    assert set(A.LAKARA) == {"laT", "liT", "luT", "lRT", "loT", "laG", "liG", "AsIrliG", "luG", "lRG"}


# ── the engine contract (§5): renaming one of these breaks the drills ─────────────────────────────

@pytest.mark.parametrize("mod,fn,params", [
    ("pipelines.subanta", "derive", ["vibhakti", "vacana", "linga"]),
    ("pipelines.tinanta", "derive", ["lakara", "prayoga", "purusha", "vacana", "upasargas", "pada", "san_recipe", "nic_recipe"]),
    ("pipelines.krdanta", "derive_krdanta", ["vibhakti", "vacana", "linga"]),
    ("pipelines.krdanta", "build_dhatu_state", []),
    ("pipelines.taddhita_loop", "derive_taddhita", ["vibhakti", "vacana", "linga"]),
    ("pipelines.pada_samhita", "join", []),
    ("pipelines.it_prakarana", "run_it_prakarana", []),
    ("phonology.pratyahara", "build_pratyahara", []),
])
def test_engine_entry_points_the_drills_call(mod, fn, params):
    import importlib
    f = getattr(importlib.import_module(mod), fn)
    sig = inspect.signature(f).parameters
    for p in params:
        assert p in sig, f"{mod}.{fn} lost parameter {p!r} — update core/abhyasa.py and docs/ABHYASA_PLAN.md §5"


def test_firewall_engine_never_imports_the_practice_code():
    pat = re.compile(r"^\s*(from|import)\s+(core\.abhyasa|tools\.abhyasa_vidyut|tools\.build_abhyasa_bank|webui)", re.M)
    for top in ("engine", "sutras", "phonology", "pipelines"):
        for p in (ROOT / top).rglob("*.py"):
            assert not pat.search(p.read_text(encoding="utf-8")), p


# ── the answer key ────────────────────────────────────────────────────────────────────────────────

def test_agree_engine_first_vidyut_only_when_allowed():
    k = A._agree("rAmAt", ["rAmAt", "rAmAd"], ["rAmAt", "rAmAd"], strict=True)
    assert k["primary"] == "rAmAt" and k["accepted"] == ["rAmAt", "rAmAd"] and k["sources"][0] == "engine"
    assert A._agree("rAmAH", ["rAmasya"], [], strict=True) is None           # engine ≠ Vidyut: not asked
    loose = A._agree(None, ["praBAvayati"], [], strict=False)
    assert loose["sources"] == ["vidyut"] and loose["primary"] == "praBAvayati"


def test_noun_paradigm_from_engine_and_printed_corpus(monkeypatch):
    if not A.corpus():
        pytest.skip("ashtadhyayi.com shabda corpus not fetched")
    _no_vidyut(monkeypatch)
    A.noun_paradigm.cache_clear()
    p = A.noun_paradigm("rAma", "pulliṅga", True)
    by = {c["key"]: c for c in p["cells"]}
    assert by["6-3"]["primary"] == "rAmARAm" and "engine" in by["6-3"]["sources"]
    assert len(p["cells"]) >= 20
    A.noun_paradigm.cache_clear()


@pytest.mark.parametrize("drill", ["mcq", "recall", "tf", "match", "odd", "table"])
def test_paradigm_drills_are_well_formed(drill):
    import random
    cells = [{"key": f"{vb}-{vc}", "vibhakti": vb, "vacana": vc, "label": f"{A.VIBHAKTI[vb]} {A.VACANA[vc]}",
              "primary": _fake(vb, vc), "accepted": [_fake(vb, vc)], "sources": ["engine", "vidyut"]}
             for vb in range(1, 9) for vc in (1, 2, 3)]
    p = {"kind": "subanta", "title": "t", "cells": cells, "rows": A.VIBHAKTI[1:], "cols": A.VACANA[1:]}
    for seed in range(20):
        q = A.paradigm_question(p, drill, random.Random(seed), 3)
        if drill == "mcq":
            assert sum(o["slp1"] in q["accepted"] for o in q["options"]) == 1
            assert len(q["options"]) == 4
        elif drill == "tf":
            for s in q["statements"]:
                truth = any(c["label"] == s["label"] and s["form"]["slp1"] in c["accepted"] for c in cells)
                assert s["answer"] == truth
        elif drill == "match":
            assert len(q["pairs"]) == 5 and sorted(q["labels"]) == sorted(x["label"] for x in q["pairs"])
        elif drill == "odd" and "answer" in q:
            assert q["answer"] in {o["slp1"] for o in q["options"]}
        elif drill == "table":
            assert len(q["cells"]) == 24


def test_odd_one_out_never_picks_a_syncretic_form():
    """रामाभ्याम् is 3/4/5 dvivacana at once — it cannot be 'the odd one' against dvivacana."""
    import random
    cells = [{"key": f"{vb}-{vc}", "vibhakti": vb, "vacana": vc, "label": f"{vb}-{vc}",
              "primary": "rAmAByAm" if (vc == 2 and vb in (3, 4, 5)) else _fake(vb, vc),
              "accepted": ["rAmAByAm"] if (vc == 2 and vb in (3, 4, 5)) else [_fake(vb, vc)], "sources": ["engine"]}
             for vb in range(1, 8) for vc in (1, 2, 3)]
    p = {"kind": "subanta", "title": "t", "cells": cells, "rows": [], "cols": []}
    for seed in range(40):
        q = A.paradigm_question(p, "odd", random.Random(seed), 2)
        if "answer" in q and "द्विवचनम्" in q["reason"]:
            assert q["answer"] != "rAmAByAm"


# ── the bank (when built) ─────────────────────────────────────────────────────────────────────────

BANK = json.loads((ROOT / "data/practice/abhyasa_bank.json").read_text()) if (ROOT / "data/practice/abhyasa_bank.json").exists() else None
needs_bank = pytest.mark.skipif(BANK is None, reason="bank not built (tools/build_abhyasa_bank.py)")


@needs_bank
def test_bank_items_carry_a_check_and_an_answer():
    for fam, items in BANK["items"].items():
        if not isinstance(items, list):
            continue
        for x in items:
            assert x.get("check") in ("vidyut", "engine", "vidyut-sandhi"), (fam, x.get("id"))
            if fam in ("subanta", "tinanta"):
                assert x["cells"] and all(v for v in x["cells"].values()), x["id"]
            if fam in ("krdanta", "taddhita", "sandhi"):
                key = x.get("forms") or x.get("out")
                assert key, x["id"]
            if fam == "sandhi":
                assert not set(x["wrong"]) & set(x["out"]), x["id"]


@needs_bank
def test_bank_never_teaches_a_known_wrong_join():
    joins = {(x["a"], x["b"]): x["out"] for x in BANK["items"].get("sandhi", [])}
    if ("mahA", "fzi") in joins:                 # 1.1.51 uraṇ raparaḥ: a + ṛ → ar
        assert joins[("mahA", "fzi")] == ["maharzi"]


@needs_bank
def test_compose_grading_explains_a_wrong_case():
    V = BANK["items"].get("vakya")
    if not V or not any(L["sentences"] for L in V["lessons"]):
        pytest.skip("no vākya sentences in the bank")
    s = next(x for L in V["lessons"] for x in L["sentences"] if any(w["role"] == "karman" for w in x["words"]))
    right = [w["form"] for w in s["words"]]
    A.bank.cache_clear()
    assert A.grade_compose(s["id"], list(reversed(right)))["ok"]          # word order is free
    k = next(w for w in s["words"] if w["role"] == "karman")
    wrong_cell = next((f for key, fs in V["tables"]["nouns"][k["lemma"]]["cells"].items()
                       for f in fs if not key.startswith("2-") and f not in k["alts"]), None)
    if wrong_cell is None:
        pytest.skip("no contrasting cell")
    r = A.grade_compose(s["id"], [wrong_cell if f == k["form"] else f for f in right])
    assert not r["ok"]
    note = next(n for n in r["notes"] if n["status"] == "wrong")
    assert {x["id"] for x in note["sutras"]} >= {"1.4.49", "2.3.2"}


@needs_bank
def test_question_for_every_bank_family():
    A.bank.cache_clear()
    for fam, drill in (("sandhi", "mcq"), ("pratyahara", "tf"), ("it", "mcq"), ("vakya", "karaka")):
        try:
            q = A.question(fam, drill, 2, {}, seed=1)
        except LookupError:
            continue                              # family not built in this bank
        assert q["family"] == fam
