"""
4.3.51  व्याहरति मृगः  —  VIDHI

Padaccheda: व्याहरति (क्रियापदम्) मृगः

व्याहरति मृगः (4.3.51)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_51_vyAharati_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.51", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vyAharati mfgaH",
    text_dev              = "व्याहरति मृगः",
    padaccheda_dev        = "व्याहरति (क्रियापदम्) मृगः",
    why_dev               = "(सूत्रम् 4.3.51) व्याहरति मृगः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
