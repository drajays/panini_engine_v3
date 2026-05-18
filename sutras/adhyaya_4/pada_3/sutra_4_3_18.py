"""
4.3.18  वर्षाभ्यष्ठक्  —  VIDHI

Padaccheda: वर्षाभ्यः ठक्

वर्षाभ्यष्ठक् (4.3.18)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_18_varzAByazW_18"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_18_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "varzAByazWak",
    text_dev              = "वर्षाभ्यष्ठक्",
    padaccheda_dev        = "वर्षाभ्यः ठक्",
    why_dev               = "(सूत्रम् 4.3.18) वर्षाभ्यष्ठक्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
