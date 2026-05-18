"""
2.4.42  हनो वध लिङि  —  VIDHI

Padaccheda: हनः वध (लुप्तप्रथमान्तनिर्देशः) लिङि

han root is replaced by vadha in lin.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_42_hana_vadha_lingi"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_42_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hano vaDa liNi",
    text_dev              = "हनो वध लिङि",
    padaccheda_dev        = "हनः वध (लुप्तप्रथमान्तनिर्देशः) लिङि",
    why_dev               = "हनः वध लिङि (२.४.४२)।",
    anuvritti_from        = ('2.4.40',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
