"""
3.3.135  नानद्यतनवत् क्रियाप्रबन्धसामीप्ययोः  —  VIDHI

Padaccheda: न अन्-अद्यतन-वत् क्रियाप्रबन्ध-सामीप्ययोः

krt-suffix rule: नानद्यतनवत् क्रियाप्रबन्धसामीप्ययोः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_135_nAnadyatan_135"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_135_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.135"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.135",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nAnadyatanavat kriyAprabanDasAmIpyayoH",
    text_dev              = "नानद्यतनवत् क्रियाप्रबन्धसामीप्ययोः",
    padaccheda_dev        = "न अन्-अद्यतन-वत् क्रियाप्रबन्ध-सामीप्ययोः",
    why_dev               = "धातोः प्रत्ययः (३.3.135)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
