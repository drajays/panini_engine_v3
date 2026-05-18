"""
5.1.97  व्युष्टादिभ्योऽण्  —  VIDHI

Padaccheda: व्युष्ट-आदिभ्यः अण्

व्युष्टादिभ्योऽण् (5.1.97)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_97_vyuzwAdiBy_97"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_97_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.97"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.97",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vyuzwAdiByo'R",
    text_dev              = "व्युष्टादिभ्योऽण्",
    padaccheda_dev        = "व्युष्ट-आदिभ्यः अण्",
    why_dev               = "(सूत्रम् 5.1.97) व्युष्टादिभ्योऽण्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
