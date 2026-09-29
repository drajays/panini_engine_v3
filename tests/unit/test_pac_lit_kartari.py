"""Gold tests for pac (bhvādi, a-upadha) liṭ kartari parasmaipada — 9-cell.

pac = [p, a, c] — consonant-final, 'a' at upadha.
Strong arm (Nal): 7.2.116 vṛddhi a→ā → pāc → abhyāsa 'pa' + root 'pāc' + a = papāca.
Weak arm no-iṭ: no guṇa/vṛddhi, pac + vowel suffix → pecatuH/pecuH/peca (6.4.120).
Weak arm iṭ: pac + i + suffix → peciTa/peciva/pecima (6.4.121, 6.4.120).
"""
from __future__ import annotations

import pytest
import sutras  # noqa: F401
from pipelines.tinanta import derive

_PAC_LIT_KARTARI_PARASMAI = {
    (3, 1): "papAca",     # Nal strong: vṛddhi a→ā
    (3, 2): "pecatuH",    # 6.4.120 ata ekahalmadhye… (gold पेचतुः)
    (3, 3): "pecuH",      # 6.4.120
    (2, 1): "peciTa",     # 6.4.121 thali ca seṭi
    (2, 2): "pecaTuH",    # 6.4.120
    (2, 3): "peca",       # 6.4.120
    (1, 1): "papAca",     # Nal strong (same as 3sg)
    (1, 2): "peciva",     # 6.4.120
    (1, 3): "pecima",     # 6.4.120
}


@pytest.mark.parametrize("purusha,vacana,expected", [
    (p, v, exp) for (p, v), exp in _PAC_LIT_KARTARI_PARASMAI.items()
])
def test_pac_lit_kartari_surface(purusha: int, vacana: int, expected: str) -> None:
    s = derive("pac", "liT", "kartari", purusha, vacana, pada="parasmai")
    assert s.flat_slp1() == expected
