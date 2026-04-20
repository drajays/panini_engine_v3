"""
phonology/savarna.py — 1.1.9 tulyāsyaprayatnaṁ savarṇam.
─────────────────────────────────────────────────────────

Savarṇa (homorganic) classification.  Two phonemes are savarṇa if
they share place of articulation (sthāna) and internal effort
(ābhyantara-prayatna).

We encode savarṇa groups as the Pāṇinian convention requires.
Short and long vowels of the same series are savarṇa:
  a, A    : a-series
  i, I    : i-series
  u, U    : u-series
  f, F    : ṛ-series
  x, X    : ḷ-series
(Consonants in the same varga+aspiration/voice group are also savarṇa;
 we expose is_savarna for that purpose.)
"""
from __future__ import annotations

_VOWEL_SERIES = [
    frozenset({"a", "A"}),
    frozenset({"i", "I"}),
    frozenset({"u", "U"}),
    frozenset({"f", "F"}),
    frozenset({"x", "X"}),
    frozenset({"e"}),      # e has no dīrgha pair
    frozenset({"E"}),
    frozenset({"o"}),
    frozenset({"O"}),
]

_CONSONANT_SERIES = [
    # ka-varga
    frozenset({"k", "K", "g", "G", "N"}),
    # ca-varga
    frozenset({"c", "C", "j", "J", "Y"}),
    # ṭa-varga
    frozenset({"w", "W", "q", "Q", "R"}),
    # ta-varga
    frozenset({"t", "T", "d", "D", "n"}),
    # pa-varga
    frozenset({"p", "P", "b", "B", "m"}),
]


def is_savarna(a: str, b: str) -> bool:
    """
    Returns True iff slp1 letters a and b are savarṇa per 1.1.9.
    """
    if a == b:
        return True
    for series in _VOWEL_SERIES + _CONSONANT_SERIES:
        if a in series and b in series:
            return True
    return False


# Map of hrasva → dīrgha used by 6.1.101 akaḥ savarṇe dīrghaḥ.
_DIRGHA_MAP = {
    "a": "A", "A": "A",
    "i": "I", "I": "I",
    "u": "U", "U": "U",
    "f": "F", "F": "F",
    "x": "X", "X": "X",
}


def dirgha_of(slp1: str) -> str:
    """Return the dīrgha ik-savarṇa of an SLP1 ak-letter, or itself."""
    return _DIRGHA_MAP.get(slp1, slp1)
