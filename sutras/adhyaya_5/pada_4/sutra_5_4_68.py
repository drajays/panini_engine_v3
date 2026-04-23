"""
5.4.68  समासान्ताः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=54068):** *samāsāntāḥ* —
*samāsāntādhikāraḥ* (scope through **5.4.160** निष्प्रवाणिश्च).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "5.4.68" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "5.4.68",
        "scope_end" : "5.4.160",
        "text_dev"  : "समासान्ताः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "5.4.68",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "samAsAntAH",
    text_dev       = "समासान्ताः",
    padaccheda_dev = "समासान्ताः",
    why_dev        = "समासान्ताधिकारः — ५.४.६८ तः ५.४.१६० पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("5.4.68", "5.4.160"),
)

register_sutra(SUTRA)

