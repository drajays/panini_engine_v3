"""
7.2.37  ग्रहोऽलिटि दीर्घः  —  VIDHI

Padaccheda: ग्रहः अ-लिटि दीर्घः

ग्रहोऽलिटि दीर्घः (7.2.37)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_37_graholiwi_37"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_37_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "graho'liwi dIrGaH",
    text_dev              = "ग्रहोऽलिटि दीर्घः",
    padaccheda_dev        = "ग्रहः अ-लिटि दीर्घः",
    why_dev               = "(सूत्रम् 7.2.37) ग्रहोऽलिटि दीर्घः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
