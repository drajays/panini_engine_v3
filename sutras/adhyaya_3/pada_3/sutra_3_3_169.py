"""
3.3.169  अर्हे कृत्यतृचश्च  —  VIDHI

Padaccheda: अर्हे कृत्य-तृचः च

krt-suffix rule: अर्हे कृत्यतृचश्च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_169_arhe_169"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.169"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.169",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "arhe kftyatfcaSca",
    text_dev              = "अर्हे कृत्यतृचश्च",
    padaccheda_dev        = "अर्हे कृत्य-तृचः च",
    why_dev               = "धातोः प्रत्ययः (३.3.169)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
