"""
4.1.3 *striyām* — *strī-adhikāraḥ (dvitīyaḥ)* (ashtadhyayi i=41003; scope to
4.1.89).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["4.1.3"]
    assert r.sutra_id == "4.1.3"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("4.1.3", "4.1.89")
    assert r.text_slp1 == "striyAm"
    assert r.text_dev == "स्त्रियाम्"


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("4.1.3", s0)
    assert any(e.get("id") == "4.1.3" for e in s1.adhikara_stack)
    s2 = apply_rule("4.1.3", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("4.1.3") == 1

