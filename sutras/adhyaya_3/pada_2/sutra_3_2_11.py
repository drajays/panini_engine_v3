"""
3.2.11  आङि ताच्छील्ये  —  VIDHI

Padaccheda: आङि ताच्छील्ये

krt-suffix rule: आङि ताच्छील्ये (11)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_11_ANi_11"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_2_11_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.11"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.11",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ANi tAcCIlye",
    text_dev              = "आङि ताच्छील्ये",
    padaccheda_dev        = "आङि ताच्छील्ये",
    why_dev               = "धातोः कृत्-प्रत्ययः [आङि ताच्छील्ये] विहितः (३.२.11)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
