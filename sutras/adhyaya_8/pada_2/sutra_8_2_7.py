"""
8.2.7  नलोपः प्रातिपदिकान्तस्य  —  VIDHI

Operational role (v3.6):
  In Tripāḍī zone, for a pada that ends in final ``n``, elide that ``n`` when
  the caller arms this rule for a specific demo slice (e.g. ``rAjAn`` → ``rAjA``).

Legacy slice:
  Also supports the existing **tṛc** nominal output path (``krt_tfc`` on the
  pada), which is treated as always-armed within that narrow demo family.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.tripadi_zone:
        return False
    if len(state.terms) != 1:
        return False
    t0 = state.terms[0]
    if "pada" not in t0.tags:
        return False
    armed = ("krt_tfc" in t0.tags) or bool(state.meta.get("8_2_7_arm"))
    if not armed:
        return False
    if t0.meta.get("nalopa_8_2_7_done"):
        return False
    if not t0.varnas:
        return False
    return t0.varnas[-1].slp1 == "n"


def act(state: State) -> State:
    t0 = state.terms[0]
    t0.varnas.pop()
    t0.meta["nalopa_8_2_7_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.2.7",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "nalopaH prAtipadikAntasya",
    text_dev       = "नलोपः प्रातिपदिकान्तस्य",
    padaccheda_dev = "न-लोपः प्रातिपदिकान्तस्य",
    why_dev        = "प्रातिपदिकान्त्यवर्णे नकारस्य लोपः (चेता-पथ)।",
    anuvritti_from = ("8.2.6",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
