"""
6.3.112  सहिवहोरोदवर्णस्य  —  VIDHI

Padaccheda: सहि-वहोः ओत् अ-वर्णस्य

सहिवहोरोदवर्णस्य (6.3.112)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_112_sahivahoro_112"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_112_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.112"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.112",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sahivahorodavarRasya",
    text_dev              = "सहिवहोरोदवर्णस्य",
    padaccheda_dev        = "सहि-वहोः ओत् अ-वर्णस्य",
    why_dev               = "(सूत्रम् 6.3.112) सहिवहोरोदवर्णस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
