"""
8.3.35  शर्परे विसर्जनीयः  —  VIDHI

Padaccheda: शर्परे । विसर्जनीयः

शर्परे विसर्जनीयः (8.3.35)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_35_Sarpare_35"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_35_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Sarpare visarjanIyaH",
    text_dev              = "शर्परे विसर्जनीयः",
    padaccheda_dev        = "शर्परे । विसर्जनीयः",
    why_dev               = "(सूत्रम् 8.3.35) शर्परे विसर्जनीयः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
