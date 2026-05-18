"""
5.4.125  जम्भा सुहरिततृणसोमेभ्यः  —  VIDHI

Padaccheda: जम्भा सु-हरित-तृण-सोमेभ्यः

जम्भा सुहरिततृणसोमेभ्यः (5.4.125)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_125_jamBA_125"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_125_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.125"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jamBA suharitatfRasomeByaH",
    text_dev              = "जम्भा सुहरिततृणसोमेभ्यः",
    padaccheda_dev        = "जम्भा सु-हरित-तृण-सोमेभ्यः",
    why_dev               = "(सूत्रम् 5.4.125) जम्भा सुहरिततृणसोमेभ्यः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
