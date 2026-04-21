"""
3.1.2  परश्च  —  ADHIKARA

The affix follows its *nimitta* (after the base).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.1.2" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.1.2",
        "scope_end" : "5.4.160",
        "text_dev"  : "परश्च",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.2",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "paraS ca",
    text_dev       = "परश्च",
    padaccheda_dev = "परः च",
    why_dev        = "प्रत्ययः निमित्तात् परः।",
    anuvritti_from = ("3.1.1",),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.1.2", "5.4.160"),
)

register_sutra(SUTRA)
