"""
1.1.3 इको गुणवृद्धी — paribhāṣā gate for *ik* as *sthāyin* under *guṇa* / *vṛddhi*.
"""
from __future__ import annotations

import pytest

import sutras  # noqa: F401 — load registry

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk, pratyahara
from sutras.adhyaya_1.pada_1 import sutra_1_1_3 as s113


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.3"]
    assert r.sutra_id == "1.1.3"
    assert r.sutra_type is SutraType.PARIBHASHA
    assert "iko" in r.text_slp1


def test_gate_sets_ik_sthanin_and_is_idempotent():
    s = State(terms=[Term(kind="prakriti", varnas=[mk("a")])])
    assert s113.GATE_KEY not in s.paribhasha_gates
    s = apply_rule("1.1.3", s)
    gate = s.paribhasha_gates.get(s113.GATE_KEY)
    assert gate is not None
    assert gate["sthanin_ik_slp1"] == pratyahara.IK
    s2 = apply_rule("1.1.3", s)
    assert s2.paribhasha_gates == s.paribhasha_gates


def test_ik_sthanin_set_matches_pratyahara_ik():
    assert s113.ik_sthanin_set_slp1() == pratyahara.IK


@pytest.mark.parametrize(
    ("letter", "expected"),
    [("i", True), ("u", True), ("f", True), ("x", True), ("A", False), ("a", False), ("e", False)],
)
def test_is_guna_vriddhi_sthanin(letter: str, expected: bool):
    assert s113.is_guna_vriddhi_sthanin(letter) is expected


def test_ik_suppletion_context_table():
    assert s113.ik_suppletion_context(
        operation_named_guna_or_vriddhi=True, sthanin_explicit_in_triggering_sutra=False
    )
    assert not s113.ik_suppletion_context(
        operation_named_guna_or_vriddhi=False, sthanin_explicit_in_triggering_sutra=False
    )
    assert not s113.ik_suppletion_context(
        operation_named_guna_or_vriddhi=True, sthanin_explicit_in_triggering_sutra=True
    )
