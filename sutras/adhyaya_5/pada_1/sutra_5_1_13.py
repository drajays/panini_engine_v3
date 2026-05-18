"""
5.1.13  छदिरुपधिबलेः ढञ्  —  VIDHI

Padaccheda: छदिः-उपधि-बलेः ढञ्

छदिरुपधिबलेः ढञ् (5.1.13)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_13_CadirupaDi_13"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_13_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CadirupaDibaleH QaY",
    text_dev              = "छदिरुपधिबलेः ढञ्",
    padaccheda_dev        = "छदिः-उपधि-बलेः ढञ्",
    why_dev               = "(सूत्रम् 5.1.13) छदिरुपधिबलेः ढञ्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
