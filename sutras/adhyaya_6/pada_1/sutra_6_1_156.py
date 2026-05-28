"""
6.1.156  कारस्करो वृक्षः  —  VIDHI

Padaccheda: कारस्करः वृक्षः

कारस्करो वृक्षः (6.1.156)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_156_kAraskaro_156"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_156_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.156"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.156",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kAraskaro vfkzaH",
    text_dev              = "कारस्करो वृक्षः",
    padaccheda_dev        = "कारस्करः वृक्षः",
    why_dev               = "(सूत्रम् 6.1.156) कारस्करो वृक्षः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
