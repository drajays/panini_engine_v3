"""
6.4.80  वाऽम्शसोः  —  VIDHI

Padaccheda: वा अम्-शसोः

वाऽम्शसोः (6.4.80)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_80_vAmSasoH_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.80", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA'mSasoH",
    text_dev              = "वाऽम्शसोः",
    padaccheda_dev        = "वा अम्-शसोः",
    why_dev               = "(सूत्रम् 6.4.80) वाऽम्शसोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
