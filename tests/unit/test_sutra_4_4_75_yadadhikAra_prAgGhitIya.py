"""
4.4.75 *prāg hitāt yat* — *yad-adhikāraḥ prāg-ghitīyaḥ* (ashtadhyayi i=44075;
scope to 5.1.136).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["4.4.75"]
    assert r.sutra_id == "4.4.75"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("4.4.75", "5.1.136")
    assert "yat" in r.text_slp1
    assert "प्राग्घित" in r.text_dev


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("4.4.75", s0)
    assert any(e.get("id") == "4.4.75" for e in s1.adhikara_stack)
    s2 = apply_rule("4.4.75", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("4.4.75") == 1

