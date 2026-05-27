"""
2.2.34  अल्पाच्तरम्  —  ANUVADA (dvandva ordering note)

Śāstra: provides a default ordering preference among compound members.

Engine: fires when any Term carries the ``dvandva`` tag and the dvandva samjña
has already been stamped (2.2.29 fired first). Records an anuvāda audit step
without mutating the tape.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if not any("dvandva" in t.tags for t in state.terms):
        return False
    if not bool(state.samjna_registry.get("2.2.29_cArthe_dvandva")):
        return False
    return not bool(state.samjna_registry.get("2.2.34_alpActaram"))


def act(state: State) -> State:
    state.samjna_registry["2.2.34_alpActaram"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.2.34",
    sutra_type     = SutraType.ANUVADA,
    text_slp1      = "alpActaram",
    text_dev       = "अल्पाच्तरम्",
    padaccheda_dev = "अल्प-अच्-तरम्",
    why_dev        = "समासे पदक्रम-नियमः (narrow audit stamp for P013).",
    anuvritti_from = ("2.2.29",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

