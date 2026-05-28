"""
6.2.196  विभाषोत्पुच्छे  —  VIDHI

Padaccheda: विभाषा उत्पुच्छे

विभाषोत्पुच्छे (6.2.196)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_196_viBAzotpuc_196"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.196"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.196",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzotpucCe",
    text_dev              = "विभाषोत्पुच्छे",
    padaccheda_dev        = "विभाषा उत्पुच्छे",
    why_dev               = "(सूत्रम् 6.2.196) विभाषोत्पुच्छे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
