"""
2.3.42  पञ्चमी विभक्ते  —  VIDHI

Padaccheda: पञ्चमी विभक्ते

Pancami marks the separated/distinguished item.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_42_vibhakte_pancami"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paYcamI viBakte",
    text_dev              = "पञ्चमी विभक्ते",
    padaccheda_dev        = "पञ्चमी विभक्ते",
    why_dev               = "विभक्ते पञ्चमी (२.३.४२)।",
    anuvritti_from        = ('2.3.28',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
