"""
8.2.51  शुषः कः  —  VIDHI

Padaccheda: शुषः कः

शुषः कः (8.2.51)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_51_SuzaH_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_51_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SuzaH kaH",
    text_dev              = "शुषः कः",
    padaccheda_dev        = "शुषः कः",
    why_dev               = "(सूत्रम् 8.2.51) शुषः कः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
