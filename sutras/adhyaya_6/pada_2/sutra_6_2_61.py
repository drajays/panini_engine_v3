"""
6.2.61  क्ते नित्यार्थे  —  VIDHI

Padaccheda: क्ते नित्य-अर्थे

क्ते नित्यार्थे (6.2.61)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_61_kte_61"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kte nityArTe",
    text_dev              = "क्ते नित्यार्थे",
    padaccheda_dev        = "क्ते नित्य-अर्थे",
    why_dev               = "(सूत्रम् 6.2.61) क्ते नित्यार्थे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
