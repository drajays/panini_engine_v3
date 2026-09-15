"""
3.1.89  न दुहस्नुनमां यक्चिणौ  —  VIDHI

Padaccheda: न दुह-स्नु-नमाम् यक्-चिणौ

Krt suffix rule from dhatu: न दुहस्नुनमां यक्चिणौ (89)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_89_na_89"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.89", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.89"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.89",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na duhasnunamAM yakciRO",
    text_dev              = "न दुहस्नुनमां यक्चिणौ",
    padaccheda_dev        = "न दुह-स्नु-नमाम् यक्-चिणौ",
    why_dev               = "धातोः [न दुहस्नुनमां यक्चिणौ]-प्रत्ययः विहितः (३.१.89)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
