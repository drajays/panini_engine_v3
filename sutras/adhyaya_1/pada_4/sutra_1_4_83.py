"""
1.4.83  कर्मप्रवचनीयाः  (karmapravacanīyāḥ)  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=14083):** opens the traditional
*karmapravacanīya-saṃjñā* adhikāra (overlapping within the broader nipāta zone).

Per legacy span metadata, the scope runs through **1.4.98** (inclusive).
v3: pushes an adhikāra scope entry onto ``state.adhikara_stack`` with
``adhikara_scope = ("1.4.83", "1.4.98")``.
"""
from __future__ import annotations

from engine        import SutraType, SutraRecord, register_sutra
from engine.state  import State


def _already_open(state: State) -> bool:
    return any(e.get("id") == "1.4.83" for e in state.adhikara_stack)


def cond(state: State) -> bool:
    return not _already_open(state)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "1.4.83",
        "scope_end" : "1.4.98",
        "text_dev"  : "कर्मप्रवचनीयाः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id        = "1.4.83",
    sutra_type      = SutraType.ADHIKARA,
    text_slp1       = "karmapravacanIyAH",
    text_dev        = "कर्मप्रवचनीयाः",
    padaccheda_dev  = "कर्मप्रवचनीयाः",
    why_dev         = "१.४.८३ इत्यतः १.४.९८ पर्यन्तं 'कर्मप्रवचनीय' संज्ञाधिकारः प्रवर्तते।",
    anuvritti_from  = (),
    adhikara_scope  = ("1.4.83", "1.4.98"),
    cond            = cond,
    act             = act,
)

register_sutra(SUTRA)

