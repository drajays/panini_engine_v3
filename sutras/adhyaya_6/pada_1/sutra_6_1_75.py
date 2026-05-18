"""
6.1.75  दीर्घात्  —  VIDHI

Padaccheda: दीर्घात्

दीर्घात् (6.1.75)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_75_dIrGAt_75"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_75_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.75"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dIrGAt",
    text_dev              = "दीर्घात्",
    padaccheda_dev        = "दीर्घात्",
    why_dev               = "(सूत्रम् 6.1.75) दीर्घात्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
