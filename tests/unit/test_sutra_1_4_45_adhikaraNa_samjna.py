"""
1.4.45 *kārake ādhāraḥ adhikaraṇam* — *adhikaraṇa* *kāraka* *saṃjñā*.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state import State, Term
from phonology import mk

from sutras.adhyaya_1.pada_4.sutra_1_4_45 import (
    META_LOCUS_INDICES,
    SAMJNA_KEY,
)


def _term() -> Term:
    return Term(
        kind="prakriti",
        varnas=[mk("k"), mk("a"), mk("w")],
        tags={"prātipadika"},
        meta={},
    )


def test_registry_samjna():
    r = SUTRA_REGISTRY["1.4.45"]
    assert r.sutra_type is SutraType.SAMJNA
    assert "1.4.23" in r.anuvritti_from
    assert "1.4.1" in r.anuvritti_from


def test_skips_without_kArake_adhikAra():
    s0 = State(terms=[_term(), _term()], meta={META_LOCUS_INDICES: (0,)})
    s1 = apply_rule("1.4.45", s0)
    assert SAMJNA_KEY not in s1.samjna_registry


def test_skips_without_meta_indices():
    s0 = State(terms=[_term(), _term()], meta={})
    s0 = apply_rule("1.4.23", s0)
    s1 = apply_rule("1.4.45", s0)
    assert SAMJNA_KEY not in s1.samjna_registry


def test_applies_under_1_4_23_with_meta():
    s0 = State(terms=[_term(), _term()], meta={META_LOCUS_INDICES: (1,)})
    s0 = apply_rule("1.4.23", s0)
    s1 = apply_rule("1.4.45", s0)
    assert s1.samjna_registry[SAMJNA_KEY] == frozenset({1})


def test_second_apply_idempotent():
    s0 = State(terms=[_term(), _term()], meta={META_LOCUS_INDICES: (0,)})
    s0 = apply_rule("1.4.23", s0)
    s1 = apply_rule("1.4.45", s0)
    s2 = apply_rule("1.4.45", s1)
    assert s1.samjna_registry[SAMJNA_KEY] == frozenset({0})
    assert s2.samjna_registry[SAMJNA_KEY] == frozenset({0})


def test_invalid_index_skips():
    s0 = State(terms=[_term()], meta={META_LOCUS_INDICES: (3,)})
    s0 = apply_rule("1.4.23", s0)
    s1 = apply_rule("1.4.45", s0)
    assert SAMJNA_KEY not in s1.samjna_registry
