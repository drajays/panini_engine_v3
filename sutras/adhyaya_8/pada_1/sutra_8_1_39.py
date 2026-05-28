"""
8.1.39  तुपश्यपश्यताहैः पूजायाम्  —  VIDHI

Padaccheda: तु-पश्य-पश्यत-अहैः पूजायाम्

तुपश्यपश्यताहैः पूजायाम् (8.1.39)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_39_tupaSyapaS_39"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tupaSyapaSyatAhEH pUjAyAm",
    text_dev              = "तुपश्यपश्यताहैः पूजायाम्",
    padaccheda_dev        = "तु-पश्य-पश्यत-अहैः पूजायाम्",
    why_dev               = "(सूत्रम् 8.1.39) तुपश्यपश्यताहैः पूजायाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
