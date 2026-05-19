"""
7.4.52  ह एति  —  VIDHI

In luṭ karmani 1sg: tāsi's final `s` → `h` before `e` (the 1sg tiṅ ādeśa from
iṭ+3.4.79: iṭ→i→e). So `tāse → tāhe` → final form `bhavitāhe`.

  tās + e  →  tāh + e = tāhe

Arm flag: state.meta["7_4_52_arm"] must be True.
Finds tāsi term with final s, followed by a term starting with e.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import mk as _mk


def _find_tasi_s_before_e(state: State):
    if not state.meta.get("7_4_52_arm"):
        return None
    for i in range(len(state.terms) - 1):
        t1, t2 = state.terms[i], state.terms[i + 1]
        if not t1.meta.get("tAsi_vikaraṇa"):
            continue
        if t1.meta.get("7_4_52_done"):
            continue
        if not t1.varnas or t1.varnas[-1].slp1 != "s":
            continue
        if not t2.varnas or t2.varnas[0].slp1 != "e":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_tasi_s_before_e(state) is not None


def act(state: State) -> State:
    i = _find_tasi_s_before_e(state)
    if i is None:
        return state
    t = state.terms[i]
    t.varnas[-1] = _mk("h")  # s → h
    t.meta["7_4_52_done"] = True
    state.meta.pop("7_4_52_arm", None)
    state.samjna_registry["7.4.52_ha_eti"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ha eti",
    text_dev              = "ह एति",
    padaccheda_dev        = "हः एति",
    why_dev               = "(सूत्रम् 7.4.52) ह एति।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
