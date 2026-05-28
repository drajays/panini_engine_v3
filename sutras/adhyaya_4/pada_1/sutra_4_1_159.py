"""
4.1.159  पुत्रान्तादन्यतरस्याम्  —  VIDHI

Padaccheda: पुत्र-अन्तात् अन्यतरस्याम्

पुत्रान्तादन्यतरस्याम् (4.1.159)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_159_putrAntAda_159"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.159", state, "4.1.92"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.159"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.159",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "putrAntAdanyatarasyAm",
    text_dev              = "पुत्रान्तादन्यतरस्याम्",
    padaccheda_dev        = "पुत्र-अन्तात् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 4.1.159) पुत्रान्तादन्यतरस्याम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
