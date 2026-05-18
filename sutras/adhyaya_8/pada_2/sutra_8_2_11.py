"""
8.2.11  संज्ञायाम्  —  VIDHI

Padaccheda: संज्ञायाम्

संज्ञायाम् (8.2.11)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_11_saMjYAyAm_11"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_11_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.11"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.11",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAm",
    text_dev              = "संज्ञायाम्",
    padaccheda_dev        = "संज्ञायाम्",
    why_dev               = "(सूत्रम् 8.2.11) संज्ञायाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
