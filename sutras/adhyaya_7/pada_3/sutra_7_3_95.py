"""
7.3.95  तुरुस्तुशम्यमः सार्वधातुके  —  VIDHI

Padaccheda: तु-रु-स्तु-शम्-यमः सार्वधातुके

तुरुस्तुशम्यमः सार्वधातुके (7.3.95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_95_turustuSam_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_95_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "turustuSamyamaH sArvaDAtuke",
    text_dev              = "तुरुस्तुशम्यमः सार्वधातुके",
    padaccheda_dev        = "तु-रु-स्तु-शम्-यमः सार्वधातुके",
    why_dev               = "(सूत्रम् 7.3.95) तुरुस्तुशम्यमः सार्वधातुके।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
