"""
5.4.39  मृदस्तिकन्  —  VIDHI

Padaccheda: मृदः तिकन्

मृदस्तिकन् (5.4.39)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_39_mfdastikan_39"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_39_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mfdastikan",
    text_dev              = "मृदस्तिकन्",
    padaccheda_dev        = "मृदः तिकन्",
    why_dev               = "(सूत्रम् 5.4.39) मृदस्तिकन्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
