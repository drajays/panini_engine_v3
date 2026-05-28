"""
3.2.7  समि ख्यः  —  VIDHI

Padaccheda: समि ख्यः

krt-suffix rule: समि ख्यः (7)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_7_sami_7"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_2_7_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sami KyaH",
    text_dev              = "समि ख्यः",
    padaccheda_dev        = "समि ख्यः",
    why_dev               = "धातोः कृत्-प्रत्ययः [समि ख्यः] विहितः (३.२.7)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
