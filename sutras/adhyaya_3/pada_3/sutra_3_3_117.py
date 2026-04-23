"""
3.3.117  करणाधिकरणयोश्च  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=33117):** *karaṇādhikaraṇayoḥ*
adhikāra — scope through **3.3.125** (खनो घ च), matching v2
``adhikara_prakarana.json`` sequence **26**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.3.117" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.3.117",
        "scope_end" : "3.3.125",
        "text_dev"  : "करणाधिकरणयोश्च",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.3.117",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "karaNA-DikaraNayoS ca",
    text_dev       = "करणाधिकरणयोश्च",
    padaccheda_dev = "करण-अधिकरणयोः / च",
    why_dev        = "करणाधिकरणयोः इत्यधिकारः — ३.३.११७ तः ३.३.१२५ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.3.117", "3.3.125"),
)

register_sutra(SUTRA)

