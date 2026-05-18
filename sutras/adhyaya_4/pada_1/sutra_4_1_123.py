"""
4.1.123  शुभ्रादिभ्यश्च  —  VIDHI

Padaccheda: शुभ्र-आदिभ्यः च

शुभ्रादिभ्यश्च (4.1.123)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_123_SuBrAdiBya_123"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_123_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.123"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.123",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SuBrAdiByaSca",
    text_dev              = "शुभ्रादिभ्यश्च",
    padaccheda_dev        = "शुभ्र-आदिभ्यः च",
    why_dev               = "(सूत्रम् 4.1.123) शुभ्रादिभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
