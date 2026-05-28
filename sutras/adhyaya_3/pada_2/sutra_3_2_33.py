"""
3.2.33  परिमाणे पचः  —  VIDHI

Padaccheda: परिमाणे पचः

krt-suffix rule: परिमाणे पचः (33)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_33_parimARe_33"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "parimARe pacaH",
    text_dev              = "परिमाणे पचः",
    padaccheda_dev        = "परिमाणे पचः",
    why_dev               = "धातोः कृत्-प्रत्ययः [परिमाणे पचः] विहितः (३.२.33)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
