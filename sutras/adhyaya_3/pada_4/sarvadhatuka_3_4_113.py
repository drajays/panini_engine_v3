"""
**3.4.113** *tiṅ-śit* — inventory of *sārvadhātuka* *pratyaya* *upadeśa* (SLP1).

Not a sūtra file.  *Tiṅ* *ādeśa* = ``TIN_ADESHA_18`` (**3.4.78**).  *Śit* = vikaraṇa and selected *kṛt*
*pratyaya* with *it* on *ś*; SLP1 strings are engine-local and **extensible**.

*Śāstra* pedagogy often lists **thirty-three** *pratyaya*; the *FrozenSet* union may be **32** if one SLP1
*upadeśa* is shared.

*Cross-refs:* **3.4.115**–**3.4.116** ( *ārdhadhātuka* *tiṅ* in *liṭ* / āśīr *liṅ* ), **3.4.114**, **1.2.4**, **7.3.84**.

**CONSTITUTION Art. 2:** ``is_sarvadhatuka_upadesha_slp1`` only checks *upadeśa* *strings*.
"""
from __future__ import annotations

from typing import Final, FrozenSet, Tuple

from sutras.adhyaya_1.pada_4.vibhakti_samjna_1_4_104 import TIN_SURFACE_AADESHA_SLP1_EXTRA
from sutras.adhyaya_3.pada_4.tin_adesha_3_4_78 import TIN_ADESHA_18, TIN_ADESHA_SET

# Vikaraṇa (śit).
_SIT_VIK: Final[Tuple[str, ...]] = (
    "Sap",
    "Syan",
    "Snu",
    "SnuM",
    "Sa",
    "Snam",
    "SnA",
)
# *Kṛt* (śit) — *Sa* may coincide with vik. *upadeśa* in the *śāstra* list.
_SIT_KRT: Final[Tuple[str, ...]] = (
    "Satf",
    "SAnac",
    "SAnan",
    "cAnaS",
    "Khas",
    "eS",
    "zadhyE",
    "zadhyOn",
)

SIT_VIK_SARVADHATUKA_SLP1: Final[FrozenSet[str]] = frozenset(_SIT_VIK)
SIT_KRT_SARVADHATUKA_SLP1: Final[FrozenSet[str]] = frozenset(_SIT_KRT)
SIT_SARVADHATUKA_SLP1: Final[FrozenSet[str]] = SIT_VIK_SARVADHATUKA_SLP1 | SIT_KRT_SARVADHATUKA_SLP1
# *anti* (**7.1.3** *ādeśa* for *jhi*) — *sārvadhātuka* *tiṅ*-class for narrow inventory checks.
_TIN_713_EXTRA: Final[Tuple[str, ...]] = ("anti",)
SARVADHATUKA_UPADESHA_SLP1: Final[FrozenSet[str]] = (
    TIN_ADESHA_SET | SIT_SARVADHATUKA_SLP1 | frozenset(_TIN_713_EXTRA) | TIN_SURFACE_AADESHA_SLP1_EXTRA
)

TIN_COUNT: Final[int] = len(TIN_ADESHA_18)
SIT_COUNT: Final[int] = len(SIT_SARVADHATUKA_SLP1)
# Union size (32 if one overlap between vik/kṛt in set theory).
SARVADHATUKA_INVENTORY_N: Final[int] = len(SARVADHATUKA_UPADESHA_SLP1)


def is_sarvadhatuka_upadesha_slp1(s: str) -> bool:
    t = s.strip()
    if t in SARVADHATUKA_UPADESHA_SLP1:
        return True
    if t.endswith("~") and t[:-1] in SARVADHATUKA_UPADESHA_SLP1:
        return True
    return False
