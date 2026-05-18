"""
7.3.51  इसुसुक्तान्तात् कः  —  VIDHI

Padaccheda: इस्-उस्-उक्-तान्तात् कः

इसुसुक्तान्तात् कः (7.3.51)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_51_isusuktAnt_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_51_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "isusuktAntAt kaH",
    text_dev              = "इसुसुक्तान्तात् कः",
    padaccheda_dev        = "इस्-उस्-उक्-तान्तात् कः",
    why_dev               = "(सूत्रम् 7.3.51) इसुसुक्तान्तात् कः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
