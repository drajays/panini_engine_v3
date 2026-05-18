"""
5.3.95  अवक्षेपणे कन्  —  VIDHI

Padaccheda: अवक्षेपणे कन्

अवक्षेपणे कन् (5.3.95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_95_avakzepaRe_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_95_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avakzepaRe kan",
    text_dev              = "अवक्षेपणे कन्",
    padaccheda_dev        = "अवक्षेपणे कन्",
    why_dev               = "(सूत्रम् 5.3.95) अवक्षेपणे कन्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
