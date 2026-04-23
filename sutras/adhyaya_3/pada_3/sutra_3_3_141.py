"""
3.3.141  वोताप्योः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=33141):** *vā lṛṅ-adhikāraḥ* — scope
through **3.3.151** (शेषे लृडयदौ), matching v2
``adhikara_prakarana.json`` sequence **27**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.3.141" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.3.141",
        "scope_end" : "3.3.151",
        "text_dev"  : "वोताप्योः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.3.141",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "vA A utApyOH",
    text_dev       = "वोताप्योः",
    padaccheda_dev = "वा / आ / उताप्योः",
    why_dev        = "वा लृङधिकारः — ३.३.१४१ तः ३.३.१५१ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.3.141", "3.3.151"),
)

register_sutra(SUTRA)

