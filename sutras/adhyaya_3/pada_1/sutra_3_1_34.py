"""
3.1.34  सिब्बहुलं लेटि  —  VIDHI

Padaccheda: सिप् बहुलम् लेटि

Krt suffix rule from dhatu: सिब्बहुलं लेटि (34)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_34_sibbahulaM_34"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.34", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sibbahulaM lewi",
    text_dev              = "सिब्बहुलं लेटि",
    padaccheda_dev        = "सिप् बहुलम् लेटि",
    why_dev               = "धातोः [सिब्बहुलं लेटि]-प्रत्ययः विहितः (३.१.34)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
