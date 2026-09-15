"""
3.1.54  आत्मनेपदेष्वन्यतरस्याम्  —  VIDHI

Padaccheda: आत्मनेपदेषु अन्यतरस्याम्

Krt suffix rule from dhatu: आत्मनेपदेष्वन्यतरस्याम् (54)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_54_Atmanepadezv_54"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.54", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AtmanepadezvanyatarasyAm",
    text_dev              = "आत्मनेपदेष्वन्यतरस्याम्",
    padaccheda_dev        = "आत्मनेपदेषु अन्यतरस्याम्",
    why_dev               = "धातोः [आत्मनेपदेष्वन्यतरस्याम्]-प्रत्ययः विहितः (३.१.54)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
