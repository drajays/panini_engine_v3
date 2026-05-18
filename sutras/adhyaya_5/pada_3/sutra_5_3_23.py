"""
5.3.23  प्रकारवचने थाल्  —  VIDHI

Padaccheda: प्रकारवचने थाल्

प्रकारवचने थाल् (5.3.23)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_23_prakAravac_23"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_23_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prakAravacane TAl",
    text_dev              = "प्रकारवचने थाल्",
    padaccheda_dev        = "प्रकारवचने थाल्",
    why_dev               = "(सूत्रम् 5.3.23) प्रकारवचने थाल्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
