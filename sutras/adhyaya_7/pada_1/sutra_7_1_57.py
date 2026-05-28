"""
7.1.57  गोः पादान्ते  —  VIDHI

Padaccheda: गोः पादान्ते

गोः पादान्ते (7.1.57)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_1_57_goH_57"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.1.57", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "goH pAdAnte",
    text_dev              = "गोः पादान्ते",
    padaccheda_dev        = "गोः पादान्ते",
    why_dev               = "(सूत्रम् 7.1.57) गोः पादान्ते।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
