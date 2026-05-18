"""
3.2.105  छन्दसि लिट्  —  VIDHI

Padaccheda: छन्दसि लिट्

krt-suffix rule: छन्दसि लिट् (105)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_105_Candasi_105"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_105_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.105"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.105",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Candasi liw",
    text_dev              = "छन्दसि लिट्",
    padaccheda_dev        = "छन्दसि लिट्",
    why_dev               = "धातोः कृत्-प्रत्ययः [छन्दसि लिट्] विहितः (३.२.105)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
