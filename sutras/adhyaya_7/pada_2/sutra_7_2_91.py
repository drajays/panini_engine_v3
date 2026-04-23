"""
7.2.91  मपर्यन्तस्य  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=72091):** *maparyantasya* —
*maparyantasya ityadhikāraḥ* (scope through **7.2.98** प्रत्ययोत्तरपदयोश्च).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "7.2.91" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "7.2.91",
        "scope_end" : "7.2.98",
        "text_dev"  : "मपर्यन्तस्य",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.2.91",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "maparyantasya",
    text_dev       = "मपर्यन्तस्य",
    padaccheda_dev = "मपर्यन्तस्य",
    why_dev        = "मपर्यन्तस्य इत्यधिकारः — ७.२.९१ तः ७.२.९८ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("7.2.91", "7.2.98"),
)

register_sutra(SUTRA)

