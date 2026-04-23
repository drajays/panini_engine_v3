"""
7.2.91 *maparyantasya* — *maparyantasya ityadhikāraḥ* (ashtadhyayi i=72091; scope to 7.2.98).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["7.2.91"]
    assert r.sutra_id == "7.2.91"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("7.2.91", "7.2.98")
    assert r.text_slp1 == "maparyantasya"
    assert r.text_dev == "मपर्यन्तस्य"


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("7.2.91", s0)
    assert any(e.get("id") == "7.2.91" for e in s1.adhikara_stack)
    s2 = apply_rule("7.2.91", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("7.2.91") == 1

