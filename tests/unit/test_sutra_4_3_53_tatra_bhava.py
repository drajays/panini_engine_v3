"""
4.3.53 *tatra bhavaḥ* — *saptamī* + *bhava* ‘stays there’ (*taddhita* licence).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state import State, Term
from phonology import mk

from sutras.adhyaya_4.pada_3.sutra_4_3_53 import (
    META_ELIGIBLE,
    META_JATI_BLOCK,
    SAMJNA_KEY,
)


def _state(**meta) -> State:
    t = Term(kind="prakriti", varnas=[mk("s"), mk("r"), mk("u")], tags=set(), meta={})
    return State(terms=[t], meta=dict(meta))


def test_registry():
    r = SUTRA_REGISTRY["4.3.53"]
    assert r.sutra_type is SutraType.SAMJNA
    assert "4.1.83" in r.anuvritti_from
    assert "4.1.82" in r.anuvritti_from
    assert "तत्र" in r.padaccheda_dev
    assert "भवः" in r.padaccheda_dev


def test_skips_without_prAg_dIvyataH_adhikAra():
    s0 = _state(**{META_ELIGIBLE: True})
    s1 = apply_rule("4.3.53", s0)
    assert SAMJNA_KEY not in s1.samjna_registry


def test_skips_without_eligible_meta():
    s0 = _state()
    s0 = apply_rule("4.1.83", s0)
    s1 = apply_rule("4.3.53", s0)
    assert SAMJNA_KEY not in s1.samjna_registry


def test_skips_when_jAti_block_meta_set():
    s0 = _state(**{META_ELIGIBLE: True, META_JATI_BLOCK: True})
    s0 = apply_rule("4.1.83", s0)
    s1 = apply_rule("4.3.53", s0)
    assert SAMJNA_KEY not in s1.samjna_registry


def test_applies_under_4_1_83_with_eligible():
    s0 = _state(**{META_ELIGIBLE: True})
    s0 = apply_rule("4.1.83", s0)
    s1 = apply_rule("4.3.53", s0)
    assert s1.samjna_registry.get(SAMJNA_KEY) is True


def test_second_apply_idempotent():
    s0 = _state(**{META_ELIGIBLE: True})
    s0 = apply_rule("4.1.83", s0)
    s1 = apply_rule("4.3.53", s0)
    s2 = apply_rule("4.3.53", s1)
    assert s1.samjna_registry.get(SAMJNA_KEY) is True
    assert s2.samjna_registry.get(SAMJNA_KEY) is True
