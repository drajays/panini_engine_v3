"""
7.4.26  च्वौ च  —  VIDHI

Padaccheda: च्वौ च

च्वौ च (7.4.26)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_26_cvO_26"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.26", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "cvO ca",
    text_dev              = "च्वौ च",
    padaccheda_dev        = "च्वौ च",
    why_dev               = "(सूत्रम् 7.4.26) च्वौ च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
