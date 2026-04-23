"""
3.2.123  वर्तमाने लट्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=32123):** *vartamānādhikāraḥ* — present
stem (**laṭ**) after *vartamāne*, through **3.3.1** (type ``$33001``). Matches
v2 ``adhikara_prakarana.json`` sequence **20**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.2.123" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.2.123",
        "scope_end" : "3.3.1",
        "text_dev"  : "वर्तमाने लट्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.2.123",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "vartamAne laT",
    text_dev       = "वर्तमाने लट्",
    padaccheda_dev = "वर्तमाने लट्",
    why_dev        = "वर्तमानाधिकारः — ३.२.१२३ तः ३.३.१ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.2.123", "3.3.1"),
)

register_sutra(SUTRA)
