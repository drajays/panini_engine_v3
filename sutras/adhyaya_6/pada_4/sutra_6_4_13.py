"""
6.4.13  सौ च  —  VIDHI

Padaccheda: सौ च

सौ च (6.4.13)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_13_sO_13"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_13_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sO ca",
    text_dev              = "सौ च",
    padaccheda_dev        = "सौ च",
    why_dev               = "(सूत्रम् 6.4.13) सौ च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
