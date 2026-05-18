"""
6.4.68  वाऽन्यस्य संयोगादेः  —  VIDHI

Padaccheda: वा अन्यस्य संयोग-आदेः

वाऽन्यस्य संयोगादेः (6.4.68)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_68_vAnyasya_68"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_68_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA'nyasya saMyogAdeH",
    text_dev              = "वाऽन्यस्य संयोगादेः",
    padaccheda_dev        = "वा अन्यस्य संयोग-आदेः",
    why_dev               = "(सूत्रम् 6.4.68) वाऽन्यस्य संयोगादेः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
