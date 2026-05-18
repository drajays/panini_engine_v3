"""
6.2.22  पूर्वे भूतपूर्वे  —  VIDHI

Padaccheda: पूर्वे भूतपूर्वे

पूर्वे भूतपूर्वे (6.2.22)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_22_pUrve_22"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_22_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUrve BUtapUrve",
    text_dev              = "पूर्वे भूतपूर्वे",
    padaccheda_dev        = "पूर्वे भूतपूर्वे",
    why_dev               = "(सूत्रम् 6.2.22) पूर्वे भूतपूर्वे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
