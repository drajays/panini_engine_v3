"""
3.2.128  पूङ्यजोः शानन्  —  VIDHI

Padaccheda: पूङ्-यजोः (पञ्चम्यर्थे षष्ठी) शानन्

krt-suffix rule: पूङ्यजोः शानन् (128)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_128_pUNyajoH_128"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.128", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.128"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.128",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUNyajoH SAnan",
    text_dev              = "पूङ्यजोः शानन्",
    padaccheda_dev        = "पूङ्-यजोः (पञ्चम्यर्थे षष्ठी) शानन्",
    why_dev               = "धातोः कृत्-प्रत्ययः [पूङ्यजोः शानन्] विहितः (३.२.128)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
