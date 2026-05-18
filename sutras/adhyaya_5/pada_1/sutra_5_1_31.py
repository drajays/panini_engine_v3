"""
5.1.31  बिस्ताच्च  —  VIDHI

Padaccheda: बिस्तात् च

बिस्ताच्च (5.1.31)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_31_bistAcca_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_31_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bistAcca",
    text_dev              = "बिस्ताच्च",
    padaccheda_dev        = "बिस्तात् च",
    why_dev               = "(सूत्रम् 5.1.31) बिस्ताच्च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
