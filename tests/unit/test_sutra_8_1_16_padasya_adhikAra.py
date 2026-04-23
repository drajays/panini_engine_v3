"""
8.1.16 *padasya* — *padasya ityadhikāraḥ* (ashtadhyayi i=81016; scope to 8.3.55).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["8.1.16"]
    assert r.sutra_id == "8.1.16"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("8.1.16", "8.3.55")
    assert r.text_slp1 == "padasya"
    assert r.text_dev == "पदस्य"


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("8.1.16", s0)
    assert any(e.get("id") == "8.1.16" for e in s1.adhikara_stack)
    s2 = apply_rule("8.1.16", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("8.1.16") == 1

