"""
4.3.127  संघाङ्कलक्षणेष्वञ्यञिञामण्  —  VIDHI

Padaccheda: संघ-अङ्क-लक्षणेषु अञ्-यञ्-इञाम् अण्

संघाङ्कलक्षणेष्वञ्यञिञामण् (4.3.127)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_127_saMGANkala_127"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_127_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.127"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.127",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMGANkalakzaRezvaYyaYiYAmaR",
    text_dev              = "संघाङ्कलक्षणेष्वञ्यञिञामण्",
    padaccheda_dev        = "संघ-अङ्क-लक्षणेषु अञ्-यञ्-इञाम् अण्",
    why_dev               = "(सूत्रम् 4.3.127) संघाङ्कलक्षणेष्वञ्यञिञामण्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
