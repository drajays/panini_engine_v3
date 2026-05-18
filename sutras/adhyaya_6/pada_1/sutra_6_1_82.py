"""
6.1.82  क्रय्यस्तदर्थे  —  VIDHI

Padaccheda: क्रय्यः तदर्थे

क्रय्यस्तदर्थे (6.1.82)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_82_krayyastad_82"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_82_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.82"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.82",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "krayyastadarTe",
    text_dev              = "क्रय्यस्तदर्थे",
    padaccheda_dev        = "क्रय्यः तदर्थे",
    why_dev               = "(सूत्रम् 6.1.82) क्रय्यस्तदर्थे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
