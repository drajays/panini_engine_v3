"""
8.1.17  पदात्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=81017):** *padāt* —
*padāt ityadhikāraḥ* (scope through **8.1.69** कुत्सने च सुप्यगोत्रादौ).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "8.1.17" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "8.1.17",
        "scope_end" : "8.1.69",
        "text_dev"  : "पदात्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.1.17",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "padAt",
    text_dev       = "पदात्",
    padaccheda_dev = "पदात्",
    why_dev        = "पदात् इत्यधिकारः — ८.१.१७ तः ८.१.६९ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("8.1.17", "8.1.69"),
)

register_sutra(SUTRA)

