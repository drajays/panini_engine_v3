"""
6.1.167  चतुरः शसि  —  VIDHI

Padaccheda: चतुरः शसि

चतुरः शसि (6.1.167)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_167_caturaH_167"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_167_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.167"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.167",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "caturaH Sasi",
    text_dev              = "चतुरः शसि",
    padaccheda_dev        = "चतुरः शसि",
    why_dev               = "(सूत्रम् 6.1.167) चतुरः शसि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
