"""
3.1.19  नमोवरिवश्चित्रङः क्यच्  —  VIDHI

Padaccheda: नमो-वरिवस्-चित्रङः क्यच्

Krt suffix rule from dhatu: नमोवरिवश्चित्रङः क्यच् (19)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_19_namovarivaSc_19"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.19", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.19",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "namovarivaScitraNaH kyac",
    text_dev              = "नमोवरिवश्चित्रङः क्यच्",
    padaccheda_dev        = "नमो-वरिवस्-चित्रङः क्यच्",
    why_dev               = "धातोः [नमोवरिवश्चित्रङः क्यच्]-प्रत्ययः विहितः (३.१.19)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
