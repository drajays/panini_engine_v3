"""
3.2.113  न यदि  —  VIDHI

Padaccheda: न यदि

krt-suffix rule: न यदि (113)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_113_na_113"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.113", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.113"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.113",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na yadi",
    text_dev              = "न यदि",
    padaccheda_dev        = "न यदि",
    why_dev               = "धातोः कृत्-प्रत्ययः [न यदि] विहितः (३.२.113)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
