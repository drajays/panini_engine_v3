"""
2.3.1 *anabhihite* — adhikāra scope opener (ashtadhyayi i=23001).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["2.3.1"]
    assert r.sutra_id == "2.3.1"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("2.3.1", "2.3.73")
    assert r.text_dev == "अनभिहिते"
    assert "anabhihite" in r.text_slp1


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("2.3.1", s0)
    assert any(e.get("id") == "2.3.1" for e in s1.adhikara_stack)
    s2 = apply_rule("2.3.1", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("2.3.1") == 1

