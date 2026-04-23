"""
5.3.2 *kiṃ-sarvanāma-bahubhyo 'dvyādibhyaḥ* — *kiṃsarvanāmādiprakṛtyadhikāraḥ*
(ashtadhyayi i=53002; scope to 5.3.26).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["5.3.2"]
    assert r.sutra_id == "5.3.2"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("5.3.2", "5.3.26")
    assert "sarvanAma" in r.text_slp1
    assert "किंसर्वनाम" in r.text_dev


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("5.3.2", s0)
    assert any(e.get("id") == "5.3.2" for e in s1.adhikara_stack)
    s2 = apply_rule("5.3.2", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("5.3.2") == 1

