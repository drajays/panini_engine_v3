"""
8.3.57 *iṇkoḥ* — *iṇkoḥ ityadhikāraḥ* (ashtadhyayi i=83057; scope to 8.3.119).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["8.3.57"]
    assert r.sutra_id == "8.3.57"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("8.3.57", "8.3.119")
    assert r.text_slp1 == "iNkoH"
    assert r.text_dev == "इण्कोः"


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("8.3.57", s0)
    assert any(e.get("id") == "8.3.57" for e in s1.adhikara_stack)
    s2 = apply_rule("8.3.57", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("8.3.57") == 1

