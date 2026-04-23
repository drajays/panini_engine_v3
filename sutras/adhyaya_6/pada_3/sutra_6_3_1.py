"""
6.3.1  अलुगुत्तरपदे  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=63001):** *aluguttarapade* —
*uttarapadādhikāraḥ* (scope through **6.3.139** सम्प्रसारणस्य).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "6.3.1" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "6.3.1",
        "scope_end" : "6.3.139",
        "text_dev"  : "अलुगुत्तरपदे",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.3.1",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "aluguttarapade",
    text_dev       = "अलुगुत्तरपदे",
    padaccheda_dev = "अलुक् / उत्तरपदे",
    why_dev        = "उत्तरपदाधिकारः — ६.३.१ तः ६.३.१३९ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.3.1", "6.3.139"),
)

register_sutra(SUTRA)

