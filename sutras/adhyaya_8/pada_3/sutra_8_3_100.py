"""
8.3.100  नक्षत्राद्वा  —  VIDHI

Padaccheda: नक्षत्रात् वा

नक्षत्राद्वा (8.3.100)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_100_nakzatrAdv_100"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.100"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nakzatrAdvA",
    text_dev              = "नक्षत्राद्वा",
    padaccheda_dev        = "नक्षत्रात् वा",
    why_dev               = "(सूत्रम् 8.3.100) नक्षत्राद्वा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
