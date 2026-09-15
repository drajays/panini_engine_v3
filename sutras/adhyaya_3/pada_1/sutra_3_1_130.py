"""
3.1.130  क्रतौ कुण्डपाय्यसंचाय्यौ  —  VIDHI

Padaccheda: क्रतौ कुण्डपाय्य-संचाय्यौ

Krt suffix rule from dhatu: क्रतौ कुण्डपाय्यसंचाय्यौ (130)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_130_kratO_130"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.130", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.130"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.130",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kratO kuRqapAyyasaMcAyyO",
    text_dev              = "क्रतौ कुण्डपाय्यसंचाय्यौ",
    padaccheda_dev        = "क्रतौ कुण्डपाय्य-संचाय्यौ",
    why_dev               = "धातोः [क्रतौ कुण्डपाय्यसंचाय्यौ]-प्रत्ययः विहितः (३.१.130)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
