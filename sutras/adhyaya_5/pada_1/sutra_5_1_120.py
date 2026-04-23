"""
5.1.120  आ च त्वात्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=51120):** *tvat-talor adhikāraḥ* — scope
through **5.1.136** (ब्रह्मणस्त्वः), matching v2
``adhikara_prakarana.json`` sequence **42**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "5.1.120" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "5.1.120",
        "scope_end" : "5.1.136",
        "text_dev"  : "आ च त्वात्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "5.1.120",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "A ca tvAt",
    text_dev       = "आ च त्वात्",
    padaccheda_dev = "आ / च / त्वात्",
    why_dev        = "त्वतलोरधिकारः — ५.१.१२० तः ५.१.१३६ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("5.1.120", "5.1.136"),
)

register_sutra(SUTRA)

