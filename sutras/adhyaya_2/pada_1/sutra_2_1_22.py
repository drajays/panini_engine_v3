"""
2.1.22  तत्पुरुषः  (tatpuruṣaḥ)  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=21022):** opens the traditional
*tatpuruṣa* adhikāra in the samāsa-prakaraṇa.

Per legacy span metadata, the scope runs through **2.2.22** (inclusive).
v3: pushes an adhikāra scope entry onto ``state.adhikara_stack`` with
``adhikara_scope = ("2.1.22", "2.2.22")``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _already_open(state: State) -> bool:
    return any(e.get("id") == "2.1.22" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return not _already_open(state)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "2.1.22",
        "scope_end" : "2.2.22",
        "text_dev"  : "तत्पुरुषः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id        = "2.1.22",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = "tatpuruzaH",
    text_dev        = "तत्पुरुषः",
    padaccheda_dev  = "तत्पुरुषः",
    why_dev         = "२.१.२२ इत्यतः २.२.२२ पर्यन्तं 'तत्पुरुष' अधिकारः प्रवर्तते।",
    anuvritti_from  = (),
    adhikara_scope  = ("2.1.22", "2.2.22"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)

