"""
3.2.49  आशिषि हनः  —  VIDHI

Padaccheda: आशिषि हनः

krt-suffix rule: आशिषि हनः (49)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_49_ASizi_49"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ASizi hanaH",
    text_dev              = "आशिषि हनः",
    padaccheda_dev        = "आशिषि हनः",
    why_dev               = "धातोः कृत्-प्रत्ययः [आशिषि हनः] विहितः (३.२.49)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
