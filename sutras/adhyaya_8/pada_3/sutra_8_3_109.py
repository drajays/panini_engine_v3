"""
8.3.109  सहेः पृतनर्ताभ्यां च  —  VIDHI

Padaccheda: सहेः पृतना-ऋताभ्याम् च

सहेः पृतनर्ताभ्यां च (8.3.109)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_109_saheH_109"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.109", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.109"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.109",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saheH pftanartAByAM ca",
    text_dev              = "सहेः पृतनर्ताभ्यां च",
    padaccheda_dev        = "सहेः पृतना-ऋताभ्याम् च",
    why_dev               = "(सूत्रम् 8.3.109) सहेः पृतनर्ताभ्यां च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
