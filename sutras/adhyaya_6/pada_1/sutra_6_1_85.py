"""
6.1.85  अन्तादिवच्च  —  PARIBHASHA

Padaccheda: अन्त-आदि-वत् च

अन्तादिवच्च (6.1.85)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_85_gate"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.85",
    sutra_type            = SutraType.PARIBHASHA,
    text_slp1             = "antAdivacca",
    text_dev              = "अन्तादिवच्च",
    padaccheda_dev        = "अन्त-आदि-वत् च",
    why_dev               = "(सूत्रम् 6.1.85) अन्तादिवच्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
