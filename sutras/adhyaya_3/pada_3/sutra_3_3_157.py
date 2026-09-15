"""
3.3.157  इच्छार्थेषु लिङ्लोटौ  —  VIDHI

Padaccheda: इच्छा-अर्थेषु लिङ्-लोटौ

krt-suffix rule: इच्छार्थेषु लिङ्लोटौ
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_157_icCArTezu_157"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.157", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.157"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.157",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "icCArTezu liNlowO",
    text_dev              = "इच्छार्थेषु लिङ्लोटौ",
    padaccheda_dev        = "इच्छा-अर्थेषु लिङ्-लोटौ",
    why_dev               = "धातोः प्रत्ययः (३.3.157)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
