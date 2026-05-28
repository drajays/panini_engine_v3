"""
3.3.40  हस्तादाने चेरस्तेये  —  VIDHI

Padaccheda: हस्त-आदाने चेः अस्तेये

krt-suffix rule: हस्तादाने चेरस्तेये
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_40_hastAdAne_40"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_40_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.40"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hastAdAne cerasteye",
    text_dev              = "हस्तादाने चेरस्तेये",
    padaccheda_dev        = "हस्त-आदाने चेः अस्तेये",
    why_dev               = "धातोः प्रत्ययः (३.3.40)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
