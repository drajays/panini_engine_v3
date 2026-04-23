"""
6.2.111  उत्तरपदादिः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=62111):** *uttarapadādiḥ* —
*uttarapadādyudāttasvarādhikāraḥ* (scope through **6.2.137** प्रकृत्या भगालम्).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "6.2.111" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "6.2.111",
        "scope_end" : "6.2.137",
        "text_dev"  : "उत्तरपदादिः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.2.111",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "uttarapadAdiH",
    text_dev       = "उत्तरपदादिः",
    padaccheda_dev = "उत्तरपदादिः",
    why_dev        = "उत्तरपदाद्युदात्तस्वराधिकारः — ६.२.१११ तः ६.२.१३७ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.2.111", "6.2.137"),
)

register_sutra(SUTRA)

