"""
8.3.28  ङ्णोः कुक्टुक् शरि  —  VIDHI

Padaccheda: ङ्‍-णोः कुक्-ट्टुक् शरि

ङ्णोः कुक्टुक् शरि (8.3.28)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_28_NRoH_28"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_28_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "NRoH kukwuk Sari",
    text_dev              = "ङ्णोः कुक्टुक् शरि",
    padaccheda_dev        = "ङ्‍-णोः कुक्-ट्टुक् शरि",
    why_dev               = "(सूत्रम् 8.3.28) ङ्णोः कुक्टुक् शरि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
