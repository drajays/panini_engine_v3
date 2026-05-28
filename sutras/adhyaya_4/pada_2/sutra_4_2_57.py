"""
4.2.57  तदस्यां प्रहरणमिति क्रीडायाम् णः  —  VIDHI

Padaccheda: तत् अस्याम् प्रहरणम् इति क्रीडायाम् णः

तदस्यां प्रहरणमिति क्रीडायाम् णः (4.2.57)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_57_tadasyAM_57"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.57", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadasyAM praharaRamiti krIqAyAm RaH",
    text_dev              = "तदस्यां प्रहरणमिति क्रीडायाम् णः",
    padaccheda_dev        = "तत् अस्याम् प्रहरणम् इति क्रीडायाम् णः",
    why_dev               = "(सूत्रम् 4.2.57) तदस्यां प्रहरणमिति क्रीडायाम् णः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
