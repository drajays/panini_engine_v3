"""
3.1.97 *aco yat* — *kṛtya-saṃjñādhikāra* (ashtadhyayi i=31097; scope to 3.1.132).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["3.1.97"]
    assert r.sutra_id == "3.1.97"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("3.1.97", "3.1.132")
    assert r.text_slp1 == "aco yat"
    assert r.text_dev == "अचो यत्"


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("3.1.97", s0)
    assert any(e.get("id") == "3.1.97" for e in s1.adhikara_stack)
    s2 = apply_rule("3.1.97", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("3.1.97") == 1
