"""
3.2.35  विध्वरुषोः तुदः  —  VIDHI

Padaccheda: विधु-अरुषोः तुदः

krt-suffix rule: विध्वरुषोः तुदः (35)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_35_viDvaruzoH_35"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.35", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viDvaruzoH tudaH",
    text_dev              = "विध्वरुषोः तुदः",
    padaccheda_dev        = "विधु-अरुषोः तुदः",
    why_dev               = "धातोः कृत्-प्रत्ययः [विध्वरुषोः तुदः] विहितः (३.२.35)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
