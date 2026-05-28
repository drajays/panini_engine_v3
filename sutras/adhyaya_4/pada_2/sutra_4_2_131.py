"""
4.2.131  मद्रवृज्योः कन्  —  VIDHI

Padaccheda: मद्र-वृज्योः कन्

मद्रवृज्योः कन् (4.2.131)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_131_madravfjyo_131"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.131", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.131"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.131",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "madravfjyoH kan",
    text_dev              = "मद्रवृज्योः कन्",
    padaccheda_dev        = "मद्र-वृज्योः कन्",
    why_dev               = "(सूत्रम् 4.2.131) मद्रवृज्योः कन्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
