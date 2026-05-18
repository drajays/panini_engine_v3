"""
4.3.16  संधिवेलाऽऽद्यृतुनक्षत्रेभ्योऽण्  —  VIDHI

Padaccheda: संधिवेला-आदि-ऋतु-नक्षत्रेभ्यः अण्

संधिवेलाऽऽद्यृतुनक्षत्रेभ्योऽण् (4.3.16)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_16_saMDivelA_16"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_16_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.16"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMDivelA''dyftunakzatreByo'R",
    text_dev              = "संधिवेलाऽऽद्यृतुनक्षत्रेभ्योऽण्",
    padaccheda_dev        = "संधिवेला-आदि-ऋतु-नक्षत्रेभ्यः अण्",
    why_dev               = "(सूत्रम् 4.3.16) संधिवेलाऽऽद्यृतुनक्षत्रेभ्योऽण्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
