"""
1.1.61 *pratyayasyādarśanaṃ luk–ślu–lupaḥ* — *luk* / *ślu* / *lup* saṃjñā.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state import State, Term
from phonology import mk

from sutras.adhyaya_1.pada_1.luk_slu_lup_samjna_1_1_61 import (
    LUK_SLU_LUP_REGISTER_VALUE,
    LUK_SLU_LUP_SAMJNA_KEY,
    luk_slu_lup_samjna_is_registered,
)
from pipelines.subanta import derive


def test_registry():
    r = SUTRA_REGISTRY["1.1.61"]
    assert r.sutra_type is SutraType.SAMJNA
    assert "1.1.60" in r.anuvritti_from
    assert "luk" in r.text_slp1


def test_requires_1_1_60_first():
    t = Term(kind="prakriti", varnas=[mk("a")], tags=set(), meta={})
    s0 = State(terms=[t], meta={})
    s1 = apply_rule("1.1.61", s0)
    assert not luk_slu_lup_samjna_is_registered(s1)


def test_registers_after_1_1_60():
    t = Term(kind="prakriti", varnas=[mk("a")], tags=set(), meta={})
    s0 = State(terms=[t], meta={})
    s1 = apply_rule("1.1.60", s0)
    s2 = apply_rule("1.1.61", s1)
    assert s2.samjna_registry[LUK_SLU_LUP_SAMJNA_KEY] == LUK_SLU_LUP_REGISTER_VALUE


def test_idempotent_second_apply():
    t = Term(kind="prakriti", varnas=[mk("a")], tags=set(), meta={})
    s0 = State(terms=[t], meta={})
    s1 = apply_rule("1.1.60", s0)
    s2 = apply_rule("1.1.61", s1)
    s3 = apply_rule("1.1.61", s2)
    assert s2.samjna_registry[LUK_SLU_LUP_SAMJNA_KEY] == LUK_SLU_LUP_REGISTER_VALUE
    assert s3.samjna_registry[LUK_SLU_LUP_SAMJNA_KEY] == LUK_SLU_LUP_REGISTER_VALUE


def test_subanta_preflight_has_luk_slu_lup():
    s = derive("gaja", 1, 1)
    assert luk_slu_lup_samjna_is_registered(s)
