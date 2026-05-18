"""
5.4.143  स्त्रियां संज्ञायाम्  —  VIDHI

Padaccheda: स्त्रियाम् संज्ञायाम्

स्त्रियां संज्ञायाम् (5.4.143)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_143_striyAM_143"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_143_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.143"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.143",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "striyAM saMjYAyAm",
    text_dev              = "स्त्रियां संज्ञायाम्",
    padaccheda_dev        = "स्त्रियाम् संज्ञायाम्",
    why_dev               = "(सूत्रम् 5.4.143) स्त्रियां संज्ञायाम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
