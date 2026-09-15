"""
8.1.50  शेषे विभाषा  —  VIDHI

Padaccheda: शेषे विभाषा

शेषे विभाषा (8.1.50)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_50_Seze_50"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.50", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Seze viBAzA",
    text_dev              = "शेषे विभाषा",
    padaccheda_dev        = "शेषे विभाषा",
    why_dev               = "(सूत्रम् 8.1.50) शेषे विभाषा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
