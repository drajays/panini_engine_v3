"""
6.3.87  तीर्थे ये  —  VIDHI

Padaccheda: तीर्थे ये

तीर्थे ये (6.3.87)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_87_tIrTe_87"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.87"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tIrTe ye",
    text_dev              = "तीर्थे ये",
    padaccheda_dev        = "तीर्थे ये",
    why_dev               = "(सूत्रम् 6.3.87) तीर्थे ये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
