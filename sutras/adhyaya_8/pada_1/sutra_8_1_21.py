"""
8.1.21  बहुवचने वस्नसौ  —  VIDHI

Padaccheda: बहुवचनस्य वस्-नसौ

बहुवचने वस्नसौ (8.1.21)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_21_bahuvacane_21"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_1_21_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahuvacane vasnasO",
    text_dev              = "बहुवचने वस्नसौ",
    padaccheda_dev        = "बहुवचनस्य वस्-नसौ",
    why_dev               = "(सूत्रम् 8.1.21) बहुवचने वस्नसौ।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
