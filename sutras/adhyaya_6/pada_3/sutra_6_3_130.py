"""
6.3.130  मित्रे चर्षौ  —  VIDHI

Padaccheda: मित्रे च ऋषौ

मित्रे चर्षौ (6.3.130)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_130_mitre_130"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.130"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.130",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mitre carzO",
    text_dev              = "मित्रे चर्षौ",
    padaccheda_dev        = "मित्रे च ऋषौ",
    why_dev               = "(सूत्रम् 6.3.130) मित्रे चर्षौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
