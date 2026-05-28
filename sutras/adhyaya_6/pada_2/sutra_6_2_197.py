"""
6.2.197  द्वित्रिभ्यां पाद्दन्मूर्धसु बहुव्रीहौ  —  VIDHI

Padaccheda: द्वि-त्रिभ्याम् पाद्-दत्-मूर्धसु बहुव्रीहौ

द्वित्रिभ्यां पाद्दन्मूर्धसु बहुव्रीहौ (6.2.197)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_197_dvitriByAM_197"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.197"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.197",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvitriByAM pAddanmUrDasu bahuvrIhO",
    text_dev              = "द्वित्रिभ्यां पाद्दन्मूर्धसु बहुव्रीहौ",
    padaccheda_dev        = "द्वि-त्रिभ्याम् पाद्-दत्-मूर्धसु बहुव्रीहौ",
    why_dev               = "(सूत्रम् 6.2.197) द्वित्रिभ्यां पाद्दन्मूर्धसु बहुव्रीहौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
