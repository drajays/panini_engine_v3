"""
3.1.22 *dhātor ekāco halādeḥ kriyāsamabhihāre yaṅ* — first *dhātv‑adhikāra*
(ashtadhyayi i=31022; scope to 3.1.90).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["3.1.22"]
    assert r.sutra_id == "3.1.22"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("3.1.22", "3.1.90")
    assert "yaG" in r.text_slp1
    assert "धातोरेकाचो" in r.text_dev


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("3.1.22", s0)
    assert any(e.get("id") == "3.1.22" for e in s1.adhikara_stack)
    s2 = apply_rule("3.1.22", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("3.1.22") == 1
