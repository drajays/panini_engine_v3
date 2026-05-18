"""
5.4.8  विभाषा अञ्चेरदिक्स्त्रियाम्  —  VIDHI

Padaccheda: विभाषा अञ्चेः अ-दिक्-स्त्रियाम्

विभाषा अञ्चेरदिक्स्त्रियाम् (5.4.8)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_8_viBAzA_8"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_8_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.8"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.8",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA aYceradikstriyAm",
    text_dev              = "विभाषा अञ्चेरदिक्स्त्रियाम्",
    padaccheda_dev        = "विभाषा अञ्चेः अ-दिक्-स्त्रियाम्",
    why_dev               = "(सूत्रम् 5.4.8) विभाषा अञ्चेरदिक्स्त्रियाम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
