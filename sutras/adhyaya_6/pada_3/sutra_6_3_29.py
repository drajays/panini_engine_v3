"""
6.3.29  दिवो द्यावा  —  VIDHI

Padaccheda: दिवः द्यावा

दिवो द्यावा (6.3.29)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_29_divo_29"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "divo dyAvA",
    text_dev              = "दिवो द्यावा",
    padaccheda_dev        = "दिवः द्यावा",
    why_dev               = "(सूत्रम् 6.3.29) दिवो द्यावा।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
