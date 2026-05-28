"""
6.3.36  क्यङ्मानिनोश्च  —  VIDHI

Padaccheda: क्यङ्-मानिनोः च

क्यङ्मानिनोश्च (6.3.36)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_36_kyaNmAnino_36"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kyaNmAninoSca",
    text_dev              = "क्यङ्मानिनोश्च",
    padaccheda_dev        = "क्यङ्-मानिनोः च",
    why_dev               = "(सूत्रम् 6.3.36) क्यङ्मानिनोश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
