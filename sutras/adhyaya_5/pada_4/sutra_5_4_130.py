"""
5.4.130  ऊर्ध्वाद्विभाषा  —  VIDHI

Padaccheda: ऊर्ध्वाद् विभाषा

ऊर्ध्वाद्विभाषा (5.4.130)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_130_UrDvAdviBA_130"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_130_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.130"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.130",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "UrDvAdviBAzA",
    text_dev              = "ऊर्ध्वाद्विभाषा",
    padaccheda_dev        = "ऊर्ध्वाद् विभाषा",
    why_dev               = "(सूत्रम् 5.4.130) ऊर्ध्वाद्विभाषा।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
