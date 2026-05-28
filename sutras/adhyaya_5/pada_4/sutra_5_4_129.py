"""
5.4.129  प्रसम्भ्यां जानुनोर्ज्ञुः  —  VIDHI

Padaccheda: प्र-सम्भ्याम् जानुनोः ज्ञुः

प्रसम्भ्यां जानुनोर्ज्ञुः (5.4.129)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_129_prasamByAM_129"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.129", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.129"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.129",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prasamByAM jAnunorjYuH",
    text_dev              = "प्रसम्भ्यां जानुनोर्ज्ञुः",
    padaccheda_dev        = "प्र-सम्भ्याम् जानुनोः ज्ञुः",
    why_dev               = "(सूत्रम् 5.4.129) प्रसम्भ्यां जानुनोर्ज्ञुः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
