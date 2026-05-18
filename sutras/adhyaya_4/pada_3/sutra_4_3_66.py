"""
4.3.66  तस्य व्याख्यान इति च व्याख्यातव्यनाम्नः  —  VIDHI

Padaccheda: तस्य व्याख्याने इति च व्याख्यातव्यनाम्नः

तस्य व्याख्यान इति च व्याख्यातव्यनाम्नः (4.3.66)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_66_tasya_66"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_66_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tasya vyAKyAna iti ca vyAKyAtavyanAmnaH",
    text_dev              = "तस्य व्याख्यान इति च व्याख्यातव्यनाम्नः",
    padaccheda_dev        = "तस्य व्याख्याने इति च व्याख्यातव्यनाम्नः",
    why_dev               = "(सूत्रम् 4.3.66) तस्य व्याख्यान इति च व्याख्यातव्यनाम्नः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
