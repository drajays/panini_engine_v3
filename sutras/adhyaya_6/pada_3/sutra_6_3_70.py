"""
6.3.70  कारे सत्यागदस्य  —  VIDHI

Padaccheda: कारे सत्य-अगदस्य

कारे सत्यागदस्य (6.3.70)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_70_kAre_70"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_70_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kAre satyAgadasya",
    text_dev              = "कारे सत्यागदस्य",
    padaccheda_dev        = "कारे सत्य-अगदस्य",
    why_dev               = "(सूत्रम् 6.3.70) कारे सत्यागदस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
