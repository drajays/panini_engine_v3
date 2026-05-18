"""
6.4.125  फणां च सप्तानाम्  —  VIDHI

Padaccheda: फणाम् च सप्तानाम्

फणां च सप्तानाम् (6.4.125)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_125_PaRAM_125"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_125_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.125"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "PaRAM ca saptAnAm",
    text_dev              = "फणां च सप्तानाम्",
    padaccheda_dev        = "फणाम् च सप्तानाम्",
    why_dev               = "(सूत्रम् 6.4.125) फणां च सप्तानाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
