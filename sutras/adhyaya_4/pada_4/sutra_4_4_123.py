"""
4.4.123  असुरस्य स्वम्  —  VIDHI

Padaccheda: असुरस्य स्वम्

असुरस्य स्वम् (4.4.123)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_123_asurasya_123"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_123_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.123"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.123",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "asurasya svam",
    text_dev              = "असुरस्य स्वम्",
    padaccheda_dev        = "असुरस्य स्वम्",
    why_dev               = "(सूत्रम् 4.4.123) असुरस्य स्वम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
