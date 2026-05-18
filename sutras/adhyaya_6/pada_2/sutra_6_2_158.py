"""
6.2.158  आक्रोशे च  —  VIDHI

Padaccheda: आक्रोशे च

आक्रोशे च (6.2.158)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_158_AkroSe_158"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_158_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.158"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.158",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AkroSe ca",
    text_dev              = "आक्रोशे च",
    padaccheda_dev        = "आक्रोशे च",
    why_dev               = "(सूत्रम् 6.2.158) आक्रोशे च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
