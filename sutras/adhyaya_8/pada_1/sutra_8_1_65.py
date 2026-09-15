"""
8.1.65  एकान्याभ्यां समर्थाभ्याम्  —  VIDHI

Padaccheda: एक-अन्याभ्याम् समर्थाभ्याम्

एकान्याभ्यां समर्थाभ्याम् (8.1.65)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_65_ekAnyAByAM_65"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.65", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ekAnyAByAM samarTAByAm",
    text_dev              = "एकान्याभ्यां समर्थाभ्याम्",
    padaccheda_dev        = "एक-अन्याभ्याम् समर्थाभ्याम्",
    why_dev               = "(सूत्रम् 8.1.65) एकान्याभ्यां समर्थाभ्याम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
