"""
6.2.166  व्यवायिनोऽन्तरम्  —  VIDHI

Padaccheda: व्यवायिनः अन्तरम्

व्यवायिनोऽन्तरम् (6.2.166)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_166_vyavAyino_166"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.166"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.166",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vyavAyino'ntaram",
    text_dev              = "व्यवायिनोऽन्तरम्",
    padaccheda_dev        = "व्यवायिनः अन्तरम्",
    why_dev               = "(सूत्रम् 6.2.166) व्यवायिनोऽन्तरम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
