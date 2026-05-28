"""
3.3.31  यज्ञे समि स्तुवः  —  VIDHI

Padaccheda: यज्ञे समि स्तुवः

krt-suffix rule: यज्ञे समि स्तुवः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_31_yajYe_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_31_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yajYe sami stuvaH",
    text_dev              = "यज्ञे समि स्तुवः",
    padaccheda_dev        = "यज्ञे समि स्तुवः",
    why_dev               = "धातोः प्रत्ययः (३.3.31)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
