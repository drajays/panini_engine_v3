"""
3.3.29  उन्न्योर्ग्रः  —  VIDHI

Padaccheda: उत्-न्योः ग्रः

krt-suffix rule: उन्न्योर्ग्रः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_29_unnyorgraH_29"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_29_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "unnyorgraH",
    text_dev              = "उन्न्योर्ग्रः",
    padaccheda_dev        = "उत्-न्योः ग्रः",
    why_dev               = "धातोः प्रत्ययः (३.3.29)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
