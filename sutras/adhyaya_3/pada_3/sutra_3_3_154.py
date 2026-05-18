"""
3.3.154  सम्भवानेऽलमिति चेत् सिद्धाप्रयोगे  —  VIDHI

Padaccheda: सम्भवाने अलम् इति चेत् सिद्ध-अप्रयोगे

krt-suffix rule: सम्भवानेऽलमिति चेत् सिद्धाप्रयोगे
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_154_samBavAne_154"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_154_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.154"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.154",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samBavAne'lamiti cet sidDAprayoge",
    text_dev              = "सम्भवानेऽलमिति चेत् सिद्धाप्रयोगे",
    padaccheda_dev        = "सम्भवाने अलम् इति चेत् सिद्ध-अप्रयोगे",
    why_dev               = "धातोः प्रत्ययः (३.3.154)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
