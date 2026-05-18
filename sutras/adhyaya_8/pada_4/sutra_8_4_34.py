"""
8.4.34  न भाभूपूकमिगमिप्यायीवेपाम्  —  VIDHI

Padaccheda: न भा-भू-पू-कमि-गमि-प्यायी-वेपाम्

न भाभूपूकमिगमिप्यायीवेपाम् (8.4.34)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_34_na_34"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_4_34_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na BABUpUkamigamipyAyIvepAm",
    text_dev              = "न भाभूपूकमिगमिप्यायीवेपाम्",
    padaccheda_dev        = "न भा-भू-पू-कमि-गमि-प्यायी-वेपाम्",
    why_dev               = "(सूत्रम् 8.4.34) न भाभूपूकमिगमिप्यायीवेपाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
