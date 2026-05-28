"""
6.2.181  न निविभ्याम्  —  VIDHI

Padaccheda: न नि-विभ्याम्

न निविभ्याम् (6.2.181)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_181_na_181"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.181"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.181",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na niviByAm",
    text_dev              = "न निविभ्याम्",
    padaccheda_dev        = "न नि-विभ्याम्",
    why_dev               = "(सूत्रम् 6.2.181) न निविभ्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
