"""
8.2.7  नलोपः प्रातिपदिकान्तस्य  —  VIDHI

Narrow v3: in **trc_nom_sg_pipeline**, elide final ``n`` of the prātipadika
before visarga/sandhi — ``cetAn`` → ``cetA`` (Tripāḍī).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not state.meta.get("trc_nom_sg_pipeline"):
        return False
    if not state.tripadi_zone:
        return False
    if len(state.terms) != 1:
        return False
    t0 = state.terms[0]
    if "pada" not in t0.tags:
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
