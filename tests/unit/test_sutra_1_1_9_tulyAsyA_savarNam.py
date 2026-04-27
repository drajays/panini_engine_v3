"""
1.1.9 तुल्यास्यप्रयत्नं सवर्णम् — *savarṇa* saṃjñā; delegates to ``phonology.savarna``.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_9 as s119


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.9"]
    assert r.sutra_id == "1.1.9"
    assert r.sutra_type is SutraType.SAMJNA
    assert "savar" in r.text_slp1.lower() or "tuly" in r.text_slp1.lower()


def test_is_savarna_slp1_delegates():
    assert s119.is_savarna_slp1("a", "A")
    assert s119.is_savarna_slp1("i", "I")
    assert not s119.is_savarna_slp1("a", "i")


def test_is_savarna_slp1_nAjjhalou_ac_hal():
    assert not s119.is_savarna_slp1("a", "h")
    assert not s119.is_savarna_slp1("i", "S")


def test_dirgha_savarna_of_ak():
    assert s119.dirgha_savarna_of_ak("a") == "A"
    assert s119.dirgha_savarna_of_ak("i") == "I"


def test_samjna_bootstrap_idempotent():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("1.1.9", s0)
    assert s1.samjna_registry.get("savarNa") == s119.SAVARNA_REGISTER_VALUE
    s2 = apply_rule("1.1.9", s1)
    assert s2.samjna_registry.get("savarNa") == s1.samjna_registry.get("savarNa")


def test_savarNa_samjna_is_registered():
    s = State(terms=[], samjna_registry={"savarNa": s119.SAVARNA_REGISTER_VALUE})
    assert s119.savarNa_samjna_is_registered(s)
