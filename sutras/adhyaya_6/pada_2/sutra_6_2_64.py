"""
6.2.64  आदिरुदात्तः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=62064):** *ādirudāttaḥ* —
*pūrvapadādyudāttasvarādhikāraḥ* (scope through **6.2.137** प्रकृत्या भगालम्).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "6.2.64" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "6.2.64",
        "scope_end" : "6.2.137",
        "text_dev"  : "आदिरुदात्तः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.2.64",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "AdirudAttaH",
    text_dev       = "आदिरुदात्तः",
    padaccheda_dev = "आदिः / उदात्तः",
    why_dev        = "पूर्वपदाद्युदात्तस्वराधिकारः — ६.२.६४ तः ६.२.१३७ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.2.64", "6.2.137"),
)

register_sutra(SUTRA)

