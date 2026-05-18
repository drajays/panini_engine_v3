"""
3.2.72  अवे यजः  —  VIDHI

Padaccheda: अवे यजः

krt-suffix rule: अवे यजः (72)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_72_ave_72"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_72_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ave yajaH",
    text_dev              = "अवे यजः",
    padaccheda_dev        = "अवे यजः",
    why_dev               = "धातोः कृत्-प्रत्ययः [अवे यजः] विहितः (३.२.72)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
