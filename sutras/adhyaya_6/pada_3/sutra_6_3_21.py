"""
6.3.21  षष्ठ्या आक्रोशे  —  VIDHI

Padaccheda: षष्ठ्या आक्रोशे

षष्ठ्या आक्रोशे (6.3.21)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_21_zazWyA_21"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_21_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zazWyA AkroSe",
    text_dev              = "षष्ठ्या आक्रोशे",
    padaccheda_dev        = "षष्ठ्या आक्रोशे",
    why_dev               = "(सूत्रम् 6.3.21) षष्ठ्या आक्रोशे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
