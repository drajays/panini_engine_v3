"""
4.3.157  उष्ट्राद्वुञ्  —  VIDHI

Padaccheda: उष्ट्रात् वुञ्

उष्ट्राद्वुञ् (4.3.157)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_157_uzwrAdvuY_157"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_157_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.157"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.157",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uzwrAdvuY",
    text_dev              = "उष्ट्राद्वुञ्",
    padaccheda_dev        = "उष्ट्रात् वुञ्",
    why_dev               = "(सूत्रम् 4.3.157) उष्ट्राद्वुञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
