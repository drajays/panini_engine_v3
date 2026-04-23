"""
6.4.46 *ārdhadhātuke* — *ārdhadhātuke ityadhikāraḥ (dvitīyaḥ)*
(ashtadhyayi i=64046; scope to 6.4.70).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["6.4.46"]
    assert r.sutra_id == "6.4.46"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("6.4.46", "6.4.70")
    assert r.text_slp1 == "ArDadhAtuke"
    assert r.text_dev == "आर्धधातुके"


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("6.4.46", s0)
    assert any(e.get("id") == "6.4.46" for e in s1.adhikara_stack)
    s2 = apply_rule("6.4.46", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("6.4.46") == 1

