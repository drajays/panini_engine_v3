"""
7.4.57  मुचोऽकर्मकस्य गुणो वा  —  VIDHI

Padaccheda: मुचः अकर्मकस्य गुणः वा

मुचोऽकर्मकस्य गुणो वा (7.4.57)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_57_mucokarma_57"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.57", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "muco'karmakasya guRo vA",
    text_dev              = "मुचोऽकर्मकस्य गुणो वा",
    padaccheda_dev        = "मुचः अकर्मकस्य गुणः वा",
    why_dev               = "(सूत्रम् 7.4.57) मुचोऽकर्मकस्य गुणो वा।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
