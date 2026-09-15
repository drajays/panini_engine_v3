"""
3.2.92  कर्मण्यग्न्याख्यायाम्  —  VIDHI

Padaccheda: कर्मणि अग्नि-आख्यायाम्

krt-suffix rule: कर्मण्यग्न्याख्यायाम् (92)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_92_karmaRyagn_92"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.92", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.92"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.92",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaRyagnyAKyAyAm",
    text_dev              = "कर्मण्यग्न्याख्यायाम्",
    padaccheda_dev        = "कर्मणि अग्नि-आख्यायाम्",
    why_dev               = "धातोः कृत्-प्रत्ययः [कर्मण्यग्न्याख्यायाम्] विहितः (३.२.92)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
