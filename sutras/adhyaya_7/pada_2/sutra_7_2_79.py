"""
7.2.79  लोपः सीयुट्स्योऽनिटि  —  VIDHI

Two operational paths:
  1. Arm ``7_2_79_sIyuw_s_lopa_arm``: original ātmanepada sīyuṭ s-lopa.
  2. Arm ``7_2_79_liG_yasut_arm``: vidhi-liṅ parasmaipada — drop the final
     's' from the yāsuṭ augment term [y,A,s] → [y,A].
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State


def _find_sIyuw(state: State) -> int | None:
    if not state.meta.get("7_2_79_sIyuw_s_lopa_arm"):
        return None
    for i, t in enumerate(state.terms):
        if "ling_sIyuw" not in t.tags:
            continue
        if t.meta.get("7_2_79_sIyuw_done"):
            continue
        if not t.varnas or t.varnas[0].slp1 != "s":
            continue
        return i
    return None


def _find_yasut(state: State) -> int | None:
    """Find the yāsuṭ augment term ending in 's' for vidhi-liṅ s-lopa."""
    if not state.meta.get("7_2_79_liG_yasut_arm"):
        return None
    for i, t in enumerate(state.terms):
        if "yasut_agama" not in t.tags:
            continue
        if t.meta.get("7_2_79_yasut_done"):
            continue
        if not t.varnas or t.varnas[-1].slp1 != "s":
            continue
        return i
    return None


def cond(state: State) -> bool:
    return _find_sIyuw(state) is not None or _find_yasut(state) is not None


def act(state: State) -> State:
    idx = _find_sIyuw(state)
    if idx is not None:
        t = state.terms[idx]
        del t.varnas[0]
        t.meta["7_2_79_sIyuw_done"] = True
        state.meta.pop("7_2_79_sIyuw_s_lopa_arm", None)
        return state

    idx = _find_yasut(state)
    if idx is not None:
        t = state.terms[idx]
        del t.varnas[-1]  # drop final 's' from [y,A,s] → [y,A]
        t.meta["7_2_79_yasut_done"] = True
        state.meta.pop("7_2_79_liG_yasut_arm", None)
        state.samjna_registry["7.2.79_yasut_s_lopa"] = True
        return state

    return state


SUTRA = SutraRecord(
    sutra_id="7.2.79",
    sutra_type=SutraType.VIDHI,
    text_slp1="lopaH sIyutsyo'niwi",
    text_dev="लोपः सीयुट्स्योऽनिटि",
    padaccheda_dev="लोपः / सीयुट्स्यः / अनिटि",
    why_dev="सीयुटः/यासुटः सकारस्य लोपः — विधि-लिङ्-पथः।",
    anuvritti_from=("7.2.76",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
