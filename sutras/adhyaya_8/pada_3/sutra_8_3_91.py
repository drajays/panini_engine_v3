"""
8.3.91  कपिष्ठलो गोत्रे  —  VIDHI

Padaccheda: कपिष्ठलः गोत्रे

कपिष्ठलो गोत्रे (8.3.91)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_91_kapizWalo_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_91_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kapizWalo gotre",
    text_dev              = "कपिष्ठलो गोत्रे",
    padaccheda_dev        = "कपिष्ठलः गोत्रे",
    why_dev               = "(सूत्रम् 8.3.91) कपिष्ठलो गोत्रे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
