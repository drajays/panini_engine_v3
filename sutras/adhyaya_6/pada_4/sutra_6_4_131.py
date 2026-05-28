"""
6.4.131  वसोः सम्प्रसारणम्  —  VIDHI

Padaccheda: वसोः सम्प्रसारणम्

वसोः सम्प्रसारणम् (6.4.131)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_131_vasoH_131"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.131", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.131"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.131",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vasoH samprasAraRam",
    text_dev              = "वसोः सम्प्रसारणम्",
    padaccheda_dev        = "वसोः सम्प्रसारणम्",
    why_dev               = "(सूत्रम् 6.4.131) वसोः सम्प्रसारणम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
