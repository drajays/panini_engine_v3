"""
8.3.26  हे मपरे वा  —  VIDHI

Padaccheda: हे म-परे वा

हे मपरे वा (8.3.26)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_26_he_26"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "he mapare vA",
    text_dev              = "हे मपरे वा",
    padaccheda_dev        = "हे म-परे वा",
    why_dev               = "(सूत्रम् 8.3.26) हे मपरे वा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
