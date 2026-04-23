"""
3.3.3  भविष्यति गम्यादयः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=33003):** *bhaviṣyadadhikāraḥ* — scope
through **3.3.15**, matching v2 ``adhikara_prakarana.json`` sequence **22**
(भविष्यति गम्यादयः ३.३.३ … ३.३.१५ इति यावत्).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.3.3" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.3.3",
        "scope_end" : "3.3.15",
        "text_dev"  : "भविष्यति गम्यादयः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.3.3",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "Bavizyati gamyAdayaH",
    text_dev       = "भविष्यति गम्यादयः",
    padaccheda_dev = "भविष्यति / गमि-आदयः",
    why_dev        = "भविष्यदधिकारः — ३.३.३ तः ३.३.१५ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.3.3", "3.3.15"),
)

register_sutra(SUTRA)

