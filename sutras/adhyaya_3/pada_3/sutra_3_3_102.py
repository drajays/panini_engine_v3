"""
3.3.102  अ प्रत्ययात्  —  VIDHI

Padaccheda: अ (लुप्तप्रथमान्तनिर्देशः) प्रत्ययात्

krt-suffix rule: अ प्रत्ययात्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_102_a_102"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_102_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.102"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.102",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "a pratyayAt",
    text_dev              = "अ प्रत्ययात्",
    padaccheda_dev        = "अ (लुप्तप्रथमान्तनिर्देशः) प्रत्ययात्",
    why_dev               = "धातोः प्रत्ययः (३.3.102)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
