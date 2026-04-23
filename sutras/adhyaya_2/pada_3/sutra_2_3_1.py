"""
2.3.1  अनभिहिते  (anabhihite)  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=23001):** opens the traditional
*anabhihita* adhikāra in vibhakti-prakaraṇa.

Per legacy span metadata, the scope runs through **2.3.73** (inclusive).
v3: pushes an adhikāra scope entry onto ``state.adhikara_stack`` with
``adhikara_scope = ("2.3.1", "2.3.73")``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _already_open(state: State) -> bool:
    return any(e.get("id") == "2.3.1" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return not _already_open(state)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "2.3.1",
        "scope_end" : "2.3.73",
        "text_dev"  : "अनभिहिते",
    })
    return state


SUTRA = SutraRecord(
    sutra_id        = "2.3.1",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = "anabhihite",
    text_dev        = "अनभिहिते",
    padaccheda_dev  = "अनभिहिते",
    why_dev         = "२.३.१ इत्यतः २.३.७३ पर्यन्तं 'अनभिहित' अधिकारः प्रवर्तते।",
    anuvritti_from  = (),
    adhikara_scope  = ("2.3.1", "2.3.73"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)

