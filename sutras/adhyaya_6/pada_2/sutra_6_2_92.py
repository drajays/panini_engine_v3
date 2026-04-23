"""
6.2.92  अन्तः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=62092):** *antaḥ* —
*pūrvapadāntodāttasvādhikāraḥ* (scope through **6.2.110**
निष्ठोपसर्गपूर्वमन्यतरस्याम्).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "6.2.92" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "6.2.92",
        "scope_end" : "6.2.110",
        "text_dev"  : "अन्तः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.2.92",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "antaH",
    text_dev       = "अन्तः",
    padaccheda_dev = "अन्तः",
    why_dev        = "पूर्वपदान्तोदात्तस्वाधिकारः — ६.२.९२ तः ६.२.११० पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.2.92", "6.2.110"),
)

register_sutra(SUTRA)

