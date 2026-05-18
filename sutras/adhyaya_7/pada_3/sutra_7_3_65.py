"""
7.3.65  ण्य आवश्यके  —  VIDHI

Padaccheda: ण्ये आवश्यके

ण्य आवश्यके (7.3.65)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_65_Rya_65"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_65_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Rya AvaSyake",
    text_dev              = "ण्य आवश्यके",
    padaccheda_dev        = "ण्ये आवश्यके",
    why_dev               = "(सूत्रम् 7.3.65) ण्य आवश्यके।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
