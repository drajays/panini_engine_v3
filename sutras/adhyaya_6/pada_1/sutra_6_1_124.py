"""
6.1.124  इन्द्रे च  —  VIDHI

Padaccheda: इन्द्रे च (नित्यम् )

इन्द्रे च (6.1.124)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_124_indre_124"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.124", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.124"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.124",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "indre ca",
    text_dev              = "इन्द्रे च",
    padaccheda_dev        = "इन्द्रे च (नित्यम् )",
    why_dev               = "(सूत्रम् 6.1.124) इन्द्रे च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
