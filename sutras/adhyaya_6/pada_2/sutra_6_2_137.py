"""
6.2.137  प्रकृत्या भगालम्  —  VIDHI

Padaccheda: प्रकृत्या भगालम्

प्रकृत्या भगालम् (6.2.137)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_137_prakftyA_137"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.137"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.137",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prakftyA BagAlam",
    text_dev              = "प्रकृत्या भगालम्",
    padaccheda_dev        = "प्रकृत्या भगालम्",
    why_dev               = "(सूत्रम् 6.2.137) प्रकृत्या भगालम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
