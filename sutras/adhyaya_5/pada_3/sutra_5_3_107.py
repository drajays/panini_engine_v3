"""
5.3.107  शर्कराऽऽदिभ्योऽण्  —  VIDHI

Padaccheda: शर्करा-आदिभ्यः अण्

शर्कराऽऽदिभ्योऽण् (5.3.107)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_107_SarkarAd_107"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_107_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.107"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SarkarA''diByo'R",
    text_dev              = "शर्कराऽऽदिभ्योऽण्",
    padaccheda_dev        = "शर्करा-आदिभ्यः अण्",
    why_dev               = "(सूत्रम् 5.3.107) शर्कराऽऽदिभ्योऽण्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
