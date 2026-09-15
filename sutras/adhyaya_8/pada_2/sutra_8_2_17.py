"""
8.2.17  नाद्घस्य  —  VIDHI

Padaccheda: नात् घस्य

नाद्घस्य (8.2.17)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_17_nAdGasya_17"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.17", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nAdGasya",
    text_dev              = "नाद्घस्य",
    padaccheda_dev        = "नात् घस्य",
    why_dev               = "(सूत्रम् 8.2.17) नाद्घस्य।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
