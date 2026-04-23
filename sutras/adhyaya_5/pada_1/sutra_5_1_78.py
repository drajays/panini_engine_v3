"""
5.1.78  कालात्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=51078):** *kālādhikāraḥ* — scope through
**5.1.97** (व्युष्टादिभ्योऽण्), matching v2 ``adhikara_prakarana.json`` sequence
**41**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "5.1.78" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "5.1.78",
        "scope_end" : "5.1.97",
        "text_dev"  : "कालात्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "5.1.78",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "kAlAt",
    text_dev       = "कालात्",
    padaccheda_dev = "कालात्",
    why_dev        = "कालाधिकारः — ५.१.७८ तः ५.१.९७ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("5.1.78", "5.1.97"),
)

register_sutra(SUTRA)

