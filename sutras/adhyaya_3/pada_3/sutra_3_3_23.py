"""
3.3.23  समि युद्रुदुवः  —  VIDHI

Padaccheda: समि यु-द्रु-दुवः

krt-suffix rule: समि युद्रुदुवः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_23_sami_23"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_23_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sami yudruduvaH",
    text_dev              = "समि युद्रुदुवः",
    padaccheda_dev        = "समि यु-द्रु-दुवः",
    why_dev               = "धातोः प्रत्ययः (३.3.23)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
