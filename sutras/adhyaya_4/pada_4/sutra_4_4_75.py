"""
4.4.75  प्राग्घिताद्यत्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=44075):** *yad-adhikāraḥ prāg-ghitīyaḥ*
— scope through **5.1.136** (ब्रह्मणस्त्वः), matching v2
``adhikara_prakarana.json`` sequence **37**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "4.4.75" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "4.4.75",
        "scope_end" : "5.1.136",
        "text_dev"  : "प्राग्घिताद्यत्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.4.75",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "prAg hitAt yat",
    text_dev       = "प्राग्घिताद्यत्",
    padaccheda_dev = "प्राक् / हितात् / यत्",
    why_dev        = "यदधिकारः प्राग्घितीयः — ४.४.७५ तः ५.१.१३६ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("4.4.75", "5.1.136"),
)

register_sutra(SUTRA)

