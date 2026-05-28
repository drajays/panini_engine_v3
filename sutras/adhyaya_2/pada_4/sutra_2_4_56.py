"""
2.4.56  अजेर्व्यघञपोः  —  VIDHI

Padaccheda: अजेः वी (लुप्तप्रथमान्तनिर्देशः) अ-घञ्-अपोः

aj root replaced by vi except with ghan and ap.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_56_ajeh_vi"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.56", state, "2.4.35")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ajervyaGaYapoH",
    text_dev              = "अजेर्व्यघञपोः",
    padaccheda_dev        = "अजेः वी (लुप्तप्रथमान्तनिर्देशः) अ-घञ्-अपोः",
    why_dev               = "अजेः वी अ-घञ्-अपोः (२.४.५६)।",
    anuvritti_from        = ('2.4.40',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
