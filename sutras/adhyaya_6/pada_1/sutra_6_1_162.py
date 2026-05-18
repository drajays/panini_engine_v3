"""
6.1.162  धातोः  —  VIDHI

Padaccheda: धातोः

धातोः (6.1.162)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_162_DAtoH_162"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_162_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.162"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.162",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "DAtoH",
    text_dev              = "धातोः",
    padaccheda_dev        = "धातोः",
    why_dev               = "(सूत्रम् 6.1.162) धातोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
