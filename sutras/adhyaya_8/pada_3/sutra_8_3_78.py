"""
8.3.78  इणः षीध्वंलुङ्लिटां धोऽङ्गात्  —  VIDHI

Padaccheda: इणः षीध्वं-लुङ्-लिटाम् धः अङ्गात्

इणः षीध्वंलुङ्लिटां धोऽङ्गात् (8.3.78)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_78_iRaH_78"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_78_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.78"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.78",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "iRaH zIDvaMluNliwAM Do'NgAt",
    text_dev              = "इणः षीध्वंलुङ्लिटां धोऽङ्गात्",
    padaccheda_dev        = "इणः षीध्वं-लुङ्-लिटाम् धः अङ्गात्",
    why_dev               = "(सूत्रम् 8.3.78) इणः षीध्वंलुङ्लिटां धोऽङ्गात्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
