"""
5.1.57  तदस्य परिमाणम्  —  VIDHI

Padaccheda: तत् अस्य परिमाणम्

तदस्य परिमाणम् (5.1.57)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_57_tadasya_57"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_57_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadasya parimARam",
    text_dev              = "तदस्य परिमाणम्",
    padaccheda_dev        = "तत् अस्य परिमाणम्",
    why_dev               = "(सूत्रम् 5.1.57) तदस्य परिमाणम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
