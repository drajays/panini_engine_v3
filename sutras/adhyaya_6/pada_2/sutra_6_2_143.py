"""
6.2.143  अन्तः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=62143):** *antaḥ* —
*uttarapadāntodāttasvaraprakaraṇam* (scope through **6.2.199**
परादिश्छन्दसि बहुलम्).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "6.2.143" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "6.2.143",
        "scope_end" : "6.2.199",
        "text_dev"  : "अन्तः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.2.143",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "antaH",
    text_dev       = "अन्तः",
    padaccheda_dev = "अन्तः",
    why_dev        = "उत्तरपदान्तोदात्तस्वरप्रकरणम् — ६.२.१४३ तः ६.२.१९९ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.2.143", "6.2.199"),
)

register_sutra(SUTRA)

