"""
8.1.32  सत्यं प्रश्ने  —  VIDHI

Padaccheda: सत्यम् प्रश्ने

सत्यं प्रश्ने (8.1.32)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_32_satyaM_32"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_1_32_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "satyaM praSne",
    text_dev              = "सत्यं प्रश्ने",
    padaccheda_dev        = "सत्यम् प्रश्ने",
    why_dev               = "(सूत्रम् 8.1.32) सत्यं प्रश्ने।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
