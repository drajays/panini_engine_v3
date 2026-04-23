"""
6.4.46  आर्धधातुके  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=64046):** *ārdhadhātuke* —
*ārdhadhātuke ityadhikāraḥ (dvitīyaḥ)* (scope through **6.4.70**
मयतेरिदन्यतरस्याम्).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "6.4.46" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "6.4.46",
        "scope_end" : "6.4.70",
        "text_dev"  : "आर्धधातुके",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.46",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "ArDadhAtuke",
    text_dev       = "आर्धधातुके",
    padaccheda_dev = "आर्धधातुके",
    why_dev        = "आर्धधातुके इत्यधिकारः (द्वितीयः) — ६.४.४६ तः ६.४.७० पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.4.46", "6.4.70"),
)

register_sutra(SUTRA)

