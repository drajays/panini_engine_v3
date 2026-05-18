"""
7.1.68  न सुदुर्भ्यां केवलाभ्याम्  —  VIDHI

Padaccheda: न सु-दुर्भ्याम् केवलाभ्याम्

न सुदुर्भ्यां केवलाभ्याम् (7.1.68)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_1_68_na_68"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_1_68_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na sudurByAM kevalAByAm",
    text_dev              = "न सुदुर्भ्यां केवलाभ्याम्",
    padaccheda_dev        = "न सु-दुर्भ्याम् केवलाभ्याम्",
    why_dev               = "(सूत्रम् 7.1.68) न सुदुर्भ्यां केवलाभ्याम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
