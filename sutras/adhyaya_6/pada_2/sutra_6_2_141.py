"""
6.2.141  देवताद्वंद्वे च  —  VIDHI

Padaccheda: देवताद्वन्द्वे च

देवताद्वंद्वे च (6.2.141)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_141_devatAdvaM_141"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.141"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.141",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "devatAdvaMdve ca",
    text_dev              = "देवताद्वंद्वे च",
    padaccheda_dev        = "देवताद्वन्द्वे च",
    why_dev               = "(सूत्रम् 6.2.141) देवताद्वंद्वे च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
