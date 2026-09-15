"""
3.2.138  भुवश्च  —  VIDHI

Padaccheda: भुवः च

krt-suffix rule: भुवश्च (138)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_138_BuvaSca_138"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.138", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.138"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.138",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BuvaSca",
    text_dev              = "भुवश्च",
    padaccheda_dev        = "भुवः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [भुवश्च] विहितः (३.२.138)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
