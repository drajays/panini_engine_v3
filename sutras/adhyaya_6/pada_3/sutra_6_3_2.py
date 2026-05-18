"""
6.3.2  पञ्चम्याः स्तोकादिभ्यः  —  VIDHI

Padaccheda: पञ्चम्याः स्तोक-आदिभ्यः

पञ्चम्याः स्तोकादिभ्यः (6.3.2)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_2_paYcamyAH_2"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_2_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.2"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.2",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paYcamyAH stokAdiByaH",
    text_dev              = "पञ्चम्याः स्तोकादिभ्यः",
    padaccheda_dev        = "पञ्चम्याः स्तोक-आदिभ्यः",
    why_dev               = "(सूत्रम् 6.3.2) पञ्चम्याः स्तोकादिभ्यः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
