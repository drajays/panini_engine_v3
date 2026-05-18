"""
3.2.36  असूर्यललाटयोर्दृशितपोः  —  VIDHI

Padaccheda: असूर्य-ललाटयोः दृशि-तपोः

krt-suffix rule: असूर्यललाटयोर्दृशितपोः (36)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_36_asUryalalA_36"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_36_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "asUryalalAwayordfSitapoH",
    text_dev              = "असूर्यललाटयोर्दृशितपोः",
    padaccheda_dev        = "असूर्य-ललाटयोः दृशि-तपोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [असूर्यललाटयोर्दृशितपोः] विहितः (३.२.36)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
