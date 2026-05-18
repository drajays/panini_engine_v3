"""
8.1.12  प्रकारे गुणवचनस्य  —  VIDHI

Padaccheda: प्रकारे गुणवचनस्य

प्रकारे गुणवचनस्य (8.1.12)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_12_prakAre_12"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_1_12_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.12"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prakAre guRavacanasya",
    text_dev              = "प्रकारे गुणवचनस्य",
    padaccheda_dev        = "प्रकारे गुणवचनस्य",
    why_dev               = "(सूत्रम् 8.1.12) प्रकारे गुणवचनस्य।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
