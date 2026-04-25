"""
4.2.114 *vṛddhāc chaḥ* — *śaiṣika* *Cha* licence (registry), under **4.2.92**.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state import State, Term
from phonology import mk
from phonology.varna import mk_inherent_a

from sutras.adhyaya_4.pada_2.sutra_4_2_114 import (
    META_ELIGIBLE_INDICES,
    SAMJNA_KEY,
    proposed_cha_eligible_indices,
)


def _rAma_stem() -> Term:
    return Term(
        kind="prakriti",
        varnas=[mk("r"), mk("A"), mk("m"), mk_inherent_a()],
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": "rAma"},
    )


def test_registry():
    r = SUTRA_REGISTRY["4.2.114"]
    assert r.sutra_type is SutraType.SAMJNA
    assert "4.2.92" in r.anuvritti_from
    assert "vfdDAt" in r.text_slp1
    assert "छः" in r.padaccheda_dev


def test_skips_without_sheSa_adhikAra():
    s0 = State(terms=[_rAma_stem()], meta={META_ELIGIBLE_INDICES: (0,)})
    s0 = apply_rule("1.1.1", s0)
    s0 = apply_rule("1.1.73", s0)
    s1 = apply_rule("4.2.114", s0)
    assert SAMJNA_KEY not in s1.samjna_registry


def test_skips_when_not_vrddham_even_if_meta_requests():
    t = Term(
        kind="prakriti",
        varnas=[mk("g"), mk("a"), mk("j"), mk_inherent_a()],
        tags={"prātipadika"},
        meta={"upadesha_slp1": "gaja"},
    )
    s0 = State(terms=[t], meta={META_ELIGIBLE_INDICES: (0,)})
    s0 = apply_rule("1.1.1", s0)
    s0 = apply_rule("1.1.73", s0)
    s0 = apply_rule("4.2.92", s0)
    s1 = apply_rule("4.2.114", s0)
    assert proposed_cha_eligible_indices(s1) == frozenset()
    assert SAMJNA_KEY not in s1.samjna_registry


def test_applies_for_vrddham_under_4_2_92():
    s0 = State(terms=[_rAma_stem()], meta={META_ELIGIBLE_INDICES: (0,)})
    s0 = apply_rule("1.1.1", s0)
    s0 = apply_rule("1.1.73", s0)
    s0 = apply_rule("4.2.92", s0)
    s1 = apply_rule("4.2.114", s0)
    assert s1.samjna_registry[SAMJNA_KEY] == frozenset({0})


def test_second_apply_idempotent():
    s0 = State(terms=[_rAma_stem()], meta={META_ELIGIBLE_INDICES: (0,)})
    s0 = apply_rule("1.1.1", s0)
    s0 = apply_rule("1.1.73", s0)
    s0 = apply_rule("4.2.92", s0)
    s1 = apply_rule("4.2.114", s0)
    s2 = apply_rule("4.2.114", s1)
    assert s1.samjna_registry[SAMJNA_KEY] == frozenset({0})
    assert s2.samjna_registry[SAMJNA_KEY] == frozenset({0})
