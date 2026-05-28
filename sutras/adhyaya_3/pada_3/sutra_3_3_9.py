"""
3.3.9  लिङ् चोर्ध्वमौहूर्तिके  —  VIDHI

Padaccheda: लिङ् च ऊर्ध्व-मौहूर्तिके

krt-suffix rule: लिङ् चोर्ध्वमौहूर्तिके
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_9_liN_9"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_9_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "liN corDvamOhUrtike",
    text_dev              = "लिङ् चोर्ध्वमौहूर्तिके",
    padaccheda_dev        = "लिङ् च ऊर्ध्व-मौहूर्तिके",
    why_dev               = "धातोः प्रत्ययः (३.3.9)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
