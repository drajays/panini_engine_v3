"""
3.2.187  ञीतः क्तः  —  VIDHI

Padaccheda: ञि-इतः क्तः

krt-suffix rule: ञीतः क्तः (187)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_187_YItaH_187"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.187", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.187"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.187",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "YItaH ktaH",
    text_dev              = "ञीतः क्तः",
    padaccheda_dev        = "ञि-इतः क्तः",
    why_dev               = "धातोः कृत्-प्रत्ययः [ञीतः क्तः] विहितः (३.२.187)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
