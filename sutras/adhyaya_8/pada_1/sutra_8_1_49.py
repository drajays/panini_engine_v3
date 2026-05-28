"""
8.1.49  आहो उताहो चानन्तरम्  —  VIDHI

Padaccheda: आहो उताहो च अनन्तरम्

आहो उताहो चानन्तरम् (8.1.49)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_49_Aho_49"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Aho utAho cAnantaram",
    text_dev              = "आहो उताहो चानन्तरम्",
    padaccheda_dev        = "आहो उताहो च अनन्तरम्",
    why_dev               = "(सूत्रम् 8.1.49) आहो उताहो चानन्तरम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
