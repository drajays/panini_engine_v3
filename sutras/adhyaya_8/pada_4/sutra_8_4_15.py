"""
8.4.15  हिनुमीना  —  VIDHI

Padaccheda: हिनु (लुप्तषष्ठ्यन्तनिर्देशः) मीना (लुप्तषष्ठ्यन्तनिर्देशः)

हिनुमीना (8.4.15)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_15_hinumInA_15"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hinumInA",
    text_dev              = "हिनुमीना",
    padaccheda_dev        = "हिनु (लुप्तषष्ठ्यन्तनिर्देशः) मीना (लुप्तषष्ठ्यन्तनिर्देशः)",
    why_dev               = "(सूत्रम् 8.4.15) हिनुमीना।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
