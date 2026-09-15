"""
engine/vareya_1_1_58.py — **1.1.58** *vareya* lopa: *acaḥ* *sthānivat* blocks for *y*-lopa.

When **1.1.57** is on but **1.1.58** is not, a **6.4.48** *para-nimitta* ``a``-lopa
is still *sthānivat* and blocks **6.1.66** / **6.1.70** *vyor vali* (ghost ``a``
between ``y`` and val/i).
"""
from __future__ import annotations

from engine.state import State

_GATE_1_1_57 = "1.1.57_aca_parasmin_purvavidhau"
_GATE_1_1_58 = "1_1_58_na_padAnta_etc"

_META_6_4_48_PARA_NIMITTA_AC = frozenset({
    "6_4_48_yaG_a_lopa_para_nimitta",
    "6_4_48_ktic_a_lopa_para_nimitta",
})

_VYOR_VALI_INITIALS = frozenset({"v", "l", "r", "t"})


def aca_sthanivat_blocks_yakaralopa(state: State, ang) -> bool:
    """
    True when *y*-lopa must **not** apply: **1.1.57** without **1.1.58** after
    **6.4.48** *a*-lopa on this *aṅga*.
    """
    if not ang.meta.get("6_4_48_a_lopa_done"):
        return False
    if not any(ang.meta.get(k) for k in _META_6_4_48_PARA_NIMITTA_AC):
        return False
    if state.paribhasha_gates.get(_GATE_1_1_58):
        return False
    return state.paribhasha_gates.get(_GATE_1_1_57) is True


def vyor_vali_initial_of_following(term) -> str | None:
    """First *vali* / *vyor* letter relevant for *lopo vyor vali* (incl. *t* inside *ktic*)."""
    if not term.varnas:
        return None
    up = (term.meta.get("upadesha_slp1") or "").strip()
    if up == "ktic":
        for v in term.varnas:
            if v.slp1 == "t":
                return "t"
    return term.varnas[0].slp1


def is_vyor_vali_following(varna_slp1: str) -> bool:
    return varna_slp1 in _VYOR_VALI_INITIALS
