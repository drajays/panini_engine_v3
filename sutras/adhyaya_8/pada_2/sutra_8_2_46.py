"""
8.2.46  क्षियो दीर्घात्  —  VIDHI

Padaccheda: क्षियः दीर्घात्

क्षियो दीर्घात् (8.2.46)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_46_kziyo_46"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_46_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kziyo dIrGAt",
    text_dev              = "क्षियो दीर्घात्",
    padaccheda_dev        = "क्षियः दीर्घात्",
    why_dev               = "(सूत्रम् 8.2.46) क्षियो दीर्घात्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
