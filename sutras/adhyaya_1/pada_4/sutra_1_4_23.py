"""
1.4.23  कारके  (kārake)  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=14023):** opens the traditional
*kāraka-saṃjñā* adhikāra.  Per legacy span metadata, the scope runs through
**1.4.55** (inclusive).

v3: pushes an adhikāra scope entry onto ``state.adhikara_stack`` with
``adhikara_scope = ("1.4.23", "1.4.55")``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _already_open(state: State) -> bool:
    return any(e.get("id") == "1.4.23" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return not _already_open(state)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "1.4.23",
        "scope_end" : "1.4.55",
        "text_dev"  : "कारके",
    })
    return state


SUTRA = SutraRecord(
    sutra_id        = "1.4.23",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = "kArake",
    text_dev        = "कारके",
    padaccheda_dev  = "कारके",
    why_dev         = "१.४.२३ 'कारके' इत्यधिकारः १.४.५५ पर्यन्तं प्रवर्तते।",
    anuvritti_from  = (),
    adhikara_scope  = ("1.4.23", "1.4.55"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)

