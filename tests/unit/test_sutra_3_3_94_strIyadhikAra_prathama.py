"""
3.3.94 *striyām ktin* — *strī-adhikāraḥ (prathamaḥ)* (ashtadhyayi i=33094;
scope to 3.3.112).

Span matches v2 ``adhikara_prakarana.json`` sequence 25.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["3.3.94"]
    assert r.sutra_id == "3.3.94"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("3.3.94", "3.3.112")
    assert "ktin" in r.text_slp1
    assert "स्त्रियां" in r.text_dev


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("3.3.94", s0)
    assert any(e.get("id") == "3.3.94" for e in s1.adhikara_stack)
    s2 = apply_rule("3.3.94", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("3.3.94") == 1

