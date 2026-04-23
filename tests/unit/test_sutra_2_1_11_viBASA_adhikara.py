"""
2.1.11 *vibhāṣā* — adhikāra scope opener (ashtadhyayi i=21011).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["2.1.11"]
    assert r.sutra_id == "2.1.11"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("2.1.11", "2.2.38")
    assert r.text_dev == "विभाषा"
    assert "BASA" in r.text_slp1


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("2.1.11", s0)
    assert any(e.get("id") == "2.1.11" for e in s1.adhikara_stack)
    s2 = apply_rule("2.1.11", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("2.1.11") == 1

