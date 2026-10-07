"""Lexicon architecture: data/inputs/subanta_krt_origin_lexicon.json replaces
the ad-hoc ugit/tfc/han_dhatu caller flags (and bench/ashtadhyayi_gold.py's
suffix-spelling guess) with a declared origin fact, for the stems it covers.
See docs/LEXICON_ARCHITECTURE.md.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.registries.subanta_origin_lookup import is_known_stem, origin_flags
from pipelines.subanta import derive


def test_lexicon_known_stems() -> None:
    assert is_known_stem("Bavat")
    assert origin_flags("Bavat") == {"ugit": True}
    assert origin_flags("pitf") == {"tfc": False}
    assert not is_known_stem("someRandomStemNotInTheLexicon")


def test_derive_consults_lexicon_without_the_caller_passing_a_flag() -> None:
    """Bavat used to need ugit=True passed in by the caller; now the lexicon supplies it."""
    with_flag = derive("Bavat", 1, 1, linga="pulliṅga", ugit=True).flat_dev()
    without_flag = derive("Bavat", 1, 1, linga="pulliṅga").flat_dev()
    assert without_flag == with_flag == "भवान्"


def test_declared_false_is_not_overridable_by_a_stray_caller_flag() -> None:
    """pitf is declared tfc=False (kinship noun, 7.1.94) — a caller passing tfc=True
    by mistake (e.g. copy-pasted from a real tṛc stem) must not relitigate that."""
    s = derive("pitf", 2, 1, linga="pulliṅga", tfc=True)
    assert "krt_tfc" not in s.terms[0].tags


def test_kartf_tfc_from_lexicon() -> None:
    s = derive("kartf", 2, 1, linga="pulliṅga")
    assert "krt_tfc" in s.terms[0].tags


def test_gold_harness_origin_flags_prefers_lexicon() -> None:
    from bench.ashtadhyayi_gold import _origin_flags
    assert _origin_flags("Bavat") == {"ugit": True}
    assert _origin_flags("pitf") == {"tfc": False}
    # a stem not in the lexicon still falls back to the suffix guess
    assert _origin_flags("kftimat") == {"ugit": True, "tfc": False}
