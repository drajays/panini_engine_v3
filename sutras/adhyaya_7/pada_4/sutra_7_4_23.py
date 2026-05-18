"""
7.4.23  उपसर्गाद्ध्रस्व ऊहतेः  —  VIDHI

Padaccheda: उपसर्गात् ह्रस्वः ऊहतेः

उपसर्गाद्ध्रस्व ऊहतेः (7.4.23)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_23_upasargAdD_23"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_23_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasargAdDrasva UhateH",
    text_dev              = "उपसर्गाद्ध्रस्व ऊहतेः",
    padaccheda_dev        = "उपसर्गात् ह्रस्वः ऊहतेः",
    why_dev               = "(सूत्रम् 7.4.23) उपसर्गाद्ध्रस्व ऊहतेः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
