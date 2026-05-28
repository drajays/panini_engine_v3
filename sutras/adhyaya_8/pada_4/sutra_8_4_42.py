"""
8.4.42  न पदान्ताट्टोरनाम्  —  VIDHI

Padaccheda: न · पदान्तात् · टोः · नाम्

न पदान्ताट्टोरनाम् (8.4.42)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_42_na_42"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na padAntAwworanAm",
    text_dev              = "न पदान्ताट्टोरनाम्",
    padaccheda_dev        = "न · पदान्तात् · टोः · नाम्",
    why_dev               = "(सूत्रम् 8.4.42) न पदान्ताट्टोरनाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
