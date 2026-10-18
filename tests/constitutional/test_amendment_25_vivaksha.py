"""AMENDMENT 25 — vivakṣā inputs are closed, cited and read only where the sūtra itself names them."""
from __future__ import annotations

import ast
import json
import re
from pathlib import Path

import pytest

import sutras  # noqa: F401
from engine import SUTRA_REGISTRY, apply_rule
from engine.state import State, Term
from engine.vivaksha import schema
from phonology.varna import parse_slp1_upadesha_sequence

ROOT = Path(__file__).resolve().parents[2]
_SPLIT = re.compile(r"[\s\-,.;:|।॥()'\"]+")
_SID = re.compile(r"sutra_id\s*=\s*['\"](\d+\.\d+\.\d+)['\"]")


def _samagra_words(sid: str) -> set[str]:
    return set(_SPLIT.split(getattr(SUTRA_REGISTRY[sid], "samagra_slp1", "") or ""))


def test_schema_values_are_named_by_the_sutras_they_cite():
    for key, values in schema().items():
        for value, entry in values.items():
            assert entry["sutras"], f"{key}={value}: no citing sūtra"
            for sid in entry["sutras"]:
                assert _samagra_words(sid) & set(entry["forms"]), f"{key}={value}: {sid} does not name it"


def _vivaksita_calls(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and getattr(node.func, "id", getattr(node.func, "attr", None)) == "vivaksita":
            yield node


def test_vivaksita_only_for_a_meaning_the_sutra_names():
    for path in (ROOT / "sutras").rglob("*.py"):
        src = path.read_text(encoding="utf-8")
        if "vivaksita" not in src:
            continue
        sid = _SID.search(src)
        assert sid, f"{path}: vivaksita outside a sūtra file"
        for call in _vivaksita_calls(ast.parse(src)):
            args = call.args[1:3]
            assert len(args) == 2 and all(isinstance(a, ast.Constant) for a in args), f"{path}: vivaksita needs literals"
            key, value = (a.value for a in args)
            forms = schema()[key][value]["forms"]
            assert _samagra_words(sid.group(1)) & set(forms), f"{path}: asks {key}={value} but its samagra has none of {forms}"


_WRITERS = re.compile(r"set_vivaksha\(|\.vivaksha\[[^\]]+\]\s*=")


@pytest.mark.parametrize("base", ["engine", "sutras", "pipelines", "core", "tools"])
def test_vivaksha_set_only_by_tape_init(base):
    allowed = {ROOT / "engine" / "vivaksha.py"}
    for path in (ROOT / base).rglob("*.py"):
        if path in allowed or (ROOT / "engine" / "tape_init") in path.parents:
            continue
        assert not _WRITERS.search(path.read_text(encoding="utf-8")), f"{path} writes the vivakṣā"


def test_karmakatva_is_data_from_ashtadhyayi_com():
    data = json.loads((ROOT / "data" / "inputs" / "dhatu_karmakatva.json").read_text(encoding="utf-8"))
    assert set(data["values"].values()) <= {"sakarmaka", "akarmaka", "dvikarmaka"}
    src = Path.home() / "data-master" / "dhatu" / "data.txt"
    if src.exists():
        code = {"A": "akarmaka", "S": "sakarmaka", "D": "dvikarmaka"}
        site = {x["baseindex"]: code.get(x.get("karma")) for x in json.loads(src.read_text(encoding="utf-8"))["data"]}
        for pid, value in data["values"].items():
            assert site[pid] == value, f"{pid}: {value} but ashtadhyayi.com says {site[pid]}"
    from engine.tape_init.tinanta import dhatu_term_from_row
    from pipelines.dhatupatha import iter_dhatu_entries
    row = next(r for r in iter_dhatu_entries() if r["dhatupatha_id"] == "01.0001")
    assert dhatu_term_from_row(row, "kartari", "laT").meta["karmakatva"] == "akarmaka"     # bhū सत्तायाम्


def test_recipes_write_karmakatva_no_more_than_today():
    pat = re.compile(r"karmakatva\"\]\s*=|\"karmakatva\",|karmakatva=")
    hits = sum(len(pat.findall(p.read_text(encoding="utf-8")))
               for base in ("pipelines", "core") for p in (ROOT / base).rglob("*.py"))
    assert hits <= 1, f"{hits} recipe writes of karmakatva (ceiling 1: the bhāve fallback for gap rows)"


def test_dispatcher_stamps_origin_on_created_varnas_only():
    dh = Term(kind="prakriti", varnas=list(parse_slp1_upadesha_sequence("jan")), tags={"dhatu", "anga"},
              meta={"upadesha_slp1": "jana~"})
    tas = Term(kind="pratyaya", varnas=list(parse_slp1_upadesha_sequence("tas")),
               tags={"pratyaya", "kngiti", "tin_adesha_3_4_78"}, meta={"upadesha_slp1": "tas"})
    after = apply_rule("6.4.42", State(terms=[dh, tas]))
    assert "".join(v.slp1 for v in after.terms[0].varnas) == "jaA"
    assert "origin:6.4.42" in after.terms[0].varnas[-1].tags
    assert not any("origin:6.4.42" in v.tags for v in after.terms[0].varnas[:-1] + after.terms[1].varnas)
    assert not any(g.startswith("__present") for t in after.terms for v in t.varnas for g in v.tags)
