"""
3.3.19 *akartari ca kārake saṃjñāyām* — adhikāra (ashtadhyayi i=33019; scope to
3.3.112).

Span matches v2 ``adhikara_prakarana.json`` sequence 24.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["3.3.19"]
    assert r.sutra_id == "3.3.19"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("3.3.19", "3.3.112")
    assert "akartari" in r.text_slp1
    assert "अकर्तरि" in r.text_dev


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("3.3.19", s0)
    assert any(e.get("id") == "3.3.19" for e in s1.adhikara_stack)
    s2 = apply_rule("3.3.19", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("3.3.19") == 1

