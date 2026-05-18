"""
3.3.155  विभाषा धातौ सम्भावनवचनेऽयदि  —  VIDHI

Padaccheda: विभाषा धातौ सम्भावनवचने अ-यदि

krt-suffix rule: विभाषा धातौ सम्भावनवचनेऽयदि
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_155_viBAzA_155"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_155_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.155"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.155",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA DAtO samBAvanavacane'yadi",
    text_dev              = "विभाषा धातौ सम्भावनवचनेऽयदि",
    padaccheda_dev        = "विभाषा धातौ सम्भावनवचने अ-यदि",
    why_dev               = "धातोः प्रत्ययः (३.3.155)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
