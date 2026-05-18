"""
3.4.6  छन्दसि लुङ्लङ्लिटः  —  VIDHI

Padaccheda: छन्दसि लुङ्-लङ्-लिटः

krt-suffix rule: छन्दसि लुङ्लङ्लिटः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_6_Candasi_6"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_4_6_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.6"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Candasi luNlaNliwaH",
    text_dev              = "छन्दसि लुङ्लङ्लिटः",
    padaccheda_dev        = "छन्दसि लुङ्-लङ्-लिटः",
    why_dev               = "धातोः प्रत्ययः (३.4.6)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
