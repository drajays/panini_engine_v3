"""
2.4.19 *tatpuruṣo'nañ karmadhārayaḥ* — adhikāra scope opener (ashtadhyayi i=24019).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["2.4.19"]
    assert r.sutra_id == "2.4.19"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("2.4.19", "2.4.25")
    assert r.text_dev == "तत्पुरुषोऽनञ् कर्मधारयः"
    assert "karmadhAraya" in r.text_slp1


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("2.4.19", s0)
    assert any(e.get("id") == "2.4.19" for e in s1.adhikara_stack)
    s2 = apply_rule("2.4.19", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("2.4.19") == 1

