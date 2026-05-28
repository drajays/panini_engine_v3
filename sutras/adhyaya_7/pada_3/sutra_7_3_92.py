"""
7.3.92  तृणह इम्  —  VIDHI

Padaccheda: तृणहः इम्

तृणह इम् (7.3.92)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_92_tfRaha_92"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.92", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_3_92_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.92"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.92",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tfRaha im",
    text_dev              = "तृणह इम्",
    padaccheda_dev        = "तृणहः इम्",
    why_dev               = "(सूत्रम् 7.3.92) तृणह इम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
