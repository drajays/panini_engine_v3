"""
4.3.24  विभाषा पूर्वाह्णापराह्णाभ्याम्  —  VIDHI

Padaccheda: विभाषा पूर्वाह्ण-अपराह्णाभ्याम्

विभाषा पूर्वाह्णापराह्णाभ्याम् (4.3.24)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_24_viBAzA_24"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_24_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA pUrvAhRAparAhRAByAm",
    text_dev              = "विभाषा पूर्वाह्णापराह्णाभ्याम्",
    padaccheda_dev        = "विभाषा पूर्वाह्ण-अपराह्णाभ्याम्",
    why_dev               = "(सूत्रम् 4.3.24) विभाषा पूर्वाह्णापराह्णाभ्याम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
