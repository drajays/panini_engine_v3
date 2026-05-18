"""
8.4.7  अह्नोऽदन्तात्  —  VIDHI

Padaccheda: अह्नः (षष्ठीस्थाने प्रथमा) अत्-अन्तात्

अह्नोऽदन्तात् (8.4.7)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_7_ahnodantA_7"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_4_7_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ahno'dantAt",
    text_dev              = "अह्नोऽदन्तात्",
    padaccheda_dev        = "अह्नः (षष्ठीस्थाने प्रथमा) अत्-अन्तात्",
    why_dev               = "(सूत्रम् 8.4.7) अह्नोऽदन्तात्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
