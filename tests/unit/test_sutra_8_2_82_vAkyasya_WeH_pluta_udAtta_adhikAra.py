"""
8.2.82 *vākyasya ṭeḥ pluta udāttaḥ* — *vākyasya ṭeḥ pluta udātta ityadhikāraḥ*
(ashtadhyayi i=82082; scope to 8.2.108).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["8.2.82"]
    assert r.sutra_id == "8.2.82"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("8.2.82", "8.2.108")
    assert "pluta" in r.text_slp1
    assert "उदात्त" in r.text_dev


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("8.2.82", s0)
    assert any(e.get("id") == "8.2.82" for e in s1.adhikara_stack)
    s2 = apply_rule("8.2.82", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("8.2.82") == 1

