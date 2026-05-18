"""
5.3.60  प्रशस्यस्य श्रः  —  VIDHI

Padaccheda: प्रशस्यस्य श्रः

प्रशस्यस्य श्रः (5.3.60)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_60_praSasyasy_60"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_60_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "praSasyasya SraH",
    text_dev              = "प्रशस्यस्य श्रः",
    padaccheda_dev        = "प्रशस्यस्य श्रः",
    why_dev               = "(सूत्रम् 5.3.60) प्रशस्यस्य श्रः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
