"""
3.3.18  भावे  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=33018):** *bhāvādhikāraḥ* — scope
through **3.3.112** (आक्रोशे नञ्यनिः), matching v2
``adhikara_prakarana.json`` sequence **23**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.3.18" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.3.18",
        "scope_end" : "3.3.112",
        "text_dev"  : "भावे",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.3.18",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "BAve",
    text_dev       = "भावे",
    padaccheda_dev = "भावे",
    why_dev        = "भावाधिकारः — ३.३.१८ तः ३.३.११२ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.3.18", "3.3.112"),
)

register_sutra(SUTRA)

