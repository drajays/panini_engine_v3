"""
6.1.32  ह्वः सम्प्रसारणम्  —  VIDHI

Padaccheda: ह्वः सम्प्रसारणम्

ह्वः सम्प्रसारणम् (6.1.32)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_32_hvaH_32"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_32_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hvaH samprasAraRam",
    text_dev              = "ह्वः सम्प्रसारणम्",
    padaccheda_dev        = "ह्वः सम्प्रसारणम्",
    why_dev               = "(सूत्रम् 6.1.32) ह्वः सम्प्रसारणम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
