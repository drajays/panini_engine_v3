"""
6.1.172  अष्टनो दीर्घात्  —  VIDHI

Padaccheda: अष्टनः दीर्घात्

अष्टनो दीर्घात् (6.1.172)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_172_azwano_172"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_172_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.172"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.172",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "azwano dIrGAt",
    text_dev              = "अष्टनो दीर्घात्",
    padaccheda_dev        = "अष्टनः दीर्घात्",
    why_dev               = "(सूत्रम् 6.1.172) अष्टनो दीर्घात्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
