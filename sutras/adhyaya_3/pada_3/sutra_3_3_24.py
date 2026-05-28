"""
3.3.24  श्रिणीभुवोऽनुपसर्गे  —  VIDHI

Padaccheda: श्रि-णी-भुवः अन्-उपसर्गे

krt-suffix rule: श्रिणीभुवोऽनुपसर्गे
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_24_SriRIBuvo_24"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_24_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SriRIBuvo'nupasarge",
    text_dev              = "श्रिणीभुवोऽनुपसर्गे",
    padaccheda_dev        = "श्रि-णी-भुवः अन्-उपसर्गे",
    why_dev               = "धातोः प्रत्ययः (३.3.24)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
