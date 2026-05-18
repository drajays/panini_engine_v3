"""
7.4.91  रुग्रिकौ च लुकि  —  VIDHI

Padaccheda: रुक्-रिकौ च लुकि

रुग्रिकौ च लुकि (7.4.91)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_91_rugrikO_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_91_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rugrikO ca luki",
    text_dev              = "रुग्रिकौ च लुकि",
    padaccheda_dev        = "रुक्-रिकौ च लुकि",
    why_dev               = "(सूत्रम् 7.4.91) रुग्रिकौ च लुकि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
