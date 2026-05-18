"""
8.1.13  अकृच्छ्रे प्रियसुखयोरन्यतरस्याम्  —  VIDHI

Padaccheda: अकृच्छ्रे प्रिय-सुखयोः अन्यतरस्याम्

अकृच्छ्रे प्रियसुखयोरन्यतरस्याम् (8.1.13)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_13_akfcCre_13"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_1_13_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "akfcCre priyasuKayoranyatarasyAm",
    text_dev              = "अकृच्छ्रे प्रियसुखयोरन्यतरस्याम्",
    padaccheda_dev        = "अकृच्छ्रे प्रिय-सुखयोः अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 8.1.13) अकृच्छ्रे प्रियसुखयोरन्यतरस्याम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
