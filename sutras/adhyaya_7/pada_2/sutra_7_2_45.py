"""
7.2.45  रधादिभ्यश्च  —  VIDHI

Padaccheda: रध-आदिभ्यः च

रधादिभ्यश्च (7.2.45)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_45_raDAdiByaS_45"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.45", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.45"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "raDAdiByaSca",
    text_dev              = "रधादिभ्यश्च",
    padaccheda_dev        = "रध-आदिभ्यः च",
    why_dev               = "(सूत्रम् 7.2.45) रधादिभ्यश्च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
