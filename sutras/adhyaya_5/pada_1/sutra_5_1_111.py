"""
5.1.111  अनुप्रवचनादिभ्यश्छः  —  VIDHI

Padaccheda: अनुप्रवचन-आदिभ्यः छः

अनुप्रवचनादिभ्यश्छः (5.1.111)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_111_anupravaca_111"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_111_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anupravacanAdiByaSCaH",
    text_dev              = "अनुप्रवचनादिभ्यश्छः",
    padaccheda_dev        = "अनुप्रवचन-आदिभ्यः छः",
    why_dev               = "(सूत्रम् 5.1.111) अनुप्रवचनादिभ्यश्छः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
