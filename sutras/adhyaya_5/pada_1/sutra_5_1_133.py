"""
5.1.133  द्वंद्वमनोज्ञादिभ्यश्च  —  VIDHI

Padaccheda: द्वन्द्व-मनोज्ञ-आदिभ्यः च

द्वंद्वमनोज्ञादिभ्यश्च (5.1.133)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_133_dvaMdvaman_133"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_133_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.133"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.133",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvaMdvamanojYAdiByaSca",
    text_dev              = "द्वंद्वमनोज्ञादिभ्यश्च",
    padaccheda_dev        = "द्वन्द्व-मनोज्ञ-आदिभ्यः च",
    why_dev               = "(सूत्रम् 5.1.133) द्वंद्वमनोज्ञादिभ्यश्च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
