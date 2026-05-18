"""
7.1.95  तृज्वत् क्रोष्टुः  —  VIDHI

Padaccheda: तृच्-वत् क्रोष्टुः

तृज्वत् क्रोष्टुः (7.1.95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_1_95_tfjvat_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_1_95_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tfjvat krozwuH",
    text_dev              = "तृज्वत् क्रोष्टुः",
    padaccheda_dev        = "तृच्-वत् क्रोष्टुः",
    why_dev               = "(सूत्रम् 7.1.95) तृज्वत् क्रोष्टुः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
