"""
4.1.174  ते तद्राजाः  —  VIDHI

Padaccheda: ते तद्राजाः

ते तद्राजाः (4.1.174)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_174_te_174"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_174_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.174"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.174",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "te tadrAjAH",
    text_dev              = "ते तद्राजाः",
    padaccheda_dev        = "ते तद्राजाः",
    why_dev               = "(सूत्रम् 4.1.174) ते तद्राजाः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
