"""
5.1.114  आकालिकडाद्यन्तवचने  —  VIDHI

Padaccheda: आकालिकट् आद्यन्तवचने

आकालिकडाद्यन्तवचने (5.1.114)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_114_AkAlikaqAd_114"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_114_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.114"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.114",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AkAlikaqAdyantavacane",
    text_dev              = "आकालिकडाद्यन्तवचने",
    padaccheda_dev        = "आकालिकट् आद्यन्तवचने",
    why_dev               = "(सूत्रम् 5.1.114) आकालिकडाद्यन्तवचने।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
