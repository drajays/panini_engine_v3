"""
6.4.42  जनसनखनां सञ्झलोः  —  VIDHI

Padaccheda: जन-सन-खनाम् सन्-झलोः

जनसनखनां सञ्झलोः (6.4.42)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_42_janasanaKa_42"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_42_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "janasanaKanAM saYJaloH",
    text_dev              = "जनसनखनां सञ्झलोः",
    padaccheda_dev        = "जन-सन-खनाम् सन्-झलोः",
    why_dev               = "(सूत्रम् 6.4.42) जनसनखनां सञ्झलोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
