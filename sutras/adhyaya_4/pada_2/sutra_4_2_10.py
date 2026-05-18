"""
4.2.10  परिवृतो रथः  —  VIDHI

Padaccheda: परिवृतः रथः

परिवृतो रथः (4.2.10)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_10_parivfto_10"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_10_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.10"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "parivfto raTaH",
    text_dev              = "परिवृतो रथः",
    padaccheda_dev        = "परिवृतः रथः",
    why_dev               = "(सूत्रम् 4.2.10) परिवृतो रथः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
