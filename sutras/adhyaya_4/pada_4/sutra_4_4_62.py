"""
4.4.62  छत्रादिभ्यो णः  —  VIDHI

Padaccheda: छत्र-आदिभ्यः णः

छत्रादिभ्यो णः (4.4.62)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_62_CatrAdiByo_62"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.62", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CatrAdiByo RaH",
    text_dev              = "छत्रादिभ्यो णः",
    padaccheda_dev        = "छत्र-आदिभ्यः णः",
    why_dev               = "(सूत्रम् 4.4.62) छत्रादिभ्यो णः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
