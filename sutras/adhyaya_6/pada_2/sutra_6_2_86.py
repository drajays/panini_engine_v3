"""
6.2.86  छात्र्यादयः शालायाम्  —  VIDHI

Padaccheda: छात्रि-आदयः शालायाम्

छात्र्यादयः शालायाम् (6.2.86)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_86_CAtryAdaya_86"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.86"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CAtryAdayaH SAlAyAm",
    text_dev              = "छात्र्यादयः शालायाम्",
    padaccheda_dev        = "छात्रि-आदयः शालायाम्",
    why_dev               = "(सूत्रम् 6.2.86) छात्र्यादयः शालायाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
