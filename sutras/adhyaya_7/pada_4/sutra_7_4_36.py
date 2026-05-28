"""
7.4.36  दुरस्युर्द्रविणस्युर्वृषण्यतिरिषण्यति  —  VIDHI

Padaccheda: दुरस्युः द्रविणस्युः वृषण्यति (क्रियापदम्) रिषण्यति (क्रियापदम्)

दुरस्युर्द्रविणस्युर्वृषण्यतिरिषण्यति (7.4.36)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_36_durasyurdr_36"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.36", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "durasyurdraviRasyurvfzaRyatirizaRyati",
    text_dev              = "दुरस्युर्द्रविणस्युर्वृषण्यतिरिषण्यति",
    padaccheda_dev        = "दुरस्युः द्रविणस्युः वृषण्यति (क्रियापदम्) रिषण्यति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 7.4.36) दुरस्युर्द्रविणस्युर्वृषण्यतिरिषण्यति।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
