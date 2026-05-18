"""
6.2.138  शितेर्नित्याबह्वज्बहुव्रीहावभसत्  —  VIDHI

Padaccheda: शितेः नित्य-अ-बहु-अच् बहुव्रीहौ अभसत्

शितेर्नित्याबह्वज्बहुव्रीहावभसत् (6.2.138)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_138_SiternityA_138"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_138_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.138"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.138",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SiternityAbahvajbahuvrIhAvaBasat",
    text_dev              = "शितेर्नित्याबह्वज्बहुव्रीहावभसत्",
    padaccheda_dev        = "शितेः नित्य-अ-बहु-अच् बहुव्रीहौ अभसत्",
    why_dev               = "(सूत्रम् 6.2.138) शितेर्नित्याबह्वज्बहुव्रीहावभसत्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
