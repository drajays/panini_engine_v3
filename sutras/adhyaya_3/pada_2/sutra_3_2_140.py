"""
3.2.140  त्रसिगृधिधृषिक्षिपेः क्नुः  —  VIDHI

Padaccheda: त्रसि- गृधि-धृषि-क्षिपेः क्नुः

krt-suffix rule: त्रसिगृधिधृषिक्षिपेः क्नुः (140)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_140_trasigfDiD_140"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.140", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.140"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.140",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "trasigfDiDfzikzipeH knuH",
    text_dev              = "त्रसिगृधिधृषिक्षिपेः क्नुः",
    padaccheda_dev        = "त्रसि- गृधि-धृषि-क्षिपेः क्नुः",
    why_dev               = "धातोः कृत्-प्रत्ययः [त्रसिगृधिधृषिक्षिपेः क्नुः] विहितः (३.२.140)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
