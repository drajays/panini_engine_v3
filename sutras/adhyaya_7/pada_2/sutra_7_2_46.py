"""
7.2.46  निरः कुषः  —  VIDHI

Padaccheda: निरः कुषः

निरः कुषः (7.2.46)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_46_niraH_46"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_46_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "niraH kuzaH",
    text_dev              = "निरः कुषः",
    padaccheda_dev        = "निरः कुषः",
    why_dev               = "(सूत्रम् 7.2.46) निरः कुषः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
