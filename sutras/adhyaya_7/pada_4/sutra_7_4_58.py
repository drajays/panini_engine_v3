"""
7.4.58  अत्र लोपोऽभ्यासस्य  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=74058):** *atra lopo'bhyāsasya* —
*abhyāsalopādhikāraḥ* (scope through **7.4.97** ई च गणः).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "7.4.58" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "7.4.58",
        "scope_end" : "7.4.97",
        "text_dev"  : "अत्र लोपोऽभ्यासस्य",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.4.58",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "atra lopo'byAsasya",
    text_dev       = "अत्र लोपोऽभ्यासस्य",
    padaccheda_dev = "अत्र / लोपः / अभ्यासस्य",
    why_dev        = "अभ्यासलोपाधिकारः — ७.४.५८ तः ७.४.९७ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("7.4.58", "7.4.97"),
)

register_sutra(SUTRA)

