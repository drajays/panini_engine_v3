"""
3.3.70  अक्षेषु ग्लहः  —  VIDHI

Padaccheda: अक्षेषु ग्लहः

krt-suffix rule: अक्षेषु ग्लहः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_70_akzezu_70"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "akzezu glahaH",
    text_dev              = "अक्षेषु ग्लहः",
    padaccheda_dev        = "अक्षेषु ग्लहः",
    why_dev               = "धातोः प्रत्ययः (३.3.70)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
