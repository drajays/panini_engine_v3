"""
3.2.50  अपे क्लेशतमसोः  —  VIDHI

Padaccheda: अपे क्लेश-तमसोः

krt-suffix rule: अपे क्लेशतमसोः (50)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_50_ape_50"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.50", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ape kleSatamasoH",
    text_dev              = "अपे क्लेशतमसोः",
    padaccheda_dev        = "अपे क्लेश-तमसोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [अपे क्लेशतमसोः] विहितः (३.२.50)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
