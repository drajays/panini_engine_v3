"""
6.4.123  राधो हिंसायाम्  —  VIDHI

Padaccheda: राधः हिंसायाम्

राधो हिंसायाम् (6.4.123)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_123_rADo_123"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_123_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.123"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.123",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rADo hiMsAyAm",
    text_dev              = "राधो हिंसायाम्",
    padaccheda_dev        = "राधः हिंसायाम्",
    why_dev               = "(सूत्रम् 6.4.123) राधो हिंसायाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
