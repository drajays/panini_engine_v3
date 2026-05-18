"""
4.4.7  नौद्व्यचष्ठन्  —  VIDHI

Padaccheda: नौ-द्वि-अचः ठन्

नौद्व्यचष्ठन् (4.4.7)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_7_nOdvyacazW_7"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_7_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nOdvyacazWan",
    text_dev              = "नौद्व्यचष्ठन्",
    padaccheda_dev        = "नौ-द्वि-अचः ठन्",
    why_dev               = "(सूत्रम् 4.4.7) नौद्व्यचष्ठन्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
