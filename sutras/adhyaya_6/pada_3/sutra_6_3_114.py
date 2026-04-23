"""
6.3.114  संहितायाम्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=63114):** *saṃhitāyām* —
*saṃhitādhikāraḥ (dvitīyaḥ)* (scope through **6.3.139** सम्प्रसारणस्य).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "6.3.114" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "6.3.114",
        "scope_end" : "6.3.139",
        "text_dev"  : "संहितायाम्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.3.114",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "saMhitAyAm",
    text_dev       = "संहितायाम्",
    padaccheda_dev = "संहितायाम्",
    why_dev        = "संहिताधिकारः (द्वितीयः) — ६.३.११४ तः ६.३.१३९ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.3.114", "6.3.139"),
)

register_sutra(SUTRA)

