"""
8.2.3  न मु ने  —  VIDHI

Padaccheda: न मु (लुप्तप्रथमान्तनिर्देशः) ने

न मु ने (8.2.3)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_3_na_3"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_3_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.3"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na mu ne",
    text_dev              = "न मु ने",
    padaccheda_dev        = "न मु (लुप्तप्रथमान्तनिर्देशः) ने",
    why_dev               = "(सूत्रम् 8.2.3) न मु ने।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
