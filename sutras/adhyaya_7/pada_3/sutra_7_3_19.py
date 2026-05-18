"""
7.3.19  हृद्भगसिन्ध्वन्ते पूर्वपदस्य च  —  VIDHI

Padaccheda: हृद्-भग-सिन्धु-अन्ते पूर्वपदस्य च

हृद्भगसिन्ध्वन्ते पूर्वपदस्य च (7.3.19)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_19_hfdBagasin_19"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_19_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.19",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hfdBagasinDvante pUrvapadasya ca",
    text_dev              = "हृद्भगसिन्ध्वन्ते पूर्वपदस्य च",
    padaccheda_dev        = "हृद्-भग-सिन्धु-अन्ते पूर्वपदस्य च",
    why_dev               = "(सूत्रम् 7.3.19) हृद्भगसिन्ध्वन्ते पूर्वपदस्य च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
