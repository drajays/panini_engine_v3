"""
8.1.16  पदस्य  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=81016):** *padasya* —
*padasya ityadhikāraḥ* (scope through **8.3.55** अपदान्तस्य मूर्धन्यः).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "8.1.16" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "8.1.16",
        "scope_end" : "8.3.55",
        "text_dev"  : "पदस्य",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.1.16",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "padasya",
    text_dev       = "पदस्य",
    padaccheda_dev = "पदस्य",
    why_dev        = "पदस्य इत्यधिकारः — ८.१.१६ तः ८.३.५५ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("8.1.16", "8.3.55"),
)

register_sutra(SUTRA)

