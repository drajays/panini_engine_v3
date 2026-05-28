"""
3.2.39  द्विषत्परयोस्तापेः  —  VIDHI

Padaccheda: द्विषत्-परयोः तापेः

krt-suffix rule: द्विषत्परयोस्तापेः (39)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_39_dvizatpara_39"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvizatparayostApeH",
    text_dev              = "द्विषत्परयोस्तापेः",
    padaccheda_dev        = "द्विषत्-परयोः तापेः",
    why_dev               = "धातोः कृत्-प्रत्ययः [द्विषत्परयोस्तापेः] विहितः (३.२.39)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
