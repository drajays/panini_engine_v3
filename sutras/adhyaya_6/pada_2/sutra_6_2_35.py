"""
6.2.35  संख्या  —  VIDHI

Padaccheda: संख्या

संख्या (6.2.35)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_35_saMKyA_35"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_35_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMKyA",
    text_dev              = "संख्या",
    padaccheda_dev        = "संख्या",
    why_dev               = "(सूत्रम् 6.2.35) संख्या।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
