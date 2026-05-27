"""
phonology/pratyaya_pratyahara.py — Pratyaya pratyāhāras via 1.1.71.

By ādir antyena sahetā (1.1.71), a pratyāhāra is formed by taking the
FIRST member of an ordered sūtra-list together with the IT-MARKER of the
LAST member; all entries from first to last are covered.

This module applies the same principle to ordered PRATYAYA lists:

  build_pratyaya_pratyahara(first_upadesha, last_it, ordered_seq)

Returns a frozenset of the upadesha_slp1 strings for all covered pratyayas.

Named pratyāhāras defined here:
  SUP   — all sup case-endings (4.1.2); s~ to p of "sup"
  SUT   — sarvanamasthāna subset (su…auṭ); s~ to T of "Ow"
  TAP   — ṭāp/ḍāp/cāp strī-pratyayas (4.1.4); explicit enumeration
  TIN   — 18 tiṅ ādeśas (3.4.78); "tip" to G of "mahiG"
  TAN   — ātmanepada subset; "ta" to G of "mahiG"
  TRN   — tṛn/tṛc/kvip kṛt group (3.2.124–135)
  SAN   — san/saṅ desiderative pratyaya group (3.1.5+)
"""
from __future__ import annotations

from typing import FrozenSet, List, Tuple


def build_pratyaya_pratyahara(
    first_upadesha: str,
    last_it: str,
    ordered_seq: List[Tuple[str, str]],
    *,
    last_occurrence: bool = False,
) -> FrozenSet[str]:
    """
    Build a pratyaya pratyāhāra by the first-member + last-it principle (1.1.71).

    ordered_seq — list of (upadesha_slp1, anubandha) tuples in sūtra order.
      anubandha is the it-marker that 1.3.3 etc. would lope (empty string if none).
    last_occurrence — if True, use the LAST entry with last_it as anubandha
      (needed for groups where all members share the same it, e.g. TAP where
      all three have 'p'; the pratyāhāra should span the whole group).
    Returns a frozenset of upadesha_slp1 values for all covered pratyayas.
    """
    start_idx = None
    for i, (upa, _) in enumerate(ordered_seq):
        if upa == first_upadesha:
            start_idx = i
            break
    if start_idx is None:
        raise ValueError(f"first_upadesha {first_upadesha!r} not in ordered_seq")

    if last_occurrence:
        # Scan from end backward to find last occurrence
        end_idx = None
        for i in range(len(ordered_seq) - 1, start_idx - 1, -1):
            _, anubandha = ordered_seq[i]
            if anubandha == last_it:
                end_idx = i
                break
    else:
        end_idx = None
        for i in range(start_idx, len(ordered_seq)):
            _, anubandha = ordered_seq[i]
            if anubandha == last_it:
                end_idx = i
                break
    if end_idx is None:
        raise ValueError(
            f"last_it {last_it!r} not found as anubandha on or after index {start_idx}"
        )

    return frozenset(upa for upa, _ in ordered_seq[start_idx : end_idx + 1])


# ── 4.1.2 sup ordered sequence ────────────────────────────────────────────
# Each entry: (upadesha_slp1, anubandha).
# anubandha = it-marker that 1.3.3/1.3.4 would identify and 1.3.9 lopos.
# Empty string = no halant it (the entry has only nasal/vowel markers or none).
_SUP_ORDERED: List[Tuple[str, str]] = [
    ("s~",   ""),    # 1-1 / 8-1 : su (nasal it ~ is removed; anubandha here is anunāsika handled by 1.3.2)
    ("O",    ""),    # 1-2 / 8-2 : au
    ("jas",  ""),    # 1-3 / 8-3 : jas
    ("am",   ""),    # 2-1       : am
    ("Ow",   "w"),   # 2-2       : auṭ  — ṭ (SLP1 w) is the it by 1.3.3
    ("Sas",  ""),    # 2-3       : śas
    ("wA",   "w"),   # 3-1       : ṭā   — ṭ (initial w) is the it by 1.3.6 (ṣaṣṭhī... no; by N-it 1.3.5: w is in NI_TU_DU)
    ("ByAm", ""),    # 3-2/4-2/5-2 : bhyām
    ("Bis",  ""),    # 3-3       : bhis
    ("Ne",   ""),    # 4-1       : ṅe    — N is the initial nasal it by 1.3.5
    ("Byas", ""),    # 4-3/5-3   : bhyas
    ("Nasi", ""),    # 5-1       : ṅasi  — N is the initial nasal it
    ("Nas",  ""),    # 6-1       : ṅas   — N is the initial nasal it
    ("os",   ""),    # 6-2/7-2   : os
    ("Am",   ""),    # 6-3       : ām
    ("Ni",   ""),    # 7-1       : ṅi    — N initial nasal it
    ("sup",  "p"),   # 7-3       : sup   — p is the it by 1.3.3 (not in tusmā)
]

# SUP: all sup pratyayas — s~ (su) to p of "sup"
SUP: FrozenSet[str] = build_pratyaya_pratyahara("s~", "p", _SUP_ORDERED)

# SUT: sarvanamasthāna subset — s~ (su) to ṭ of "auṭ" (Ow)
SUT: FrozenSet[str] = build_pratyaya_pratyahara("s~", "w", _SUP_ORDERED)


# ── 4.1.4 + related ṭāp group ──────────────────────────────────────────────
# ṭāp (TAp), ḍāp (qAp), cāp (cAp) — explicit enumeration (three members).
# All have 'p' as the it; their phonemic body is ṭā / ḍā / cā.
# The TAP pratyāhāra = ṭā (from TAp, the first member) + p (the it).
_TAP_ORDERED: List[Tuple[str, str]] = [
    ("TAp", "p"),   # ṭāp
    ("qAp", "p"),   # ḍāp
    ("cAp", "p"),   # cāp
]

TAP: FrozenSet[str] = build_pratyaya_pratyahara("TAp", "p", _TAP_ORDERED, last_occurrence=True)


# ── 3.4.78 tiṅ ordered sequence ──────────────────────────────────────────
# 18 classical tiṅ ādeśas only (not the composite āśīr-liṅ / karmani forms).
# anubandha column: 'p' = final p it (tip, sip, mip), 'm' = mas, 's'= tas etc.
# Most tiṅ have no final halant-it in their ādeśa upadesha; the it-lopa has
# already been tracked by 3.4.78/1.3.3 at attachment time.
# For the pratyāhāra: TIN = "ti" (from tip) + G (from mahiG).
_TIN_ORDERED: List[Tuple[str, str]] = [
    ("tip",   "p"),   # 1.3: parasmaipada 3sg
    ("tas",   ""),    # 1.3: 3du
    ("jhi",   ""),    # 1.3: 3pl  (jh- marker → 3.4.108 etc.)
    ("sip",   "p"),   # 2.3: 2sg
    ("Tas",   ""),    # 2.3: 2du
    ("Ta",    ""),    # 2.3: 2pl
    ("mip",   "p"),   # 1.3: 1sg
    ("vas",   ""),    # 1.3: 1du
    ("mas",   ""),    # 1.3: 1pl
    ("ta",    ""),    # 3.3: ātmanepada 3sg
    ("AtAm",  ""),    # 3.3: 3du
    ("Ja",    ""),    # 3.3: 3pl  (jh- initial)
    ("TAs",   ""),    # 2.3: 2sg  ātp
    ("ATAm",  ""),    # 2.3: 2du
    ("Dvam",  ""),    # 2.3: 2pl
    ("iw",    "w"),   # 1.3: 1sg  ātp  (iṭ → ṭ is it by 1.3.3)
    ("vahi",  ""),    # 1.3: 1du  ātp
    ("mahiG", "G"),   # 1.3: 1pl  ātp  (mahiṅ → G/ṅ is the it)
]

# TIN: all 18 tiṅ ādeśas — "tip" to G of "mahiG"
TIN: FrozenSet[str] = build_pratyaya_pratyahara("tip", "G", _TIN_ORDERED)

# TAN: ātmanepada subset — "ta" to G of "mahiG"
TAN: FrozenSet[str] = build_pratyaya_pratyahara("ta", "G", _TIN_ORDERED)

# Parasmaipada subset = TIN - TAN (derived, not a named pratyāhāra in Pāṇini)
PARASMAI: FrozenSet[str] = TIN - TAN


# ── 3.2.124–135 tṛn group (kṛdanta) ──────────────────────────────────────
# tṛn, tṛc, kvip and related nominal kṛt suffixes.
# TRN pratyāhāra = "tṛ" (from tṛn) + n (it of tṛn).
# Engine inventory (structural subset used in v3):
_TRN_ORDERED: List[Tuple[str, str]] = [
    ("tfn",  "n"),   # 3.2.124 tṛn (kartṛ suffix)
    ("tfc",  "c"),   # 3.2.125 tṛc (karmakāraka)
    ("kvip", "p"),   # 3.2.76+  kvip (zero suffix, p=it)
    ("kvin", "n"),   # kvin variant
]

TRN: FrozenSet[str] = build_pratyaya_pratyahara("tfn", "n", _TRN_ORDERED)


# ── 3.1.5+ saṅ / san group ────────────────────────────────────────────────
# The san desiderative marker and related affixes.
# SAN = sa (from san) + G (from saṅ = san with ṅ it, or the group-closing ṅ).
_SAN_ORDERED: List[Tuple[str, str]] = [
    ("san",  "n"),   # 3.1.5  san (desiderative)
    ("saG",  "G"),   # saṅ (ṅ = it; closes the pratyāhāra)
]

SAN: FrozenSet[str] = build_pratyaya_pratyahara("san", "G", _SAN_ORDERED)


# ── Utility ───────────────────────────────────────────────────────────────

def is_sup_upadesha(upadesha_slp1: str) -> bool:
    """True iff the upadesha_slp1 is in the SUP pratyāhāra."""
    return upadesha_slp1 in SUP


def is_tin_upadesha(upadesha_slp1: str) -> bool:
    """True iff the upadesha_slp1 is in the TIN pratyāhāra."""
    return upadesha_slp1 in TIN


def is_atmanepada_tin(upadesha_slp1: str) -> bool:
    """True iff the upadesha_slp1 is an ātmanepada tiṅ ādeśa (TAN)."""
    return upadesha_slp1 in TAN


def is_parasmaipada_tin(upadesha_slp1: str) -> bool:
    """True iff the upadesha_slp1 is a parasmaipada tiṅ ādeśa."""
    return upadesha_slp1 in PARASMAI


def is_tap_upadesha(upadesha_slp1: str) -> bool:
    """True iff the upadesha_slp1 is in the TAP strī-pratyaya group."""
    return upadesha_slp1 in TAP


__all__ = [
    "build_pratyaya_pratyahara",
    "SUP", "SUT", "TAP", "TIN", "TAN", "TRN", "SAN", "PARASMAI",
    "is_sup_upadesha", "is_tin_upadesha", "is_atmanepada_tin",
    "is_parasmaipada_tin", "is_tap_upadesha",
]
