"""
3.1.6  मान्बधदान्शान्भ्यो दीर्घश्चाभ्यासस्य  —  VIDHI

Padaccheda: मान्-बध-दान्-शान्भ्यः दीर्घः च अभ्यासस्य

Krt suffix rule from dhatu: मान्बधदान्शान्भ्यो दीर्घश्चाभ्यासस्य (6)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_6_mAnbaDadAnSA_6"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.6", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.6"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mAnbaDadAnSAnByo dIrGaScAByAsasya",
    text_dev              = "मान्बधदान्शान्भ्यो दीर्घश्चाभ्यासस्य",
    padaccheda_dev        = "मान्-बध-दान्-शान्भ्यः दीर्घः च अभ्यासस्य",
    why_dev               = "धातोः [मान्बधदान्शान्भ्यो दीर्घश्चाभ्यासस्य]-प्रत्ययः विहितः (३.१.6)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
