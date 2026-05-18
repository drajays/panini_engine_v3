"""
6.2.109  नदी बन्धुनि  —  VIDHI

Padaccheda: नदी बन्धुनि

नदी बन्धुनि (6.2.109)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_109_nadI_109"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_109_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.109"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.109",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nadI banDuni",
    text_dev              = "नदी बन्धुनि",
    padaccheda_dev        = "नदी बन्धुनि",
    why_dev               = "(सूत्रम् 6.2.109) नदी बन्धुनि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
