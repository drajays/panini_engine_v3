"""
3.1.109  एतिस्तुशस्वृदृजुषः क्यप्  —  VIDHI

Padaccheda: एति-स्तु-शास्-वृ-दृ-जुषः क्यप्

Krt suffix rule from dhatu: एतिस्तुशस्वृदृजुषः क्यप् (109)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_109_etistuSasvfd_109"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.109", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.109"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.109",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "etistuSasvfdfjuzaH kyap",
    text_dev              = "एतिस्तुशस्वृदृजुषः क्यप्",
    padaccheda_dev        = "एति-स्तु-शास्-वृ-दृ-जुषः क्यप्",
    why_dev               = "धातोः [एतिस्तुशस्वृदृजुषः क्यप्]-प्रत्ययः विहितः (३.१.109)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
