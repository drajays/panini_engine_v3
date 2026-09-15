"""
3.1.144  गेहे कः  —  VIDHI

Padaccheda: गेहे कः

Krt suffix rule from dhatu: गेहे कः (144)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_144_gehe_144"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.144", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.144"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.144",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gehe kaH",
    text_dev              = "गेहे कः",
    padaccheda_dev        = "गेहे कः",
    why_dev               = "धातोः [गेहे कः]-प्रत्ययः विहितः (३.१.144)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
