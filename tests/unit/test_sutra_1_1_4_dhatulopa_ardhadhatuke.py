"""
1.1.4 न धातुलोप आर्धधातुके — *ik* *guṇa* / *vṛddhi* sthāyin N/A when ārdhat + dhatu-lopa.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_4 as s114


def test_metadata():
    r = SUTRA_REGISTRY["1.1.4"]
    assert r.sutra_type is SutraType.PARIBHASHA
    assert "na" in r.text_slp1 or "DAt" in r.text_slp1


def test_ik_guna_vriddhi_blocked_requires_both_flags():
    s0 = State(terms=[Term(kind="prakriti", varnas=[mk("a")])])
    assert not s114.ik_guna_vriddhi_blocked_by_1_1_4(s0)
    t_ardh = Term(kind="pratyaya", varnas=[mk("a")], tags={"ardhadhatuka"})
    # Only ārdhadhātuka — not enough.
    s1 = State(terms=[t_ardh], samjna_registry={})
    assert not s114.ik_guna_vriddhi_blocked_by_1_1_4(s1)
    t_lopa = Term(kind="prakriti", varnas=[mk("k")], tags={"dhatulopa"})
    s2 = State(terms=[t_ardh, t_lopa])
    assert s114.ik_guna_vriddhi_blocked_by_1_1_4(s2)
    t_both = Term(
        kind="prakriti", varnas=[mk("B")], tags={"ardhadhatuka", "dhatulopa"}
    )
    assert s114.ik_guna_vriddhi_blocked_by_1_1_4(State(terms=[t_both]))


def test_ik_guna_vriddhi_blocked_by_registry_ardhadhatuka():
    s = State(
        terms=[Term(kind="prakriti", varnas=[mk("a")], tags={"dhatulopa"})],
        samjna_registry={"3.4.114_ardhadhatuka": True},
    )
    assert s114.ik_guna_vriddhi_blocked_by_1_1_4(s)


def test_apply_rule_sets_paribhasha_and_is_idempotent():
    t = Term(
        kind="prakriti",
        varnas=[mk("S")],
        tags={"ardhadhatuka", "dhatulopa", "aNga"},
    )
    s = State(terms=[t])
    assert s114.GATE_KEY not in s.paribhasha_gates
    s1 = apply_rule("1.1.4", s)
    g = s1.paribhasha_gates.get(s114.GATE_KEY)
    assert g and g.get("dhatulopa_ardhadhatuke") is True
    s2 = apply_rule("1.1.4", s1)
    assert s2.paribhasha_gates[s114.GATE_KEY] == s1.paribhasha_gates[s114.GATE_KEY]


def test_apply_skipped_without_context():
    s = apply_rule("1.1.4", State(terms=[Term(kind="prakriti", varnas=[mk("a")])]))
    assert s114.GATE_KEY not in s.paribhasha_gates
