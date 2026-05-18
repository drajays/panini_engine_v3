"""
8.4.26  छन्दस्यृदवग्रहात्  —  VIDHI

Padaccheda: छन्दसि ऋत्-अवग्रहात्

छन्दस्यृदवग्रहात् (8.4.26)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_26_Candasyfda_26"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_4_26_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CandasyfdavagrahAt",
    text_dev              = "छन्दस्यृदवग्रहात्",
    padaccheda_dev        = "छन्दसि ऋत्-अवग्रहात्",
    why_dev               = "(सूत्रम् 8.4.26) छन्दस्यृदवग्रहात्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
