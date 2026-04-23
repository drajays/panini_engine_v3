"""
1.1.5 क्ङिति — 1.1.3 *ik* *guṇa* / *vṛddhi* not in locus of *kit* pratyāya.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_5 as s115


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.5"]
    assert r.sutra_id == "1.1.5"
    assert r.sutra_type is SutraType.PARIBHASHA
    assert "KNG" in r.text_slp1 or "kiti" in r.text_slp1.lower()


def test_blocked_false_without_kngiti():
    s = State(terms=[Term(kind="pratyaya", varnas=[mk("a")], tags=set())])
    assert not s115.ik_guna_vriddhi_blocked_by_1_1_5(s)
    s2 = State(
        terms=[Term(kind="prakriti", varnas=[mk("k")], tags=set())],
        samjna_registry={},
    )
    assert not s115.ik_guna_vriddhi_blocked_by_1_1_5(s2)


def test_blocked_by_tag_or_registry():
    s_tag = State(
        terms=[Term(
            kind="pratyaya",
            varnas=[mk("N"), mk("v")],
            tags={"kngiti", "krt_pratyaya"},
        )],
    )
    assert s115.ik_guna_vriddhi_blocked_by_1_1_5(s_tag)
    s_reg = State(
        terms=[],
        samjna_registry={"1.1.5_kngiti": True},
    )
    assert s115.ik_guna_vriddhi_blocked_by_1_1_5(s_reg)


def test_apply_rule_idempotent_with_gate():
    t = Term(
        kind="pratyaya",
        varnas=[mk("N"), mk("v")],
        tags={"kngiti", "krt_pratyaya"},
    )
    s0 = State(terms=[t])
    assert s115.GATE_KEY not in s0.paribhasha_gates
    s1 = apply_rule("1.1.5", s0)
    g = s1.paribhasha_gates.get(s115.GATE_KEY)
    assert g and g.get("kngiti") is True
    s2 = apply_rule("1.1.5", s1)
    assert s2.paribhasha_gates[s115.GATE_KEY] == s1.paribhasha_gates[s115.GATE_KEY]


def test_apply_skipped_when_context_absent():
    s = apply_rule("1.1.5", State(terms=[Term(kind="pratyaya", varnas=[mk("i")], tags=set())]))
    assert s115.GATE_KEY not in s.paribhasha_gates
