"""
8.2.56  नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम्  —  VIDHI

Padaccheda: नुद-विद-उन्द-त्रा-घ्रा-ह्रीभ्यः अन्यतरस्याम्

नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम् (8.2.56)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_56_nudavidond_56"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_56_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nudavidondatrAGrAhrIByo'nyatarasyAm",
    text_dev              = "नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम्",
    padaccheda_dev        = "नुद-विद-उन्द-त्रा-घ्रा-ह्रीभ्यः अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 8.2.56) नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
