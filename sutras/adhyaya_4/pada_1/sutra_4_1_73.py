"""
4.1.73  शार्ङ्गरवाद्यञो ङीन्  —  VIDHI

Padaccheda: शार्ङ्गरव-आदि-अञः ङीन्

शार्ङ्गरवाद्यञो ङीन् (4.1.73)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_73_SArNgaravA_73"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_73_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.73"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SArNgaravAdyaYo NIn",
    text_dev              = "शार्ङ्गरवाद्यञो ङीन्",
    padaccheda_dev        = "शार्ङ्गरव-आदि-अञः ङीन्",
    why_dev               = "(सूत्रम् 4.1.73) शार्ङ्गरवाद्यञो ङीन्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
