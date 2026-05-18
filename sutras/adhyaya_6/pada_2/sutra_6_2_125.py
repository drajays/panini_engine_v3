"""
6.2.125  आदिश्चिहणादीनाम्  —  VIDHI

Padaccheda: आदिः चिहण-आदीनाम्

आदिश्चिहणादीनाम् (6.2.125)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_125_AdiScihaRA_125"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_125_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.125"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AdiScihaRAdInAm",
    text_dev              = "आदिश्चिहणादीनाम्",
    padaccheda_dev        = "आदिः चिहण-आदीनाम्",
    why_dev               = "(सूत्रम् 6.2.125) आदिश्चिहणादीनाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
