"""
7.4.69  दीर्घ इणः किति  —  VIDHI

Padaccheda: दीर्घः इणः किति

दीर्घ इणः किति (7.4.69)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_69_dIrGa_69"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.69", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_4_69_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dIrGa iRaH kiti",
    text_dev              = "दीर्घ इणः किति",
    padaccheda_dev        = "दीर्घः इणः किति",
    why_dev               = "(सूत्रम् 7.4.69) दीर्घ इणः किति।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
