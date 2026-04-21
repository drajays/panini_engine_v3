"""
phonology/pratyahara.py — Pratyāhāras derived from the Śiva-sūtras.
────────────────────────────────────────────────────────────────────

We do NOT hard-code the big pratyāhāras (AC, HAL, etc.) as magic sets.
They are DERIVED by applying Pāṇini's own rule ādir antyena sahetā
(1.1.71) to the Māheśvara-sūtra sequence loaded in phonology/maheshvara.py.

Constants exposed:
    AC    : all vowels (a .. O)
    HAL   : all consonants (h .. l)
    IK    : i u f x    (short ik)
    EC    : e E o O
    YAN   : y v r l
    JHAL  : all non-nasal stops + sibilants (ja to h excluded properly)
    KHAR  : voiceless stops + sibilants
    TUSMA : t T d D n s                   — 1.3.4 na vibhaktau tusmāḥ
    CUTU  : c-group + ṭ-group             — 1.3.7 cuṭū
    KU_VARGA : k K g G N                  — 1.3.8 backdrop
    NI_TU_DU : Y w q                      — 1.3.5 trigger set

Each is a frozenset of short-vowel/consonant SLP1 letters.  For ik-savarṇa
dīrgha lookups the corresponding long forms are computed in savarna.py.
"""
from __future__ import annotations

from typing import FrozenSet, Iterable, List

from phonology.maheshvara import MAHESHVARA_SUTRAS, ordered_phoneme_sequence


def build_pratyahara(start: str, end_it: str) -> FrozenSet[str]:
    """
    Build a pratyāhāra whose first letter is `start` and whose
    group-closer (anubandha) is `end_it`.

    `start` must be located as a PHONEME (not as an it-marker).
    `end_it` must be located as an IT-MARKER (the anubandha that closes
    a Māheśvara-sūtra), not as a phoneme that happens to share its shape.

    E.g. build_pratyahara('a', 'c') = {a, i, u, f, x, e, o, E, O}  (AC)
         build_pratyahara('h', 'l') = all consonants (HAL) — correctly
           skipping the 'l' that appears as a PHONEME in MS6 and
           stopping at the 'l' it-marker that closes MS14.
    """
    # Build a structured sequence: list of (letter, is_it_marker, ms_index).
    structured = []
    for ms in MAHESHVARA_SUTRAS:
        for ph in ms["phonemes"]:
            structured.append((ph, False, ms["index"]))
        structured.append((ms["it"], True, ms["index"]))

    # Locate `start` — first occurrence as a PHONEME.
    i = None
    for k, (ch, is_it, _) in enumerate(structured):
        if ch == start and not is_it:
            i = k
            break
    if i is None:
        raise ValueError(f"start {start!r} not found as phoneme in Māheśvara-sūtras")

    # Locate `end_it` — first occurrence AFTER i as an IT-MARKER.
    j = None
    for k in range(i + 1, len(structured)):
        ch, is_it, _ = structured[k]
        if ch == end_it and is_it:
            j = k
            break
    if j is None:
        raise ValueError(f"end_it {end_it!r} not found as it-marker after {start!r}")

    # Collect everything strictly between i and j that is itself a phoneme
    # (skip intervening it-markers of earlier Māheśvara-sūtras).
    out = [structured[k][0] for k in range(i, j) if not structured[k][1]]
    return frozenset(out)


# Core vowel/consonant sets derived from the Māheśvara-sūtras.
AC    = build_pratyahara("a", "c")
HAL   = build_pratyahara("h", "l")
IK    = build_pratyahara("i", "k")
EC    = build_pratyahara("e", "c")
YAN   = build_pratyahara("y", "R")   # antaḥsthā y v r l
JHAL  = build_pratyahara("J", "l")
KHAR  = build_pratyahara("K", "r")
# AK, IN, AN, ENG could be added here as needed — pattern identical.


# ──────────────────────────────────────────────────────────────
# Ganana-based auxiliary sets used by 1.3.4 / 1.3.5 / 1.3.7 / 1.3.8
# These are LITERAL enumerations because Pāṇini's śloka spells them
# out letter-by-letter; they are NOT further-derivable pratyāhāras.
# ──────────────────────────────────────────────────────────────

TUSMA     = frozenset({"t", "T", "d", "D", "n", "s"})
CUTU      = frozenset({"c", "C", "j", "J", "Y", "S", "w", "W", "q", "Q", "R"})
KU_VARGA  = frozenset({"k", "K", "g", "G", "N"})
NI_TU_DU  = frozenset({"Y", "w", "q"})


# ──────────────────────────────────────────────────────────────
# Hrasva / dīrgha classification (pure phonemic; no grammar)
# ──────────────────────────────────────────────────────────────

_HRASVA = frozenset({"a", "i", "u", "f", "x"})
_DIRGHA = frozenset({"A", "I", "U", "F", "X", "e", "E", "o", "O"})


def is_hrasva(slp1: str) -> bool:
    return slp1 in _HRASVA


def is_dirgha(slp1: str) -> bool:
    return slp1 in _DIRGHA


def count_vowel_letters(slp1_flat: str) -> int:
    """Count SLP1 vowel letters (hrasva + dīrgha) in a flat string."""
    return sum(1 for ch in slp1_flat if is_hrasva(ch) or is_dirgha(ch))


def is_ekac_upadesha(slp1_flat: str) -> bool:
    """True iff exactly one vowel letter — used with 7.2.10 / एकाच् धातु."""
    return count_vowel_letters(slp1_flat) == 1
