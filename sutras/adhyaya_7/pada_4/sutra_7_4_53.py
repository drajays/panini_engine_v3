"""
7.4.53  यीवर्णयोर्दीधीवेव्योः  —  VIDHI

Padaccheda: यि-इवर्णयोः दीधी-वेव्योः

यीवर्णयोर्दीधीवेव्योः (7.4.53)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_53_yIvarRayor_53"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_53_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yIvarRayordIDIvevyoH",
    text_dev              = "यीवर्णयोर्दीधीवेव्योः",
    padaccheda_dev        = "यि-इवर्णयोः दीधी-वेव्योः",
    why_dev               = "(सूत्रम् 7.4.53) यीवर्णयोर्दीधीवेव्योः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
