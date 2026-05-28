"""
3.3.103  गुरोश्च हलः  —  VIDHI

Padaccheda: गुरोः च हलः

krt-suffix rule: गुरोश्च हलः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_103_guroSca_103"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "guroSca halaH",
    text_dev              = "गुरोश्च हलः",
    padaccheda_dev        = "गुरोः च हलः",
    why_dev               = "धातोः प्रत्ययः (३.3.103)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
