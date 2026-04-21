"""
3.1.1  प्रत्ययः  —  ADHIKARA

Affix (*pratyaya*) scope opener (3.1.1–5.4.160 in traditional layout).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.1.1" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.1.1",
        "scope_end" : "5.4.160",
        "text_dev"  : "प्रत्ययः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.1",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "pratyayaH",
    text_dev       = "प्रत्ययः",
    padaccheda_dev = "प्रत्ययः",
    why_dev        = "अधिकारः प्रत्यय-विधानम् — ३.१.१ तः ५.४.१६० पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.1.1", "5.4.160"),
)

register_sutra(SUTRA)
