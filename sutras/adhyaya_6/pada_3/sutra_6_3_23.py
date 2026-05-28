"""
6.3.23  ऋतो विद्यायोनिसम्बन्धेभ्यः  —  VIDHI

Padaccheda: ऋतः विद्या-योनि-सम्बन्धेभ्यः

ऋतो विद्यायोनिसम्बन्धेभ्यः (6.3.23)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_23_fto_23"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fto vidyAyonisambanDeByaH",
    text_dev              = "ऋतो विद्यायोनिसम्बन्धेभ्यः",
    padaccheda_dev        = "ऋतः विद्या-योनि-सम्बन्धेभ्यः",
    why_dev               = "(सूत्रम् 6.3.23) ऋतो विद्यायोनिसम्बन्धेभ्यः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
