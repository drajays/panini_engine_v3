"""
8.3.55  अपदान्तस्य मूर्धन्यः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=83055):** *apadāntasya mūrdhanyaḥ* —
*apadāntasya mūrdhanyaḥ ityadhikāraḥ* (scope through **8.3.119**
निव्यभिभ्योऽड्व्यवाये वा छन्दसि).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "8.3.55" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "8.3.55",
        "scope_end" : "8.3.119",
        "text_dev"  : "अपदान्तस्य मूर्धन्यः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.3.55",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "apadAntasya mUrdhanyaH",
    text_dev       = "अपदान्तस्य मूर्धन्यः",
    padaccheda_dev = "अपदान्तस्य / मूर्धन्यः",
    why_dev        = "अपदान्तस्य मूर्धन्यः इत्यधिकारः — ८.३.५५ तः ८.३.११९ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("8.3.55", "8.3.119"),
)

register_sutra(SUTRA)

