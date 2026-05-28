"""
6.1.146  आस्पदं प्रतिष्ठायाम्  —  VIDHI

Padaccheda: आस्पदम् प्रतिष्ठायाम्

आस्पदं प्रतिष्ठायाम् (6.1.146)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_146_AspadaM_146"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_146_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.146"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.146",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AspadaM pratizWAyAm",
    text_dev              = "आस्पदं प्रतिष्ठायाम्",
    padaccheda_dev        = "आस्पदम् प्रतिष्ठायाम्",
    why_dev               = "(सूत्रम् 6.1.146) आस्पदं प्रतिष्ठायाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
