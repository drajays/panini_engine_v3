"""Metadata on 1.1.1 vṛddhi saṃjñā (scholarly list)."""
from __future__ import annotations

from sutras.adhyaya_1.pada_1 import sutra_1_1_1 as s111


def test_vriddhi_phoneme_set():
    assert s111.VRIDHI_PHONEMES_SLP1 == frozenset({"A", "E", "O"})


def test_nine_referencing_sutras_listed():
    assert len(s111.VRIDHI_SAMJNA_REFERENCING_SUTRAS) == 9
    ids = [t[0] for t in s111.VRIDHI_SAMJNA_REFERENCING_SUTRAS]
    assert "6.1.88" in ids
    assert "1.1.3" in ids
