"""
6.3.111  ढ्रलोपे पूर्वस्य दीर्घोऽणः  —  VIDHI

Padaccheda: ढ्-र-लोपे पूर्वस्य दीर्घः अणः

ढ्रलोपे पूर्वस्य दीर्घोऽणः (6.3.111)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_111_Qralope_111"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_111_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Qralope pUrvasya dIrGo'RaH",
    text_dev              = "ढ्रलोपे पूर्वस्य दीर्घोऽणः",
    padaccheda_dev        = "ढ्-र-लोपे पूर्वस्य दीर्घः अणः",
    why_dev               = "(सूत्रम् 6.3.111) ढ्रलोपे पूर्वस्य दीर्घोऽणः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
