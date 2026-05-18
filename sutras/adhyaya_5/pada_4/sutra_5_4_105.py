"""
5.4.105  कुमहद्भ्यामन्यतरस्याम्  —  VIDHI

Padaccheda: कु-महद्‍भ्याम् अन्यतरस्याम्

कुमहद्भ्यामन्यतरस्याम् (5.4.105)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_105_kumahadByA_105"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_105_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.105"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.105",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kumahadByAmanyatarasyAm",
    text_dev              = "कुमहद्भ्यामन्यतरस्याम्",
    padaccheda_dev        = "कु-महद्‍भ्याम् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 5.4.105) कुमहद्भ्यामन्यतरस्याम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
