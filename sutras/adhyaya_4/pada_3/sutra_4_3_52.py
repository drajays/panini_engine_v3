"""
4.3.52  तदस्य सोढम्  —  VIDHI

Padaccheda: तत् अस्य सोढम्

तदस्य सोढम् (4.3.52)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_52_tadasya_52"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_52_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadasya soQam",
    text_dev              = "तदस्य सोढम्",
    padaccheda_dev        = "तत् अस्य सोढम्",
    why_dev               = "(सूत्रम् 4.3.52) तदस्य सोढम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
