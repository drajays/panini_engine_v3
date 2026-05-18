"""
6.1.13  ष्यङः सम्प्रसारणं पुत्रपत्योस्तत्पुरुषे  —  VIDHI

Padaccheda: ष्यङः सम्प्रसारणम् पुत्र-पत्योः तत्पुरुषे

ष्यङः सम्प्रसारणं पुत्रपत्योस्तत्पुरुषे (6.1.13)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_13_zyaNaH_13"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_13_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zyaNaH samprasAraRaM putrapatyostatpuruze",
    text_dev              = "ष्यङः सम्प्रसारणं पुत्रपत्योस्तत्पुरुषे",
    padaccheda_dev        = "ष्यङः सम्प्रसारणम् पुत्र-पत्योः तत्पुरुषे",
    why_dev               = "(सूत्रम् 6.1.13) ष्यङः सम्प्रसारणं पुत्रपत्योस्तत्पुरुषे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
