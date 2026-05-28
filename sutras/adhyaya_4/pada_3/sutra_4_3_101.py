"""
4.3.101  तेन प्रोक्तम्  —  VIDHI

Padaccheda: तेन प्रोक्तम्

तेन प्रोक्तम् (4.3.101)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_101_tena_101"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.101", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.101"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.101",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tena proktam",
    text_dev              = "तेन प्रोक्तम्",
    padaccheda_dev        = "तेन प्रोक्तम्",
    why_dev               = "(सूत्रम् 4.3.101) तेन प्रोक्तम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
