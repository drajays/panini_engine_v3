"""
2.3.30  षष्ठ्यतसर्थप्रत्ययेन  —  VIDHI

Padaccheda: षष्ठी अतस्-अर्थ-प्रत्ययेन

Sasthi with atas-artha pratyaya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import karaka_gate_eligible

_GATE_KEY: str = "2_3_30_atas_pratyaya"


def cond(state: State) -> bool:
    return karaka_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.30"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.30",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zazWyatasarTapratyayena",
    text_dev              = "षष्ठ्यतसर्थप्रत्ययेन",
    padaccheda_dev        = "षष्ठी अतस्-अर्थ-प्रत्ययेन",
    why_dev               = "अतस्-अर्थ-प्रत्ययेन षष्ठी (२.३.३०)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
