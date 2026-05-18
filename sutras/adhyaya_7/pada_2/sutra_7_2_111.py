"""
7.2.111  इदोऽय् पुंसि  —  VIDHI

Padaccheda: इदः अय् पुंसि

इदोऽय् पुंसि (7.2.111)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_111_idoy_111"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_111_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ido'y puMsi",
    text_dev              = "इदोऽय् पुंसि",
    padaccheda_dev        = "इदः अय् पुंसि",
    why_dev               = "(सूत्रम् 7.2.111) इदोऽय् पुंसि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
