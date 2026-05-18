"""
3.2.156  प्रजोरिनिः  —  VIDHI

Padaccheda: प्र-जोः इनिः

krt-suffix rule: प्रजोरिनिः (156)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_156_prajoriniH_156"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_156_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.156"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.156",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prajoriniH",
    text_dev              = "प्रजोरिनिः",
    padaccheda_dev        = "प्र-जोः इनिः",
    why_dev               = "धातोः कृत्-प्रत्ययः [प्रजोरिनिः] विहितः (३.२.156)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
