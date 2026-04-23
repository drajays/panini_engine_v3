"""
1.1.13 शे — paribhāṣā gate ( *aś* / *ś* locus vs *pragṛhya*; *samāsa* / *sup* *prayoga*).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_13 as s1113


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.13"]
    assert r.sutra_id == "1.1.13"
    assert r.sutra_type is SutraType.PARIBHASHA
    assert r.text_slp1 == "Se"
    assert r.text_dev == "शे"


def test_gate_set_and_idempotent():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    assert s1113.GATE_KEY not in s0.paribhasha_gates
    s1 = apply_rule("1.1.13", s0)
    assert s1113.Se_gate_is_set(s1)
    assert s1.paribhasha_gates[s1113.GATE_KEY].get("active") is True
    s2 = apply_rule("1.1.13", s1)
    assert s2.paribhasha_gates == s1.paribhasha_gates


def test_Se_gate_is_set_false_initially():
    s = State(terms=[Term(kind="prakriti", varnas=[mk("k")])])
    assert not s1113.Se_gate_is_set(s)
