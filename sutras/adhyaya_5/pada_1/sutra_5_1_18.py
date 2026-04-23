"""
5.1.18  प्राग्वतेष्ठञ्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=51018):** *prāg-vatīya ṭhañ-adhikāraḥ*
— scope through **5.1.114** (आकालिकडाद्यन्तवचने), matching v2
``adhikara_prakarana.json`` sequence **39**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "5.1.18" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "5.1.18",
        "scope_end" : "5.1.114",
        "text_dev"  : "प्राग्वतेष्ठञ्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "5.1.18",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "prAg vateH WaY",
    text_dev       = "प्राग्वतेष्ठञ्",
    padaccheda_dev = "प्राक् / वतेः / ठञ्",
    why_dev        = "प्राग्वतीयः ठञधिकारः — ५.१.१८ तः ५.१.११४ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("5.1.18", "5.1.114"),
)

register_sutra(SUTRA)

