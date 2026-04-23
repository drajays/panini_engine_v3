"""
4.1.83  प्राग्दीव्यतोऽण्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=41083):** *prāg-dīvyatīya aṇ-adhikāraḥ*
— scope through **4.3.168** (कंसीयपरशव्ययोर्यञञौ लुक् च), matching v2
``adhikara_prakarana.json`` sequence **34**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "4.1.83" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "4.1.83",
        "scope_end" : "4.3.168",
        "text_dev"  : "प्राग्दीव्यतोऽण्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.83",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "prAg dIvyataH aR",
    text_dev       = "प्राग्दीव्यतोऽण्",
    padaccheda_dev = "प्राक् / दीव्यतः / अण्",
    why_dev        = "प्राग्दीव्यतीयः अणधिकारः — ४.१.८३ तः ४.३.१६८ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("4.1.83", "4.3.168"),
)

register_sutra(SUTRA)

