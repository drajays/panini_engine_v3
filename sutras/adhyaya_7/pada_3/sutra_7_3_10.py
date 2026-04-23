"""
7.3.10  उत्तरपदस्य  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=73010):** *uttarapadasya* —
*uttarapadasya ityadhikāraḥ* (scope through **7.3.32** हनस्तोऽचिण्णलोः).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "7.3.10" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "7.3.10",
        "scope_end" : "7.3.32",
        "text_dev"  : "उत्तरपदस्य",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "7.3.10",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "uttarapadasya",
    text_dev       = "उत्तरपदस्य",
    padaccheda_dev = "उत्तरपदस्य",
    why_dev        = "उत्तरपदस्य इत्यधिकारः — ७.३.१० तः ७.३.३२ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("7.3.10", "7.3.32"),
)

register_sutra(SUTRA)

