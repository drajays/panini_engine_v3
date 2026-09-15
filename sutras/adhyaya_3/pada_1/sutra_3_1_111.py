"""
3.1.111  ई च खनः  —  VIDHI

Padaccheda: ई (लुप्तप्रथमान्तनिर्देशः) च खनः

Krt suffix rule from dhatu: ई च खनः (111)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_111_I_111"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.111", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "I ca KanaH",
    text_dev              = "ई च खनः",
    padaccheda_dev        = "ई (लुप्तप्रथमान्तनिर्देशः) च खनः",
    why_dev               = "धातोः [ई च खनः]-प्रत्ययः विहितः (३.१.111)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
