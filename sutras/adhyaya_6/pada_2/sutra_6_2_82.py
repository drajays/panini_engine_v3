"""
6.2.82  दीर्घकाशतुषभ्राष्ट्रवटं जे  —  VIDHI

Padaccheda: दीर्घ-काश-तुष-भ्राष्ट्र-वटम् जे

दीर्घकाशतुषभ्राष्ट्रवटं जे (6.2.82)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_82_dIrGakASat_82"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_82_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.82"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.82",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dIrGakASatuzaBrAzwravawaM je",
    text_dev              = "दीर्घकाशतुषभ्राष्ट्रवटं जे",
    padaccheda_dev        = "दीर्घ-काश-तुष-भ्राष्ट्र-वटम् जे",
    why_dev               = "(सूत्रम् 6.2.82) दीर्घकाशतुषभ्राष्ट्रवटं जे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
