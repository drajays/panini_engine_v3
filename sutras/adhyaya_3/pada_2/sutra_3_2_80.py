"""
3.2.80  व्रते  —  VIDHI

Padaccheda: व्रते

krt-suffix rule: व्रते (80)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_80_vrate_80"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.80", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vrate",
    text_dev              = "व्रते",
    padaccheda_dev        = "व्रते",
    why_dev               = "धातोः कृत्-प्रत्ययः [व्रते] विहितः (३.२.80)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
