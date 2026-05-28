"""
8.3.39  इणः षः  —  VIDHI

Padaccheda: इणः · षः

इणः षः (8.3.39)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_39_iRaH_39"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "iRaH zaH",
    text_dev              = "इणः षः",
    padaccheda_dev        = "इणः · षः",
    why_dev               = "(सूत्रम् 8.3.39) इणः षः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
