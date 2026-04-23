"""
3.2.134 *ākveś tacchīla-taddharma-tatsādhukāriṣu* — *tācchīlyādhikāraḥ*
(ashtadhyayi i=32134; scope to 3.2.177).

Span matches v2 ``adhikara_prakarana.json`` sequence 21.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["3.2.134"]
    assert r.sutra_id == "3.2.134"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("3.2.134", "3.2.177")
    assert "A kve" in r.text_slp1
    assert "आक्वे" in r.text_dev


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("3.2.134", s0)
    assert any(e.get("id") == "3.2.134" for e in s1.adhikara_stack)
    s2 = apply_rule("3.2.134", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("3.2.134") == 1

