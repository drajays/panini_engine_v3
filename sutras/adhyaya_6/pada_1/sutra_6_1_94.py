"""
6.1.94  एङि पररूपम्  —  VIDHI

Padaccheda: एङि पररूपम्

एङि पररूपम् (6.1.94)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_94_eNi_94"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_94_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "eNi pararUpam",
    text_dev              = "एङि पररूपम्",
    padaccheda_dev        = "एङि पररूपम्",
    why_dev               = "(सूत्रम् 6.1.94) एङि पररूपम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
