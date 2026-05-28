"""
6.3.31  उषासोषसः  —  VIDHI

Padaccheda: उषासा उषसः

उषासोषसः (6.3.31)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_31_uzAsozasaH_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uzAsozasaH",
    text_dev              = "उषासोषसः",
    padaccheda_dev        = "उषासा उषसः",
    why_dev               = "(सूत्रम् 6.3.31) उषासोषसः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
