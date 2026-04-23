"""
2.1.11  विभाषा  (vibhāṣā)  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=21011):** opens the traditional
*vibhāṣā* adhikāra within the samāsa-prakaraṇa.

Per legacy span metadata, the scope runs through **2.2.38** (inclusive).
v3: pushes an adhikāra scope entry onto ``state.adhikara_stack`` with
``adhikara_scope = ("2.1.11", "2.2.38")``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _already_open(state: State) -> bool:
    return any(e.get("id") == "2.1.11" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return not _already_open(state)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "2.1.11",
        "scope_end" : "2.2.38",
        "text_dev"  : "विभाषा",
    })
    return state


SUTRA = SutraRecord(
    sutra_id        = "2.1.11",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = "viBASA",
    text_dev        = "विभाषा",
    padaccheda_dev  = "विभाषा",
    why_dev         = "२.१.११ इत्यतः २.२.३८ पर्यन्तं 'विभाषा' अधिकारः प्रवर्तते।",
    anuvritti_from  = (),
    adhikara_scope  = ("2.1.11", "2.2.38"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)

