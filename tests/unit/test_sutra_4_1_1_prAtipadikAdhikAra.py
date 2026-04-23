"""
4.1.1 *ṅyāp-prātipadikāt* — *prātipadikādhikāraḥ* (ashtadhyayi i=41001; scope to
5.4.160).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["4.1.1"]
    assert r.sutra_id == "4.1.1"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("4.1.1", "5.4.160")
    assert "prAtipadikAt" in r.text_slp1
    assert "प्रातिपदिक" in r.why_dev


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("4.1.1", s0)
    assert any(e.get("id") == "4.1.1" for e in s1.adhikara_stack)
    s2 = apply_rule("4.1.1", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("4.1.1") == 1

