"""
6.3.37  न कोपधायाः  —  VIDHI

Padaccheda: न कउपधायाः

न कोपधायाः (6.3.37)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_37_na_37"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na kopaDAyAH",
    text_dev              = "न कोपधायाः",
    padaccheda_dev        = "न कउपधायाः",
    why_dev               = "(सूत्रम् 6.3.37) न कोपधायाः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
