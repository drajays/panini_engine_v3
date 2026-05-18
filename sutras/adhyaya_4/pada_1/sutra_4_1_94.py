"""
4.1.94  गोत्राद्यून्यस्त्रियाम्  —  VIDHI

Padaccheda: गोत्रात् यूनि अ-स्त्रियाम्

गोत्राद्यून्यस्त्रियाम् (4.1.94)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_94_gotrAdyUny_94"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_94_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gotrAdyUnyastriyAm",
    text_dev              = "गोत्राद्यून्यस्त्रियाम्",
    padaccheda_dev        = "गोत्रात् यूनि अ-स्त्रियाम्",
    why_dev               = "(सूत्रम् 4.1.94) गोत्राद्यून्यस्त्रियाम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
