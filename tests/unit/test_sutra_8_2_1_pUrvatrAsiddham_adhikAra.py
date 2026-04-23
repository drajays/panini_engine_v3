"""
8.2.1 *pūrvatrāsiddham* — *pūrvatrāsiddham ityadhikāraḥ* (ashtadhyayi i=82001; scope to 8.4.68).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_sutra_metadata():
    r = SUTRA_REGISTRY["8.2.1"]
    assert r.sutra_id == "8.2.1"
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("8.2.1", "8.4.68")
    assert r.text_slp1 == "pUrvatrAsiddham"
    assert r.text_dev == "पूर्वत्रासिद्धम्"


def test_act_sets_tripadi_zone_and_pushes_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    assert s0.tripadi_zone is False
    s1 = apply_rule("8.2.1", s0)
    assert s1.tripadi_zone is True
    assert any(e.get("id") == "8.2.1" for e in s1.adhikara_stack)
    s2 = apply_rule("8.2.1", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("8.2.1") == 1

