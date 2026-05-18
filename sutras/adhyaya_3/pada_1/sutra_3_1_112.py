"""
3.1.112  भृञोऽसंज्ञायाम्  —  VIDHI

Padaccheda: भृञः अ-संज्ञायाम्

Krt suffix rule from dhatu: भृञोऽसंज्ञायाम् (112)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_112_BfYosaMjYAy_112"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_112_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.112"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.112",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BfYo'saMjYAyAm",
    text_dev              = "भृञोऽसंज्ञायाम्",
    padaccheda_dev        = "भृञः अ-संज्ञायाम्",
    why_dev               = "धातोः [भृञोऽसंज्ञायाम्]-प्रत्ययः विहितः (३.१.112)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
