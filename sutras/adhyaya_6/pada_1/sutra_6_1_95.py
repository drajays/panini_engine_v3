"""
6.1.95  ओमाङोश्च  —  VIDHI

Padaccheda: ओम्-आङोः च

ओमाङोश्च (6.1.95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_95_omANgoSca_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_95_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "omANgoSca",
    text_dev              = "ओमाङोश्च",
    padaccheda_dev        = "ओम्-आङोः च",
    why_dev               = "(सूत्रम् 6.1.95) ओमाङोश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
