"""
4.1.135  चतुष्पाद्भ्यो ढञ्  —  VIDHI

Padaccheda: चतुष्पाद्‍भ्यः ढञ्

चतुष्पाद्भ्यो ढञ् (4.1.135)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_135_catuzpAdBy_135"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_135_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.135"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.135",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "catuzpAdByo QaY",
    text_dev              = "चतुष्पाद्भ्यो ढञ्",
    padaccheda_dev        = "चतुष्पाद्‍भ्यः ढञ्",
    why_dev               = "(सूत्रम् 4.1.135) चतुष्पाद्भ्यो ढञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
