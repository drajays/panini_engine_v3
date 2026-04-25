"""
1.1.73 *vṛddhir yasyācām ādis tad vṛddham* — *vṛddha-pada* saṃjñā on *terms*.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state import State, Term
from phonology import mk
from phonology.varna import mk_inherent_a

from pipelines.subanta import derive

from sutras.adhyaya_1.pada_1.sutra_1_1_73 import (
    META_NAMADHEYA_VRDDHA_INDICES,
    VRIDDHAM_INDICES_KEY,
    first_ac_slp1_in_term,
    varttika2_blocks_vrddha_samjna,
    vrddham_term_indices,
)


def _stem_term(varna_list: list) -> Term:
    return Term(
        kind="prakriti",
        varnas=varna_list,
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": "test"},
    )


def test_registry_metadata():
    r = SUTRA_REGISTRY["1.1.73"]
    assert r.sutra_type is SutraType.SAMJNA
    assert "1.1.1" in r.anuvritti_from
    assert "yasya" in r.text_slp1
    assert "वृद्धम्" in r.padaccheda_dev


def test_first_ac_skips_hal_to_find_vowel():
    t = _stem_term([mk("g"), mk("a"), mk("j"), mk_inherent_a()])
    assert first_ac_slp1_in_term(t) == "a"


def test_first_ac_long_a_is_vrddhi_sthan():
    t = _stem_term([mk("r"), mk("A"), mk("m"), mk_inherent_a()])
    assert first_ac_slp1_in_term(t) == "A"


def test_vrddham_indices_empty_for_gaja_shape():
    t = _stem_term([mk("g"), mk("a"), mk("j"), mk_inherent_a()])
    s = State(terms=[t], meta={})
    s = apply_rule("1.1.1", s)
    assert vrddham_term_indices(s) == frozenset()


def test_vrddham_indices_contains_zero_for_rAma_shape():
    t = _stem_term([mk("r"), mk("A"), mk("m"), mk_inherent_a()])
    s = State(terms=[t], meta={})
    s = apply_rule("1.1.1", s)
    assert vrddham_term_indices(s) == frozenset({0})


def test_apply_after_1_1_1_sets_registry():
    t = _stem_term([mk("r"), mk("A"), mk("m"), mk_inherent_a()])
    s0 = State(terms=[t], meta={})
    s1 = apply_rule("1.1.1", s0)
    s2 = apply_rule("1.1.73", s1)
    assert s2.samjna_registry[VRIDDHAM_INDICES_KEY] == frozenset({0})
    assert "vṛddha" in s2.terms[0].tags


def test_second_apply_idempotent():
    t = _stem_term([mk("r"), mk("A"), mk("m"), mk_inherent_a()])
    s0 = State(terms=[t], meta={})
    s1 = apply_rule("1.1.1", s0)
    s2 = apply_rule("1.1.73", s1)
    s3 = apply_rule("1.1.73", s2)
    assert s2.samjna_registry[VRIDDHAM_INDICES_KEY] == frozenset({0})
    assert s3.samjna_registry[VRIDDHAM_INDICES_KEY] == frozenset({0})


def test_subanta_preflight_records_rAma_stem_vrddham():
    s = derive("rAma", 1, 1)
    assert s.samjna_registry.get(VRIDDHAM_INDICES_KEY) == frozenset({0})


def test_subanta_preflight_gaja_not_vrddham():
    s = derive("gaja", 1, 1)
    # 1.1.73 *cond* false when no term qualifies — registry key may be absent.
    assert s.samjna_registry.get(VRIDDHAM_INDICES_KEY, frozenset()) == frozenset()


def test_varttika2_blocks_stems():
    t1 = Term(
        kind="prakriti",
        varnas=[mk("j"), mk("i"), mk("h"), mk("v"), mk("A"), mk("k"), mk("A"), mk("t"), mk("y"), mk("a")],
        tags={"prātipadika"},
        meta={"upadesha_slp1": "jihvAkAtya"},
    )
    assert varttika2_blocks_vrddha_samjna(t1) is True
    t2 = Term(
        kind="prakriti",
        varnas=[mk("h"), mk("a")],
        tags=set(),
        meta={"upadesha_slp1": "haritakAtya"},
    )
    assert varttika2_blocks_vrddha_samjna(t2) is True


def test_nAmadheya_vrddha_without_first_vrddhi_ac():
    # देवदत्त — first *ac* is ``e`` (not Ā/E/O); optional *vṛddha* via *vārttika*.
    t = Term(
        kind="prakriti",
        varnas=[
            mk("d"), mk("e"), mk("v"), mk("a"), mk("d"), mk("a"),
            mk("t"), mk("t"), mk("a"),
        ],
        tags={"prātipadika"},
        meta={"upadesha_slp1": "devadatta"},
    )
    s0 = State(terms=[t], meta={META_NAMADHEYA_VRDDHA_INDICES: (0,)})
    s0 = apply_rule("1.1.1", s0)
    assert vrddham_term_indices(s0) == frozenset({0})


def test_nAmadheya_overridden_by_varttika2():
    t = Term(
        kind="prakriti",
        varnas=[mk("j"), mk("i"), mk("h"), mk("v"), mk("A"), mk("k"), mk("A"), mk("t"), mk("y"), mk("a")],
        tags={"prātipadika"},
        meta={"upadesha_slp1": "jihvAkAtya"},
    )
    s0 = State(terms=[t], meta={META_NAMADHEYA_VRDDHA_INDICES: (0,)})
    s0 = apply_rule("1.1.1", s0)
    assert vrddham_term_indices(s0) == frozenset()


def test_derive_devadatta_with_nAmadheya_kwarg():
    s = derive("devadatta", 1, 1, nAmadheya_vrddha_term_indices=(0,))
    assert s.samjna_registry.get(VRIDDHAM_INDICES_KEY) == frozenset({0})
