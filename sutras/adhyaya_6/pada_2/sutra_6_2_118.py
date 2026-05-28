"""
6.2.118  क्रत्वादयश्च  —  VIDHI

Padaccheda: क्रतु-आदयः च

क्रत्वादयश्च (6.2.118)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_118_kratvAdaya_118"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.118"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.118",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kratvAdayaSca",
    text_dev              = "क्रत्वादयश्च",
    padaccheda_dev        = "क्रतु-आदयः च",
    why_dev               = "(सूत्रम् 6.2.118) क्रत्वादयश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
