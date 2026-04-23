"""
6.4.22  असिद्धवदत्राभात्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=64022):** *asiddhavad atrā bhāt* —
*asiddhavada-dhikāraḥ* (scope through **6.4.175**
ऋत्व्यवास्त्व्यवास्त्वमाध्वीहिरण्ययानि च्छन्दसि).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "6.4.22" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "6.4.22",
        "scope_end" : "6.4.175",
        "text_dev"  : "असिद्धवदत्राभात्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.4.22",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "asiddhavadatrABAt",
    text_dev       = "असिद्धवदत्राभात्",
    padaccheda_dev = "असिद्धवत् / अत्र / आ / भात्",
    why_dev        = "असिद्धवदधिकारः — ६.४.२२ तः ६.४.१७५ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.4.22", "6.4.175"),
)

register_sutra(SUTRA)

