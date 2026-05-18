"""
5.1.95  तस्य च दक्षिणा यज्ञाख्येभ्यः  —  VIDHI

Padaccheda: तस्य च दक्षिणा यज्ञाख्येभ्यः

तस्य च दक्षिणा यज्ञाख्येभ्यः (5.1.95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_95_tasya_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_95_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tasya ca dakziRA yajYAKyeByaH",
    text_dev              = "तस्य च दक्षिणा यज्ञाख्येभ्यः",
    padaccheda_dev        = "तस्य च दक्षिणा यज्ञाख्येभ्यः",
    why_dev               = "(सूत्रम् 5.1.95) तस्य च दक्षिणा यज्ञाख्येभ्यः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
