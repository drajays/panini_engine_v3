"""
8.2.10  झयः  —  VIDHI

Padaccheda: झयः

झयः (8.2.10)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_10_JayaH_10"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.10", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.10"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "JayaH",
    text_dev              = "झयः",
    padaccheda_dev        = "झयः",
    why_dev               = "(सूत्रम् 8.2.10) झयः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
