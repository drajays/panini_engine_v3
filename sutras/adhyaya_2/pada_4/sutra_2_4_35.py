"""
2.4.35  आर्धधातुके  (ārdhadhātuke)  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=24035):** opens the first
*ārdhadhātuka* adhikāra.

Per legacy span metadata, the scope runs through **2.4.57** (inclusive).
v3: pushes an adhikāra scope entry onto ``state.adhikara_stack`` with
``adhikara_scope = ("2.4.35", "2.4.57")``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _already_open(state: State) -> bool:
    return any(e.get("id") == "2.4.35" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return not _already_open(state)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "2.4.35",
        "scope_end" : "2.4.57",
        "text_dev"  : "आर्धधातुके",
    })
    return state


SUTRA = SutraRecord(
    sutra_id        = "2.4.35",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = "ArDadhAtuke",
    text_dev        = "आर्धधातुके",
    padaccheda_dev  = "आर्धधातुके",
    why_dev         = "२.४.३५ इत्यतः २.४.५७ पर्यन्तम् 'आर्धधातुके' अधिकारः (प्रथमः) प्रवर्तते।",
    anuvritti_from  = (),
    adhikara_scope  = ("2.4.35", "2.4.57"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)

