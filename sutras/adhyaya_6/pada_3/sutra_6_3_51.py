"""
6.3.51  वा शोकष्यञ्रोगेषु  —  VIDHI

Padaccheda: वा शोक-ष्यञ्-रोगेषु

वा शोकष्यञ्रोगेषु (6.3.51)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_51_vA_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA SokazyaYrogezu",
    text_dev              = "वा शोकष्यञ्रोगेषु",
    padaccheda_dev        = "वा शोक-ष्यञ्-रोगेषु",
    why_dev               = "(सूत्रम् 6.3.51) वा शोकष्यञ्रोगेषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
