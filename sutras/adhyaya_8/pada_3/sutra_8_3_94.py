"""
8.3.94  छन्दोनाम्नि च  —  VIDHI

Padaccheda: छन्दोनाम्नि च

छन्दोनाम्नि च (8.3.94)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_94_CandonAmni_94"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_94_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CandonAmni ca",
    text_dev              = "छन्दोनाम्नि च",
    padaccheda_dev        = "छन्दोनाम्नि च",
    why_dev               = "(सूत्रम् 8.3.94) छन्दोनाम्नि च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
