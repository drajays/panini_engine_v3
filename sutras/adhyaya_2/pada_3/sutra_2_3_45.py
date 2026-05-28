"""
2.3.45  नक्षत्रे च लुपि  —  VIDHI

Padaccheda: नक्षत्रे च लुपि

Nakshatra with lup also takes saptami.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_45_naksatra_lupi"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("2_3_45_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.45"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nakzatre ca lupi",
    text_dev              = "नक्षत्रे च लुपि",
    padaccheda_dev        = "नक्षत्रे च लुपि",
    why_dev               = "नक्षत्रे च लुपि (२.३.४५)।",
    anuvritti_from        = ('2.3.36',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
