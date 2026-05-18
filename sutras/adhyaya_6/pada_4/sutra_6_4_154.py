"""
6.4.154  तुरिष्ठेमेयस्सु  —  VIDHI

Padaccheda: तुः इष्ठ-इमा-ईयस्सु

तुरिष्ठेमेयस्सु (6.4.154)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_154_turizWemey_154"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_154_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.154"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.154",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "turizWemeyassu",
    text_dev              = "तुरिष्ठेमेयस्सु",
    padaccheda_dev        = "तुः इष्ठ-इमा-ईयस्सु",
    why_dev               = "(सूत्रम् 6.4.154) तुरिष्ठेमेयस्सु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
