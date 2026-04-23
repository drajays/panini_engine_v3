"""
8.1.1  सर्वस्य द्वे  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=81001):** *sarvasya dve* —
*dviruktādhikāraḥ* (scope through **8.1.15**
द्वन्द्वं रहस्यमर्यादावचनव्युत्क्रमणयज्ञपात्रप्रयोगाभिव्यक्तिषु).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "8.1.1" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "8.1.1",
        "scope_end" : "8.1.15",
        "text_dev"  : "सर्वस्य द्वे",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.1.1",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "sarvasya dve",
    text_dev       = "सर्वस्य द्वे",
    padaccheda_dev = "सर्वस्य / द्वे",
    why_dev        = "द्विरुक्ताधिकारः — ८.१.१ तः ८.१.१५ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("8.1.1", "8.1.15"),
)

register_sutra(SUTRA)

