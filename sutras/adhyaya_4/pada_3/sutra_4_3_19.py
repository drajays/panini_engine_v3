"""
4.3.19  छन्दसि ठञ्  —  VIDHI

Padaccheda: छन्दसि ठञ्

छन्दसि ठञ् (4.3.19)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_19_Candasi_19"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_19_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.19",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Candasi WaY",
    text_dev              = "छन्दसि ठञ्",
    padaccheda_dev        = "छन्दसि ठञ्",
    why_dev               = "(सूत्रम् 4.3.19) छन्दसि ठञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
