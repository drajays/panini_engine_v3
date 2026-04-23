"""
5.3.70  प्रागिवात्कः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=53070):** *kādhikāraḥ* — scope through
**5.3.95** (अवक्षेपणे कन्), matching v2 ``adhikara_prakarana.json`` sequence
**45**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "5.3.70" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "5.3.70",
        "scope_end" : "5.3.95",
        "text_dev"  : "प्रागिवात्कः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "5.3.70",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "prAg ivAt kaH",
    text_dev       = "प्रागिवात्कः",
    padaccheda_dev = "प्राक् / इवात् / कः",
    why_dev        = "काधिकारः — ५.३.७० तः ५.३.९५ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("5.3.70", "5.3.95"),
)

register_sutra(SUTRA)

