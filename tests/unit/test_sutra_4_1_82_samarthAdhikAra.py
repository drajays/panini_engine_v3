"""
4.1.82 *samarthānām prathamād vā* — *samarthādhikāraḥ* (ashtadhyayi i=41082;
scope to 5.2.140).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["4.1.82"]
    assert r.sutra_id == "4.1.82"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("4.1.82", "5.2.140")
    assert "samarth" in r.text_slp1
    assert "prathamAt" in r.text_slp1
    assert "NyAp" in r.text_slp1
    assert "taddhitaH" in r.text_slp1
    assert "समर्थ" in r.text_dev
    assert "ङ्याप्प्रातिपदिकात्" in r.text_dev
    assert r.anuvritti_from == ("3.1.1", "3.1.2", "3.1.3", "4.1.1", "4.1.76")


def test_act_pushes_scope_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("4.1.82", s0)
    assert any(e.get("id") == "4.1.82" for e in s1.adhikara_stack)
    s2 = apply_rule("4.1.82", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("4.1.82") == 1

