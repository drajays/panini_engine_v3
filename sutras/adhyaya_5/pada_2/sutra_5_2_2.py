"""
5.2.2  व्रीहिशाल्योर्ढक्  —  VIDHI

Padaccheda: व्रीहि-शाल्योः ढक्

व्रीहिशाल्योर्ढक् (5.2.2)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_2_vrIhiSAlyo_2"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_2_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.2"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.2",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vrIhiSAlyorQak",
    text_dev              = "व्रीहिशाल्योर्ढक्",
    padaccheda_dev        = "व्रीहि-शाल्योः ढक्",
    why_dev               = "(सूत्रम् 5.2.2) व्रीहिशाल्योर्ढक्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
