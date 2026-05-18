"""
7.4.96  विभाषा वेष्टिचेष्ट्योः  —  VIDHI

Padaccheda: विभाषा वेष्टि-चेष्ट्योः

विभाषा वेष्टिचेष्ट्योः (7.4.96)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_96_viBAzA_96"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_96_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.96"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA vezwicezwyoH",
    text_dev              = "विभाषा वेष्टिचेष्ट्योः",
    padaccheda_dev        = "विभाषा वेष्टि-चेष्ट्योः",
    why_dev               = "(सूत्रम् 7.4.96) विभाषा वेष्टिचेष्ट्योः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
