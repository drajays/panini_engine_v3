"""
3.3.129  छन्दसि गत्यर्थेभ्यः  —  VIDHI

Padaccheda: छन्दसि गति-अर्थेभ्यः

krt-suffix rule: छन्दसि गत्यर्थेभ्यः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_129_Candasi_129"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_129_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.129"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.129",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Candasi gatyarTeByaH",
    text_dev              = "छन्दसि गत्यर्थेभ्यः",
    padaccheda_dev        = "छन्दसि गति-अर्थेभ्यः",
    why_dev               = "धातोः प्रत्ययः (३.3.129)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
