"""
4.1.92  तस्यापत्यम्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=41092):** *prāg-dīvyatīya śeṣādhikāraḥ*
— scope through **4.3.120** (तस्येदम्), matching v2
``adhikara_prakarana.json`` sequence **35**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "4.1.92" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "4.1.92",
        "scope_end" : "4.3.120",
        "text_dev"  : "तस्यापत्यम्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.92",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "tasya apatyam",
    text_dev       = "तस्यापत्यम्",
    padaccheda_dev = "तस्य / अपत्यम्",
    why_dev        = "प्राग्दीव्यतीयः शेषाधिकारः — ४.१.९२ तः ४.३.१२० पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("4.1.92", "4.3.120"),
)

register_sutra(SUTRA)

