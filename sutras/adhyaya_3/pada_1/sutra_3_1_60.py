"""
3.1.60  चिण् ते पदः  —  VIDHI

Padaccheda: चिण् ते पदः

Krt suffix rule from dhatu: चिण् ते पदः (60)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_60_ciR_60"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_60_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ciR te padaH",
    text_dev              = "चिण् ते पदः",
    padaccheda_dev        = "चिण् ते पदः",
    why_dev               = "धातोः [चिण् ते पदः]-प्रत्ययः विहितः (३.१.60)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
