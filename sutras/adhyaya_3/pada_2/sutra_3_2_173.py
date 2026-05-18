"""
3.2.173  शॄवन्द्योरारुः  —  VIDHI

Padaccheda: शॄ-वन्द्योः आरुः

krt-suffix rule: शॄवन्द्योरारुः (173)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_173_SFvandyorA_173"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_173_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.173"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.173",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SFvandyorAruH",
    text_dev              = "शॄवन्द्योरारुः",
    padaccheda_dev        = "शॄ-वन्द्योः आरुः",
    why_dev               = "धातोः कृत्-प्रत्ययः [शॄवन्द्योरारुः] विहितः (३.२.173)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
