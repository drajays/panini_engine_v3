"""
8.3.22  हलि सर्वेषाम्  —  VIDHI

Padaccheda: हलि · सर्वेषाम्

हलि सर्वेषाम् (8.3.22)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_22_hali_22"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_22_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hali sarvezAm",
    text_dev              = "हलि सर्वेषाम्",
    padaccheda_dev        = "हलि · सर्वेषाम्",
    why_dev               = "(सूत्रम् 8.3.22) हलि सर्वेषाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
