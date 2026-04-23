"""
3.4.77  लस्य  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=34077):** *lādhikāraḥ* — scope through
**3.4.112** (द्विषश्च), matching v2 ``adhikara_prakarana.json`` sequence **28**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.4.77" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.4.77",
        "scope_end" : "3.4.112",
        "text_dev"  : "लस्य",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.4.77",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "lasya",
    text_dev       = "लस्य",
    padaccheda_dev = "लस्य",
    why_dev        = "लाधिकारः — ३.४.७७ तः ३.४.११२ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.4.77", "3.4.112"),
)

register_sutra(SUTRA)

