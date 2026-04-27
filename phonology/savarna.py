"""
phonology/savarna.py — 1.1.9 tulyāsyaprayatnaṁ savarṇam.
─────────────────────────────────────────────────────────

Śāstrīyā registry anchor: ``sutras/adhyaya_1/pada_1/sutra_1_1_9.py`` (``SutraType.SAMJNA``).

Savarṇa (homorganic) classification.  Two phonemes are savarṇa if
they share place of articulation (sthāna) and internal effort
(ābhyantara-prayatna).

We encode savarṇa groups as the Pāṇinian convention requires.
**1.1.10** *nājjhalau* is enforced here: no *ac*–*hal* pair is *savarṇa*, regardless
of shared *sthāna* / *prayatna* (see user note *दण्डहस्त.md*).

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

from phonology.varna import AC_DEV, HAL_DEV

# 1.1.10 *nājjhalau* (prayoga reading): *ac* and *hal* are never *savarṇa* to
# each other, blocking over-broad *tulyāsya-prayatna* identifications at vowel–
# consonant boundaries (e.g. *daṇḍa*+*hasta*, *dadhi*+*śītalam*).
_AC_LETTERS: frozenset[str] = frozenset(AC_DEV.keys())
_HAL_LETTERS: frozenset[str] = frozenset(HAL_DEV.keys())

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
    Returns True iff slp1 letters a and b are savarṇa per 1.1.9,
    subject to **1.1.10** *nājjhalau*: no *ac*–*hal* pair is *savarṇa*.
    """
    a_ac = a in _AC_LETTERS
    b_ac = b in _AC_LETTERS
    a_hal = a in _HAL_LETTERS
    b_hal = b in _HAL_LETTERS
    if (a_ac and b_hal) or (b_ac and a_hal):
        return False
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
