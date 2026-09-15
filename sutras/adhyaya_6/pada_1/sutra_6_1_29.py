"""
6.1.29  लिड्यङोश्च  —  VIDHI

Padaccheda: लिट्-यङोः च

लिड्यङोश्च (6.1.29)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_29_liqyaNoSca_29"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.29", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "liqyaNoSca",
    text_dev              = "लिड्यङोश्च",
    padaccheda_dev        = "लिट्-यङोः च",
    why_dev               = "(सूत्रम् 6.1.29) लिड्यङोश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
