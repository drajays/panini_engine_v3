"""
8.3.6  पुमः खय्यम्परे  —  VIDHI

Padaccheda: पुमः खयि अम्-परे

पुमः खय्यम्परे (8.3.6)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_6_pumaH_6"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.6"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pumaH Kayyampare",
    text_dev              = "पुमः खय्यम्परे",
    padaccheda_dev        = "पुमः खयि अम्-परे",
    why_dev               = "(सूत्रम् 8.3.6) पुमः खय्यम्परे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
