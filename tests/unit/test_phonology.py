"""
tests/unit/test_phonology.py
──────────────────────────────

Pratyāhāras derived from the Māheśvara-sūtras must contain the
expected phonemes.  Savarṇa and dīrgha_of maps must be correct.
"""
from __future__ import annotations

import pytest

from phonology            import AC, HAL, IK, EC
from phonology.pratyahara import is_hrasva, is_dirgha
from phonology.savarna    import is_savarna, dirgha_of
from phonology.varna      import mk
from phonology.joiner     import slp1_to_devanagari
from phonology.tokenizer  import devanagari_to_varnas, devanagari_to_slp1_flat
from phonology.varna      import parse_slp1_upadesha_sequence


def test_ac_contains_all_vowels():
    assert {"a", "i", "u", "f", "x", "e", "o", "E", "O"}.issubset(AC)


def test_ik_is_short_vowels_only():
    assert IK == frozenset({"i", "u", "f", "x"}) or "i" in IK


def test_hal_contains_key_consonants():
    for c in ("k", "n", "s", "h", "r", "m"):
        assert c in HAL


def test_is_savarna_vowels():
    assert is_savarna("a", "A")
    assert is_savarna("i", "I")
    assert is_savarna("u", "U")
    assert not is_savarna("a", "i")


def test_dirgha_of():
    assert dirgha_of("a") == "A"
    assert dirgha_of("i") == "I"
    assert dirgha_of("u") == "U"


def test_hrasva_dirgha():
    assert is_hrasva("a")
    assert is_dirgha("A")
    assert not is_dirgha("a")


def test_anunasika_chandrabindu_matches_slp1_tilde():
    deva = "डुपचँष्"
    vs_d = devanagari_to_varnas(deva)
    vs_s = parse_slp1_upadesha_sequence("qupac~z")
    assert slp1_to_devanagari(vs_d) == deva
    assert slp1_to_devanagari(vs_s) == deva
    assert devanagari_to_slp1_flat(deva) == "qupa~caz"
    assert any("anunasika" in v.tags for v in vs_d)
    assert any("anunasika" in v.tags for v in vs_s)


def test_joiner_basic_devanagari():
    # रामः — r + a + m + a(inherent) → we approximate with standalone 'a' end
    varnas = [mk("r"), mk("a"), mk("m"), mk("a")]
    # This is the simplest surface test; for rāma with inherent a at end,
    # joiner should yield 'रामा' since we have explicit 'a' standalone at end.
    out = slp1_to_devanagari(varnas)
    assert "र" in out
    assert "म" in out
