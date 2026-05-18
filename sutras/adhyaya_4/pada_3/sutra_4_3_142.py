"""
4.3.142  शम्याष्ट्लञ्  —  VIDHI

Padaccheda: शम्याः ष्लञ्

शम्याष्ट्लञ् (4.3.142)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_142_SamyAzwlaY_142"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_142_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.142"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.142",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SamyAzwlaY",
    text_dev              = "शम्याष्ट्लञ्",
    padaccheda_dev        = "शम्याः ष्लञ्",
    why_dev               = "(सूत्रम् 4.3.142) शम्याष्ट्लञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
