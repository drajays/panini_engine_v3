"""
8.3.66  सदिरप्रतेः  —  VIDHI

Padaccheda: सदिः (षष्ठ्याः स्थाने प्रथमा) अ-प्रतेः

सदिरप्रतेः (8.3.66)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_66_sadiraprat_66"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_66_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sadiraprateH",
    text_dev              = "सदिरप्रतेः",
    padaccheda_dev        = "सदिः (षष्ठ्याः स्थाने प्रथमा) अ-प्रतेः",
    why_dev               = "(सूत्रम् 8.3.66) सदिरप्रतेः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
