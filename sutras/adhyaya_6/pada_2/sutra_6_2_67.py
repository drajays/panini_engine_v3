"""
6.2.67  विभाषाऽध्यक्षे  —  VIDHI

Padaccheda: विभाषा अध्यक्षे

विभाषाऽध्यक्षे (6.2.67)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_67_viBAzADya_67"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA'Dyakze",
    text_dev              = "विभाषाऽध्यक्षे",
    padaccheda_dev        = "विभाषा अध्यक्षे",
    why_dev               = "(सूत्रम् 6.2.67) विभाषाऽध्यक्षे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
