"""
6.4.126  न शसददवादिगुणानाम्  —  VIDHI

Padaccheda: न शस-दद-व-आदि-गुणानाम्

न शसददवादिगुणानाम् (6.4.126)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_126_na_126"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_126_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.126"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.126",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na SasadadavAdiguRAnAm",
    text_dev              = "न शसददवादिगुणानाम्",
    padaccheda_dev        = "न शस-दद-व-आदि-गुणानाम्",
    why_dev               = "(सूत्रम् 6.4.126) न शसददवादिगुणानाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
