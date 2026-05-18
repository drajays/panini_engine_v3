"""
5.2.61  विमुक्तादिभ्योऽण्  —  VIDHI

Padaccheda: विमुक्तादिभ्यः अण्

विमुक्तादिभ्योऽण् (5.2.61)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_61_vimuktAdiB_61"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_61_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vimuktAdiByo'R",
    text_dev              = "विमुक्तादिभ्योऽण्",
    padaccheda_dev        = "विमुक्तादिभ्यः अण्",
    why_dev               = "(सूत्रम् 5.2.61) विमुक्तादिभ्योऽण्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
