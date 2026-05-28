"""
7.2.21  प्रभौ परिवृढः  —  VIDHI

Padaccheda: प्रभौ परिवृढः

प्रभौ परिवृढः (7.2.21)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_21_praBO_21"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.21", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_2_21_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "praBO parivfQaH",
    text_dev              = "प्रभौ परिवृढः",
    padaccheda_dev        = "प्रभौ परिवृढः",
    why_dev               = "(सूत्रम् 7.2.21) प्रभौ परिवृढः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
