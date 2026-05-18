"""
7.4.85  नुगतोऽनुनासिकान्तस्य  —  VIDHI

Padaccheda: नुक् अतः अनुनासिकान्तस्य

नुगतोऽनुनासिकान्तस्य (7.4.85)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_85_nugatonun_85"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_85_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.85"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.85",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nugato'nunAsikAntasya",
    text_dev              = "नुगतोऽनुनासिकान्तस्य",
    padaccheda_dev        = "नुक् अतः अनुनासिकान्तस्य",
    why_dev               = "(सूत्रम् 7.4.85) नुगतोऽनुनासिकान्तस्य।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
