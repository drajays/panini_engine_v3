"""
6.1.23  स्त्यः प्रपूर्वस्य  —  VIDHI

Padaccheda: स्त्यः प्र-पूर्वस्य

स्त्यः प्रपूर्वस्य (6.1.23)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_23_styaH_23"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "styaH prapUrvasya",
    text_dev              = "स्त्यः प्रपूर्वस्य",
    padaccheda_dev        = "स्त्यः प्र-पूर्वस्य",
    why_dev               = "(सूत्रम् 6.1.23) स्त्यः प्रपूर्वस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
