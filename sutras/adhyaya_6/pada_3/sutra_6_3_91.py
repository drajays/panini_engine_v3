"""
6.3.91  आ सर्वनाम्नः  —  VIDHI

Padaccheda: आ (लुप्तप्रथमान्तनिर्देशः) सर्वनाम्नः

आ सर्वनाम्नः (6.3.91)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_91_A_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_91_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "A sarvanAmnaH",
    text_dev              = "आ सर्वनाम्नः",
    padaccheda_dev        = "आ (लुप्तप्रथमान्तनिर्देशः) सर्वनाम्नः",
    why_dev               = "(सूत्रम् 6.3.91) आ सर्वनाम्नः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
