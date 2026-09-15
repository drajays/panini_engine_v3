"""
3.2.180  विप्रसम्भ्यो ड्वसंज्ञायाम्  —  VIDHI

Padaccheda: वि-प्-रसम्भ्यः डु असंज्ञायाम्

krt-suffix rule: विप्रसम्भ्यो ड्वसंज्ञायाम् (180)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_180_viprasamBy_180"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.180", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.180"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.180",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viprasamByo qvasaMjYAyAm",
    text_dev              = "विप्रसम्भ्यो ड्वसंज्ञायाम्",
    padaccheda_dev        = "वि-प्-रसम्भ्यः डु असंज्ञायाम्",
    why_dev               = "धातोः कृत्-प्रत्ययः [विप्रसम्भ्यो ड्वसंज्ञायाम्] विहितः (३.२.180)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
