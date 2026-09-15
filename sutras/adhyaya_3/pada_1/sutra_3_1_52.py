"""
3.1.52  अस्यतिवक्तिख्यातिभ्यः अङ्  —  VIDHI

Padaccheda: अस्यति-वक्ति-ख्यातिभ्यः अङ्

Krt suffix rule from dhatu: अस्यतिवक्तिख्यातिभ्यः अङ् (52)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_52_asyativaktiK_52"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.52", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "asyativaktiKyAtiByaH aN",
    text_dev              = "अस्यतिवक्तिख्यातिभ्यः अङ्",
    padaccheda_dev        = "अस्यति-वक्ति-ख्यातिभ्यः अङ्",
    why_dev               = "धातोः [अस्यतिवक्तिख्यातिभ्यः अङ्]-प्रत्ययः विहितः (३.१.52)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
