"""
**3.4.78** — inventory of the eighteen *tiṅ* *ādeśa* replacers of *lakāra* (*lac*).

Not a sūtra file.  Used by ``sutra_3_4_78.py`` and recipes/tests.

*Śāstra (order):* tip, tas, jhi, sip, thas, tha, mip, vas, mas, ta, *ātām*, *jha*, thās,
*āthām*, dhvam, *iṭ*, vahi, mahiṅ.

SLP1 strings follow ``phonology.varna`` / engine conventions (``T``=थ्, ``D``=ध्, ``J``=झ्, …).

**Note:** 1.4.99–1.4.102 (*parasmaipada* / *ātmanepada* / *puruṣa* / *vacana* saṃjñā), **1.4.104**
(*vibhakti* of *sup* / *tiṅ*), and *ṭithīn* *pratyāhāra* naming are **separate** sūtras — not implemented in
this module.
"""
from __future__ import annotations

from typing import Final, FrozenSet, Tuple

# Ten *lakāra* *upadeśa* forms (l + medial + final consonant of the name).
LAKAARA_UPADESHA_SLP1: Final[FrozenSet[str]] = frozenset(
    {
        "laT",
        "liT",
        "luT",
        "lRT",
        "leT",
        "loT",
        "laG",
        "liG",
        "luG",
        "lRG",
    }
)

# 3.4.78 *ādeśa* list (one-to-one with the *Pāṇini* *ṣoḍaśa* + *dva* = 18 items).
TIN_ADESHA_18: Final[Tuple[str, ...]] = (
    "tip",
    "tas",
    "jhi",
    "sip",
    "Tas",
    "Ta",
    "mip",
    "vas",
    "mas",
    "ta",
    "AtAm",
    "Ja",
    "TAs",
    "ATAm",
    "Dvam",
    "iw",
    "vahi",
    "mahiG",
)

TIN_ADESHA_SET: Final[FrozenSet[str]] = frozenset(TIN_ADESHA_18)


def is_tin_adesha(s: str) -> bool:
    return s in TIN_ADESHA_SET


def is_lakara_upadesha(s: str) -> bool:
    return s.strip() in LAKAARA_UPADESHA_SLP1
