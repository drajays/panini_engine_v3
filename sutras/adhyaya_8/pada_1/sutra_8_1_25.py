"""
8.1.25  पश्यार्थैश्चानालोचने  —  VIDHI

Padaccheda: पश्य-अर्थैः च अनालोचने

पश्यार्थैश्चानालोचने (8.1.25)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_25_paSyArTESc_25"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.25", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paSyArTEScAnAlocane",
    text_dev              = "पश्यार्थैश्चानालोचने",
    padaccheda_dev        = "पश्य-अर्थैः च अनालोचने",
    why_dev               = "(सूत्रम् 8.1.25) पश्यार्थैश्चानालोचने।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
