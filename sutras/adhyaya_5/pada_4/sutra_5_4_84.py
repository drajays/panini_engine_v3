"""
5.4.84  द्विस्तावा त्रिस्तावा वेदिः  —  VIDHI

Padaccheda: द्विस्तावा त्रिस्तावा वेदिः

द्विस्तावा त्रिस्तावा वेदिः (5.4.84)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_84_dvistAvA_84"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_84_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.84"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.84",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvistAvA tristAvA vediH",
    text_dev              = "द्विस्तावा त्रिस्तावा वेदिः",
    padaccheda_dev        = "द्विस्तावा त्रिस्तावा वेदिः",
    why_dev               = "(सूत्रम् 5.4.84) द्विस्तावा त्रिस्तावा वेदिः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
