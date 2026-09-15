"""
8.3.21  उञि च पदे  —  VIDHI

Padaccheda: उञि · च · पदे

उञि च पदे (8.3.21)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_21_uYi_21"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.21", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uYi ca pade",
    text_dev              = "उञि च पदे",
    padaccheda_dev        = "उञि · च · पदे",
    why_dev               = "(सूत्रम् 8.3.21) उञि च पदे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
