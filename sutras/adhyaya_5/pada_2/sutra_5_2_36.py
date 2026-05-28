"""
5.2.36  तदस्य संजातं तारकाऽऽदिभ्य इतच्  —  VIDHI

Padaccheda: तत् अस्य संजातम् तारका-आदिभ्यः इतच्

तदस्य संजातं तारकाऽऽदिभ्य इतच् (5.2.36)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_36_tadasya_36"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.36", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadasya saMjAtaM tArakA''diBya itac",
    text_dev              = "तदस्य संजातं तारकाऽऽदिभ्य इतच्",
    padaccheda_dev        = "तत् अस्य संजातम् तारका-आदिभ्यः इतच्",
    why_dev               = "(सूत्रम् 5.2.36) तदस्य संजातं तारकाऽऽदिभ्य इतच्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
