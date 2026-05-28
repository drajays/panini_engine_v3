"""
3.3.26  अवोदोर्नियः  —  VIDHI

Padaccheda: अव-उदोः नियः

krt-suffix rule: अवोदोर्नियः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_26_avodorniya_26"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_26_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avodorniyaH",
    text_dev              = "अवोदोर्नियः",
    padaccheda_dev        = "अव-उदोः नियः",
    why_dev               = "धातोः प्रत्ययः (३.3.26)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
