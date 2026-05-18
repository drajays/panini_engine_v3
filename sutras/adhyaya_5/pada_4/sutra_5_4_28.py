"""
5.4.28  अवेः कः  —  VIDHI

Padaccheda: अवेः कः

अवेः कः (5.4.28)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_28_aveH_28"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_28_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aveH kaH",
    text_dev              = "अवेः कः",
    padaccheda_dev        = "अवेः कः",
    why_dev               = "(सूत्रम् 5.4.28) अवेः कः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
