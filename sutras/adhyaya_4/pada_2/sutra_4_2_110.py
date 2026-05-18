"""
4.2.110  प्रस्थोत्तरपदपलद्यादिकोपधादण्  —  VIDHI

Padaccheda: प्रस्थ-उत्तरपद-पलद्य-आदि-क-उपधात् अण्

प्रस्थोत्तरपदपलद्यादिकोपधादण् (4.2.110)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_110_prasTottar_110"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_110_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.110"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.110",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prasTottarapadapaladyAdikopaDAdaR",
    text_dev              = "प्रस्थोत्तरपदपलद्यादिकोपधादण्",
    padaccheda_dev        = "प्रस्थ-उत्तरपद-पलद्य-आदि-क-उपधात् अण्",
    why_dev               = "(सूत्रम् 4.2.110) प्रस्थोत्तरपदपलद्यादिकोपधादण्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
