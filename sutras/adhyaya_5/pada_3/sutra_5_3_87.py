"""
5.3.87  संज्ञायां कन्  —  VIDHI

Padaccheda: संज्ञायाम् कन्

संज्ञायां कन् (5.3.87)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_87_saMjYAyAM_87"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_87_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.87"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAM kan",
    text_dev              = "संज्ञायां कन्",
    padaccheda_dev        = "संज्ञायाम् कन्",
    why_dev               = "(सूत्रम् 5.3.87) संज्ञायां कन्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
