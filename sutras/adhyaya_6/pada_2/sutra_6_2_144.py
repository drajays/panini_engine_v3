"""
6.2.144  थाथघञ्क्ताजबित्रकाणाम्  —  VIDHI

Padaccheda: थ-अथ-घञ्-क्त-अच्-अप्-इत्र-काणाम्

थाथघञ्क्ताजबित्रकाणाम् (6.2.144)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_144_TATaGaYktA_144"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.144"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.144",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "TATaGaYktAjabitrakARAm",
    text_dev              = "थाथघञ्क्ताजबित्रकाणाम्",
    padaccheda_dev        = "थ-अथ-घञ्-क्त-अच्-अप्-इत्र-काणाम्",
    why_dev               = "(सूत्रम् 6.2.144) थाथघञ्क्ताजबित्रकाणाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
