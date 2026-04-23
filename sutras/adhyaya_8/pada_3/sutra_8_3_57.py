"""
8.3.57  इण्कोः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=83057):** *iṇkoḥ* —
*iṇkoḥ ityadhikāraḥ* (scope through **8.3.119**
निव्यभिभ्योऽड्व्यवाये वा छन्दसि).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "8.3.57" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "8.3.57",
        "scope_end" : "8.3.119",
        "text_dev"  : "इण्कोः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.3.57",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "iNkoH",
    text_dev       = "इण्कोः",
    padaccheda_dev = "इण्कोः",
    why_dev        = "इण्कोः इत्यधिकारः — ८.३.५७ तः ८.३.११९ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("8.3.57", "8.3.119"),
)

register_sutra(SUTRA)

