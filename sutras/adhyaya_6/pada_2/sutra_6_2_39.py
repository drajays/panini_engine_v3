"""
6.2.39  क्षुल्लकश्च वैश्वदेवे  —  VIDHI

Padaccheda: क्षुल्लकः च वैश्वदेवे

क्षुल्लकश्च वैश्वदेवे (6.2.39)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_39_kzullakaSc_39"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_39_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kzullakaSca vESvadeve",
    text_dev              = "क्षुल्लकश्च वैश्वदेवे",
    padaccheda_dev        = "क्षुल्लकः च वैश्वदेवे",
    why_dev               = "(सूत्रम् 6.2.39) क्षुल्लकश्च वैश्वदेवे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
