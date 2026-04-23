"""
5.3.2  किंसर्वनामबहुभ्योऽद्व्यादिभ्यः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=53002):** *kiṃ-sarvanāmādi-prakṛty*
adhikāra — scope through **5.3.26** (था हेतौ च च्छन्दसि), matching v2
``adhikara_prakarana.json`` sequence **44**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "5.3.2" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "5.3.2",
        "scope_end" : "5.3.26",
        "text_dev"  : "किंसर्वनामबहुभ्योऽद्व्यादिभ्यः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "5.3.2",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "kiM-sarvanAma-bahubhyaH advyAdibhyaH",
    text_dev       = "किंसर्वनामबहुभ्योऽद्व्यादिभ्यः",
    padaccheda_dev = "किं-सर्वनाम-बहुभ्यः / अद्व्यादिभ्यः",
    why_dev        = "किंसर्वनामादिप्रकृत्यधिकारः — ५.३.२ तः ५.३.२६ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("5.3.2", "5.3.26"),
)

register_sutra(SUTRA)

