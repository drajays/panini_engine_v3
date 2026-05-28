"""
8.2.91  ब्रूहिप्रेस्यश्रौषड्वौषडावहानामादेः  —  VIDHI

Padaccheda: ब्रूहि-प्रेष्य-श्रौषतट्-वौषट्-आवहानाम् आदेः

ब्रूहिप्रेस्यश्रौषड्वौषडावहानामादेः (8.2.91)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_91_brUhipresy_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "brUhipresyaSrOzaqvOzaqAvahAnAmAdeH",
    text_dev              = "ब्रूहिप्रेस्यश्रौषड्वौषडावहानामादेः",
    padaccheda_dev        = "ब्रूहि-प्रेष्य-श्रौषतट्-वौषट्-आवहानाम् आदेः",
    why_dev               = "(सूत्रम् 8.2.91) ब्रूहिप्रेस्यश्रौषड्वौषडावहानामादेः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
