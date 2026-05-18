"""
7.3.91  गुणोऽपृक्ते  —  VIDHI

Padaccheda: गुणः अपृक्ते

गुणोऽपृक्ते (7.3.91)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_91_guRopfkte_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_91_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "guRo'pfkte",
    text_dev              = "गुणोऽपृक्ते",
    padaccheda_dev        = "गुणः अपृक्ते",
    why_dev               = "(सूत्रम् 7.3.91) गुणोऽपृक्ते।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
