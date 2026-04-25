"""
phonology/ajadi_tap_4_1_4.py — eligibility for **4.1.4** *ajādyataṣṭāp* (ṭāp).

*Tatpara* **at**: only **hrasva-akārānta** bases (SLP1 final ``a``, not ``A``).
*Ajādi*: membership in ``data/inputs/ajadi_gana_slp1.json`` (opaque list).

No ``State`` / engine imports.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import FrozenSet, Optional

_MEMBERS: Optional[FrozenSet[str]] = None


def load_ajadi_members() -> FrozenSet[str]:
    global _MEMBERS
    if _MEMBERS is not None:
        return _MEMBERS
    path = Path(__file__).resolve().parents[1] / "data" / "inputs" / "ajadi_gana_slp1.json"
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    _MEMBERS = frozenset(m.strip() for m in data.get("members", []) if m.strip())
    return _MEMBERS


def stem_flat_for_match(stem_meta: object, varna_flat: str) -> str:
    """Prefer ``meta['upadesha_slp1']`` when it is a non-empty string."""
    if isinstance(stem_meta, str) and stem_meta.strip():
        return stem_meta.strip()
    return varna_flat.strip()


def is_hrasva_akaranta_tapara(flat: str) -> bool:
    """*At*-condition: stem ends in hrasa ``a`` (not long ``A`` / *ā*)."""
    s = flat.strip()
    return len(s) >= 1 and s[-1] == "a"


def is_ajadi_stem(flat: str, members: Optional[FrozenSet[str]] = None) -> bool:
    m = members if members is not None else load_ajadi_members()
    return flat.strip() in m


def tap_4_1_4_applies(
    stem_meta_upadesha: object,
    varna_flat_slp1: str,
    *,
    members: Optional[FrozenSet[str]] = None,
) -> bool:
    """
    True iff **4.1.4** may attach ṭāp (engine slice): *ajādi* **or**
    *hrasva-akārānta* (*at*-para).
    """
    flat = stem_flat_for_match(stem_meta_upadesha, varna_flat_slp1)
    if not flat:
        return False
    if is_ajadi_stem(flat, members=members):
        return True
    return is_hrasva_akaranta_tapara(flat)
