"""
3.3.145  अनवकॢप्त्यमर्षयोरकिंवृत्ते अपि  —  VIDHI

Padaccheda: अनवकॢप्ति-अमर्षयोः अ-किंवृत्ते अपि

krt-suffix rule: अनवकॢप्त्यमर्षयोरकिंवृत्ते अपि
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_145_anavakxpty_145"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_145_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.145"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.145",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anavakxptyamarzayorakiMvftte api",
    text_dev              = "अनवकॢप्त्यमर्षयोरकिंवृत्ते अपि",
    padaccheda_dev        = "अनवकॢप्ति-अमर्षयोः अ-किंवृत्ते अपि",
    why_dev               = "धातोः प्रत्ययः (३.3.145)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
