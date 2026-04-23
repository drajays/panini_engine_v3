"""
3.1.91  धातोः  —  ADHIKARA

Kṛt/tiṅ pratyayas attach to *dhātu* (3.1.91–3.4.117).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if any(e.get("id") == "3.1.91" for e in state.adhikara_stack):
        return False
    return any("dhatu" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.1.91",
        "scope_end" : "3.4.117",
        "text_dev"  : "धातोः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.91",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "DAtoH",
    text_dev       = "धातोः",
    padaccheda_dev = "धातोः",
    why_dev        = "धातोः कृत्-तिङ्-प्रत्ययाः — अधिकारः ३.१.९१ तः ३.४.११७ पर्यन्तम्।",
    anuvritti_from = ("3.1.1", "3.1.2", "3.1.3"),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.1.91", "3.4.117"),
)

register_sutra(SUTRA)
