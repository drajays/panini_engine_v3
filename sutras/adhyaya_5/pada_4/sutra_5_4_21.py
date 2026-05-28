"""
5.4.21  तत्प्रकृतवचने मयट्  —  VIDHI

Padaccheda: तत् प्रकृतवचने मयट्

तत्प्रकृतवचने मयट् (5.4.21)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_21_tatprakfta_21"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.21", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tatprakftavacane mayaw",
    text_dev              = "तत्प्रकृतवचने मयट्",
    padaccheda_dev        = "तत् प्रकृतवचने मयट्",
    why_dev               = "(सूत्रम् 5.4.21) तत्प्रकृतवचने मयट्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
