"""
2.2.32  द्वंद्वे घि  —  VIDHI

Padaccheda: द्वन्द्वे घि

In dvandva compound ghi-samjna applies.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_32_dvandva_ghi"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_2_32_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["dvandva_kind"]             = "2.2.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvaMdve Gi",
    text_dev              = "द्वंद्वे घि",
    padaccheda_dev        = "द्वन्द्वे घि",
    why_dev               = "द्वन्द्वे घि-संज्ञा (२.२.३२)।",
    anuvritti_from        = ('2.2.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
