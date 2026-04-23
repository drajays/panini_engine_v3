"""
4.1.3  स्त्रियाम्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=41003):** *strī-adhikāraḥ (dvitīyaḥ)*
— scope through **4.1.89** (गोत्रेऽलुगचि), matching v2
``adhikara_prakarana.json`` sequence **30**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "4.1.3" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "4.1.3",
        "scope_end" : "4.1.89",
        "text_dev"  : "स्त्रियाम्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.3",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "striyAm",
    text_dev       = "स्त्रियाम्",
    padaccheda_dev = "स्त्रियाम्",
    why_dev        = "स्त्र्यधिकारः (द्वितीयः) — ४.१.३ तः ४.१.८९ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("4.1.3", "4.1.89"),
)

register_sutra(SUTRA)

