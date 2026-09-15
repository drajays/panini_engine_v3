"""
3.2.145  प्रे लपसृद्रुमथवदवसः  —  VIDHI

Padaccheda: प्रे लप-सृ-द्रु-मथ-वद-वसः

krt-suffix rule: प्रे लपसृद्रुमथवदवसः (145)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_145_pre_145"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.145", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.145"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.145",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pre lapasfdrumaTavadavasaH",
    text_dev              = "प्रे लपसृद्रुमथवदवसः",
    padaccheda_dev        = "प्रे लप-सृ-द्रु-मथ-वद-वसः",
    why_dev               = "धातोः कृत्-प्रत्ययः [प्रे लपसृद्रुमथवदवसः] विहितः (३.२.145)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
