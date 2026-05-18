"""
8.4.36  नशेः षान्तस्य  —  VIDHI

Padaccheda: नशेः ष-अन्तस्य

नशेः षान्तस्य (8.4.36)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_36_naSeH_36"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_4_36_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "naSeH zAntasya",
    text_dev              = "नशेः षान्तस्य",
    padaccheda_dev        = "नशेः ष-अन्तस्य",
    why_dev               = "(सूत्रम् 8.4.36) नशेः षान्तस्य।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
