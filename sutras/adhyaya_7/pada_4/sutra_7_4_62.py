"""
7.4.62  कुहोश्चुः  —  VIDHI (narrow demo)

Demo slice (जिघृक्षति):
  In the abhyāsa, replace initial guttural `g` (ku) with its corresponding
  palatal `j` (cu).

Teaching **P040** (*juhoti*): *abhyāsa* initial **h** (``hu``) → **j**
(``P040_juhoti_abhyasa`` + ``state.meta['P040_7_4_62_abhyasa_arm']``).

Engine:
  - recipe arms via ``state.meta['7_4_62_kuhoscu_abhyasa_arm']``.
  - **P040** via ``state.meta['P040_7_4_62_abhyasa_arm']``.
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology import mk


def _find(state: State):
    if not state.meta.get("7_4_62_kuhoscu_abhyasa_arm"):
        return None
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if t.meta.get("7_4_62_done"):
            continue
        if not t.varnas:
            continue
        # **g** or **G** (घ) → **j** (P034 *jakṣatuḥ* abhyāsa, *kuhoścuḥ* narrow).
        if t.varnas[0].slp1 in {"g", "G"}:
            return ti
    return None


def _find_p040_juhoti(state: State):
    if not state.meta.get("P040_7_4_62_abhyasa_arm"):
        return None
    for ti, t in enumerate(state.terms):
        if "abhyasa" not in t.tags:
            continue
        if "P040_juhoti_abhyasa" not in t.tags:
            continue
        if t.meta.get("7_4_62_done"):
            continue
        if not t.varnas:
            continue
        if t.varnas[0].slp1 == "h":
            return ti
    return None


def cond(state: State) -> bool:
    return _find(state) is not None or _find_p040_juhoti(state) is not None


def act(state: State) -> State:
    ti_p = _find_p040_juhoti(state)
    if ti_p is not None:
        t = state.terms[ti_p]
        t.varnas[0] = mk("j")
        t.meta["7_4_62_done"] = True
        state.meta.pop("P040_7_4_62_abhyasa_arm", None)
        return state
    ti = _find(state)
    if ti is None:
        return state
    t = state.terms[ti]
    t.varnas[0] = mk("j")
    t.meta["7_4_62_done"] = True
    state.meta["7_4_62_kuhoscu_abhyasa_arm"] = False
    return state


SUTRA = SutraRecord(
    sutra_id="7.4.62",
    sutra_type=SutraType.VIDHI,
    text_slp1="kuhoScuH (narrow)",
    text_dev="कुहोश्चुः",
    padaccheda_dev="कुहोः / चुः",
    why_dev="अभ्यासे कु-वर्णस्य चु-आदेशः (ग→ज) — जिघृक्षति।",
    anuvritti_from=("7.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)

