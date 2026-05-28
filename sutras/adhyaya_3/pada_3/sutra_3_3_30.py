"""
3.3.30  कॄ धान्ये  —  VIDHI

Padaccheda: कॄ (लुप्तपञ्चम्यन्तनिर्देशः) धान्ये

krt-suffix rule: कॄ धान्ये
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_30_kF_30"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.30"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.30",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kF DAnye",
    text_dev              = "कॄ धान्ये",
    padaccheda_dev        = "कॄ (लुप्तपञ्चम्यन्तनिर्देशः) धान्ये",
    why_dev               = "धातोः प्रत्ययः (३.3.30)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
