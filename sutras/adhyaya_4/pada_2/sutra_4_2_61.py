"""
4.2.61  क्रमादिभ्यो वुन्  —  VIDHI

Padaccheda: क्रम-आदिभ्यः वुन्

क्रमादिभ्यो वुन् (4.2.61)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_61_kramAdiByo_61"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_61_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kramAdiByo vun",
    text_dev              = "क्रमादिभ्यो वुन्",
    padaccheda_dev        = "क्रम-आदिभ्यः वुन्",
    why_dev               = "(सूत्रम् 4.2.61) क्रमादिभ्यो वुन्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
