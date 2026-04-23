"""
5.3.1  प्राग्दिशो विभक्तिः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=53001):** *vibhakti-saṃjñā* domain
opener. Scope through **5.3.26** (था हेतौ च च्छन्दसि), matching v2
``adhikara_prakarana.json`` sequence **43**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "5.3.1" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "5.3.1",
        "scope_end" : "5.3.26",
        "text_dev"  : "प्राग्दिशो विभक्तिः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "5.3.1",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "prAg diSo vibhaktiH",
    text_dev       = "प्राग्दिशो विभक्तिः",
    padaccheda_dev = "प्राक् / दिशः / विभक्तिः",
    why_dev        = "विभक्तिसंज्ञाधिकारः — ५.३.१ तः ५.३.२६ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("5.3.1", "5.3.26"),
)

register_sutra(SUTRA)

