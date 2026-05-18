"""
6.3.103  तृणे च जातौ  —  VIDHI

Padaccheda: तृणे च जातौ

तृणे च जातौ (6.3.103)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_103_tfRe_103"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_103_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tfRe ca jAtO",
    text_dev              = "तृणे च जातौ",
    padaccheda_dev        = "तृणे च जातौ",
    why_dev               = "(सूत्रम् 6.3.103) तृणे च जातौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
