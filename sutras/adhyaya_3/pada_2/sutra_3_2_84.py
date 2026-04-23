"""
3.2.84  भूते  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=32084):** *bhūtādhikāraḥ* — scope for
past (*bhūta*) readings through **3.2.122**, per v2
``data/adhikara_prakarana.json`` sequence **19** (anchor: भूते ३.२.८४ …
३.२.१२२ इति यावत्).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.2.84" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.2.84",
        "scope_end" : "3.2.122",
        "text_dev"  : "भूते",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.2.84",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "BUte",
    text_dev       = "भूते",
    padaccheda_dev = "भूते",
    why_dev        = "भूताधिकारः — ३.२.८४ तः ३.२.१२२ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.2.84", "3.2.122"),
)

register_sutra(SUTRA)
