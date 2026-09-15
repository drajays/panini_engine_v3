"""Gold tests for pac (bhvādi, a-upadha) liṭ kartari parasmaipada — 9-cell.

pac = [p, a, c] — consonant-final, 'a' at upadha.
Strong arm (Nal): 7.2.116 vṛddhi a→ā → pāc → abhyāsa 'pa' + root 'pāc' + a = papāca.
Weak arm no-iṭ: no guṇa/vṛddhi, pac + vowel suffix → papacatuH/papacuH/papaca.
Weak arm iṭ: pac + i + suffix → papaciTa/papaciva/papacima.
"""
from __future__ import annotations

import pytest
import sutras  # noqa: F401
from pipelines.tinanta import derive

_PAC_LIT_KARTARI_PARASMAI = {
    (3, 1): "papAca",     # Nal strong: vṛddhi a→ā
    (3, 2): "papacatuH",  # atuH weak
    (3, 3): "papacuH",    # uH weak
    (2, 1): "papaciTa",   # iṭ+TaL: pac+i+tha
    (2, 2): "papacaTuH",  # aTuH weak
    (2, 3): "papaca",     # a weak
    (1, 1): "papAca",     # Nal strong (same as 3sg)
    (1, 2): "papaciva",   # iṭ+va
    (1, 3): "papacima",   # iṭ+ma
}


@pytest.mark.parametrize("purusha,vacana,expected", [
    (p, v, exp) for (p, v), exp in _PAC_LIT_KARTARI_PARASMAI.items()
])
def test_pac_lit_kartari_surface(purusha: int, vacana: int, expected: str) -> None:
    s = derive("pac", "liT", "kartari", purusha, vacana, pada="parasmai")
    assert s.flat_slp1() == expected
