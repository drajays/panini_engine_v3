"""
3.3.94  स्त्रियां क्तिन्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=33094):** *strī-adhikāraḥ (prathamaḥ)*
— scope through **3.3.112** (आक्रोशे नञ्यनिः), matching v2
``adhikara_prakarana.json`` sequence **25**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.3.94" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.3.94",
        "scope_end" : "3.3.112",
        "text_dev"  : "स्त्रियां क्तिन्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.3.94",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "striyAm ktin",
    text_dev       = "स्त्रियां क्तिन्",
    padaccheda_dev = "स्त्रियाम् / क्तिन्",
    why_dev        = "स्त्र्यधिकारः (प्रथमः) — ३.३.९४ तः ३.३.११२ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.3.94", "3.3.112"),
)

register_sutra(SUTRA)

