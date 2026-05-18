"""
3.4.27  अन्यथैवंकथमित्थंसु सिद्धाप्रयोगश्चेत्  —  VIDHI

Padaccheda: अन्यथा-एवं-कथम्-इत्थंसु सिद्ध-अप्रयोगः चेत्

krt-suffix rule: अन्यथैवंकथमित्थंसु सिद्धाप्रयोगश्चेत्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_27_anyaTEvaMk_27"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_4_27_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anyaTEvaMkaTamitTaMsu sidDAprayogaScet",
    text_dev              = "अन्यथैवंकथमित्थंसु सिद्धाप्रयोगश्चेत्",
    padaccheda_dev        = "अन्यथा-एवं-कथम्-इत्थंसु सिद्ध-अप्रयोगः चेत्",
    why_dev               = "धातोः प्रत्ययः (३.4.27)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
