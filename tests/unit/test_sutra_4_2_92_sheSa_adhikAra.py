"""
4.2.92 *śeṣe* — *śeṣādhikāraḥ* (scope through **4.3.134**).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state import State, Term
from phonology import mk


def test_registry():
    r = SUTRA_REGISTRY["4.2.92"]
    assert r.sutra_type is SutraType.ADHIKARA
    assert r.adhikara_scope == ("4.2.92", "4.3.134")
    assert "Seze" in r.text_slp1
    assert "शेषे" in r.text_dev
    assert "4.1.83" in r.anuvritti_from


def test_push_once():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("4.2.92", s0)
    assert any(e.get("id") == "4.2.92" for e in s1.adhikara_stack)
    s2 = apply_rule("4.2.92", s1)
    assert [e.get("id") for e in s2.adhikara_stack].count("4.2.92") == 1
