"""
2.1.4  सह सुपा  (saha supā)  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=21004):** opens the traditional
*supsupā* adhikāra (compound scope where a *sup*-ending item co-occurs “with
sup” in samāsa).

Per legacy span metadata, the scope runs through **2.2.38** (inclusive).
v3: pushes an adhikāra scope entry onto ``state.adhikara_stack`` with
``adhikara_scope = ("2.1.4", "2.2.38")``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _already_open(state: State) -> bool:
    return any(e.get("id") == "2.1.4" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return not _already_open(state)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "2.1.4",
        "scope_end" : "2.2.38",
        "text_dev"  : "सह सुपा",
    })
    return state


SUTRA = SutraRecord(
    sutra_id        = "2.1.4",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = "saha supA",
    text_dev        = "सह सुपा",
    padaccheda_dev  = "सह / सुपा",
    why_dev         = "२.१.४ इत्यतः २.२.३८ पर्यन्तं 'सुप्सुपा' अधिकारः प्रवर्तते।",
    anuvritti_from  = (),
    adhikara_scope  = ("2.1.4", "2.2.38"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)

