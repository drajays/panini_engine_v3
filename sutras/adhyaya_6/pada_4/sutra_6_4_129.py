"""
6.4.129  भस्य  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=64129):** *bhasya* —
*bhādhikāraḥ* (scope through **6.4.175**
ऋत्व्यवास्त्व्यवास्त्वमाध्वीहिरण्ययानि च्छन्दसि).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "6.4.129" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "6.4.129",
        "scope_end" : "6.4.175",
        "text_dev"  : "भस्य",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.129",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "bhasya",
    text_dev       = "भस्य",
    padaccheda_dev = "भस्य",
    why_dev        = "भाधिकारः — ६.४.१२९ तः ६.४.१७५ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.4.129", "6.4.175"),
)

register_sutra(SUTRA)

