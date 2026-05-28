"""
7.3.116  ङेराम्नद्याम्नीभ्यः  —  VIDHI

Padaccheda: ङेः आम् नदी-आम्-नीभ्यः

ङेराम्नद्याम्नीभ्यः (7.3.116)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_116_NerAmnadyA_116"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.116", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.116"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "NerAmnadyAmnIByaH",
    text_dev              = "ङेराम्नद्याम्नीभ्यः",
    padaccheda_dev        = "ङेः आम् नदी-आम्-नीभ्यः",
    why_dev               = "(सूत्रम् 7.3.116) ङेराम्नद्याम्नीभ्यः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
