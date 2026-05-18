"""
3.2.31  उदि कूले रुजिवहोः  —  VIDHI

Padaccheda: उदि कूले रुजि-वहोः

krt-suffix rule: उदि कूले रुजिवहोः (31)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_31_udi_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_31_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udi kUle rujivahoH",
    text_dev              = "उदि कूले रुजिवहोः",
    padaccheda_dev        = "उदि कूले रुजि-वहोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [उदि कूले रुजिवहोः] विहितः (३.२.31)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
