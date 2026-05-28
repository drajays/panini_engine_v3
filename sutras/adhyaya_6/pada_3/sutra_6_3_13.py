"""
6.3.13  बन्धे च विभाषा  —  VIDHI

Padaccheda: बन्धे च विभाषा

बन्धे च विभाषा (6.3.13)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_13_banDe_13"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "banDe ca viBAzA",
    text_dev              = "बन्धे च विभाषा",
    padaccheda_dev        = "बन्धे च विभाषा",
    why_dev               = "(सूत्रम् 6.3.13) बन्धे च विभाषा।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
