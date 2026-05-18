"""
6.4.159  इष्ठस्य यिट् च  —  VIDHI

Padaccheda: इष्ठस्य यिट् च

इष्ठस्य यिट् च (6.4.159)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_159_izWasya_159"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_159_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.159"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.159",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "izWasya yiw ca",
    text_dev              = "इष्ठस्य यिट् च",
    padaccheda_dev        = "इष्ठस्य यिट् च",
    why_dev               = "(सूत्रम् 6.4.159) इष्ठस्य यिट् च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
