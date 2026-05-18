"""
4.1.112  शिवादिभ्योऽण्  —  VIDHI

Padaccheda: शिव-आदिभ्यः अण्

शिवादिभ्योऽण् (4.1.112)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_112_SivAdiByo_112"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_112_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.112"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.112",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SivAdiByo'R",
    text_dev              = "शिवादिभ्योऽण्",
    padaccheda_dev        = "शिव-आदिभ्यः अण्",
    why_dev               = "(सूत्रम् 4.1.112) शिवादिभ्योऽण्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
