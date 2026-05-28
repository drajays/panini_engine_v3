"""
2.4.54  चक्षिङः ख्याञ्  —  VIDHI

Padaccheda: चक्षिङः ख्याञ्

caksin is replaced by khyan.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_54_caksin_khyan"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.54", state, "2.4.35")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "cakziNaH KyAY",
    text_dev              = "चक्षिङः ख्याञ्",
    padaccheda_dev        = "चक्षिङः ख्याञ्",
    why_dev               = "चक्षिङः ख्याञ् (२.४.५४)।",
    anuvritti_from        = ('2.4.40',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
