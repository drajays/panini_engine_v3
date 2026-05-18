"""
3.1.115  भिद्योद्ध्यौ नदे  —  VIDHI

Padaccheda: भिद्य-उद्ध्यौ नदे

Krt suffix rule from dhatu: भिद्योद्ध्यौ नदे (115)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_115_BidyodDyO_115"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_115_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.115"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.115",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BidyodDyO nade",
    text_dev              = "भिद्योद्ध्यौ नदे",
    padaccheda_dev        = "भिद्य-उद्ध्यौ नदे",
    why_dev               = "धातोः [भिद्योद्ध्यौ नदे]-प्रत्ययः विहितः (३.१.115)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
