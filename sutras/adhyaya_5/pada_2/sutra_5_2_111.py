"""
5.2.111  काण्डाण्डादीरन्नीरचौ  —  VIDHI

Padaccheda: काण्ड-अण्डात् ईरन्-ईरचौ

काण्डाण्डादीरन्नीरचौ (5.2.111)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_111_kARqARqAdI_111"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_111_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kARqARqAdIrannIracO",
    text_dev              = "काण्डाण्डादीरन्नीरचौ",
    padaccheda_dev        = "काण्ड-अण्डात् ईरन्-ईरचौ",
    why_dev               = "(सूत्रम् 5.2.111) काण्डाण्डादीरन्नीरचौ।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
