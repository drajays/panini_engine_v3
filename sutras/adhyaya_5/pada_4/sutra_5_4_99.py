"""
5.4.99  नावो द्विगोः  —  VIDHI

Padaccheda: नावः द्विगोः

नावो द्विगोः (5.4.99)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_99_nAvo_99"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_99_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nAvo dvigoH",
    text_dev              = "नावो द्विगोः",
    padaccheda_dev        = "नावः द्विगोः",
    why_dev               = "(सूत्रम् 5.4.99) नावो द्विगोः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
