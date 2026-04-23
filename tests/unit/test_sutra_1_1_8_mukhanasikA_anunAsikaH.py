"""
1.1.8 मुखनासिकावचनोऽनुनासिकः — *anunāsika* definiens; M / ``anunasika`` tag.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term, Varna
from phonology         import mk
from sutras.adhyaya_1.pada_1 import sutra_1_1_8 as s118


def test_sutra_metadata():
    r = SUTRA_REGISTRY["1.1.8"]
    assert r.sutra_id == "1.1.8"
    assert r.sutra_type is SutraType.SAMJNA
    assert "anun" in r.text_slp1.lower() or "muk" in r.text_slp1.lower()


def test_is_anusvara_slp1():
    assert s118.is_anusvara_slp1("M")
    assert not s118.is_anusvara_slp1("m")


def test_is_varna_tagged_anunAsika():
    v0 = Varna(slp1="i", dev="इ", tags=set())
    v1 = Varna(slp1="i", dev="इ", tags={"anunasika"})
    assert not s118.is_varna_tagged_anunAsika(v0)
    assert s118.is_varna_tagged_anunAsika(v1)


def test_samjna_bootstrap_idempotent():
    t = Term(kind="prakriti", varnas=[mk("a")])
    s0 = State(terms=[t])
    s1 = apply_rule("1.1.8", s0)
    assert s1.samjna_registry.get("anunAsika") == s118.ANUNASIKA_REGISTER_VALUE
    s2 = apply_rule("1.1.8", s1)
    assert s2.samjna_registry.get("anunAsika") == s1.samjna_registry.get("anunAsika")


def test_helper_registered():
    s = State(terms=[], samjna_registry={"anunAsika": s118.ANUNASIKA_REGISTER_VALUE})
    assert s118.anunAsika_samjna_is_registered(s)
