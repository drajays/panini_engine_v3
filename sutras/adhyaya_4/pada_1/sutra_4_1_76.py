"""
4.1.76  तद्धिताः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=41076):** opens the *taddhita* domain.
Scope through **5.4.160**, matching v2 ``adhikara_prakarana.json`` sequence
**32**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "4.1.76" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "4.1.76",
        "scope_end" : "5.4.160",
        "text_dev"  : "तद्धिताः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.76",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "taddhitAH",
    text_dev       = "तद्धिताः",
    padaccheda_dev = "तद्धिताः",
    why_dev        = "तद्धिताधिकारः — ४.१.७६ तः ५.४.१६० पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("4.1.76", "5.4.160"),
)

register_sutra(SUTRA)

