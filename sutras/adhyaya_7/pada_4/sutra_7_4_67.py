"""
7.4.67  द्युतिस्वाप्योः सम्प्रसारणम्  —  VIDHI

Padaccheda: द्युति-स्वाप्योः सम्प्रसारणम्

द्युतिस्वाप्योः सम्प्रसारणम् (7.4.67)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_67_dyutisvApy_67"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_67_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dyutisvApyoH samprasAraRam",
    text_dev              = "द्युतिस्वाप्योः सम्प्रसारणम्",
    padaccheda_dev        = "द्युति-स्वाप्योः सम्प्रसारणम्",
    why_dev               = "(सूत्रम् 7.4.67) द्युतिस्वाप्योः सम्प्रसारणम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
