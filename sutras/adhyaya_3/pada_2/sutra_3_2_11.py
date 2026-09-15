"""
3.2.11  आङि ताच्छील्ये  —  VIDHI

Padaccheda: आङि ताच्छील्ये

krt-suffix rule: आङि ताच्छील्ये (11)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_11_ANi_11"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.11", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.11"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.11",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ANi tAcCIlye",
    text_dev              = "आङि ताच्छील्ये",
    padaccheda_dev        = "आङि ताच्छील्ये",
    why_dev               = "धातोः कृत्-प्रत्ययः [आङि ताच्छील्ये] विहितः (३.२.11)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
