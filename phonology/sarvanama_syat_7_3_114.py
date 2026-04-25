"""
phonology/sarvanama_syat_7_3_114.py — structural checks for **7.3.114**
*sarvanāmnaḥ syāḍ hr̥asvaś ca* (ṅit *sup* after *ā*-final sarvanāma).

No ``State`` import; callers pass flat strings / upadeśa ids.
"""
from __future__ import annotations

from typing import FrozenSet

# ṅit *sup* pratyayas keyed like ``4.1.2`` inventory (same set as 7.3.111).
_NGIT_SUP_UPADESHA: FrozenSet[str] = frozenset({"Ne", "Nas", "Nasi"})


def ngit_sup_upadeshas() -> FrozenSet[str]:
    return _NGIT_SUP_UPADESHA


def is_abanta_flat(flat_slp1: str) -> bool:
    """*Āp* / *ā-banta*: stem ends in SLP1 long ``A`` (not ``a``)."""
    s = flat_slp1.strip()
    return len(s) >= 1 and s[-1] == "A"


def ngit_sup_match(upadesha_slp1: object) -> bool:
    return isinstance(upadesha_slp1, str) and upadesha_slp1 in _NGIT_SUP_UPADESHA
