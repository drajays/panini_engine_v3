"""
6.3.50  हृदयस्य हृल्लेखयदण्लासेषु  —  VIDHI

Padaccheda: हृदयस्य हृत् लेख-यत्-अण्-लासेषु

हृदयस्य हृल्लेखयदण्लासेषु (6.3.50)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_50_hfdayasya_50"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hfdayasya hflleKayadaRlAsezu",
    text_dev              = "हृदयस्य हृल्लेखयदण्लासेषु",
    padaccheda_dev        = "हृदयस्य हृत् लेख-यत्-अण्-लासेषु",
    why_dev               = "(सूत्रम् 6.3.50) हृदयस्य हृल्लेखयदण्लासेषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
