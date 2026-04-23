"""
3.3.19  अकर्तरि च कारके संज्ञायाम्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=33019):** adhikāra scope through
**3.3.112** (आक्रोशे नञ्यनिः), matching v2 ``adhikara_prakarana.json`` sequence
**24**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.3.19" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.3.19",
        "scope_end" : "3.3.112",
        "text_dev"  : "अकर्तरि च कारके संज्ञायाम्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.3.19",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "akartari ca kArake saMjYAyAm",
    text_dev       = "अकर्तरि च कारके संज्ञायाम्",
    padaccheda_dev = "अकर्तरि / च / कारके / संज्ञायाम्",
    why_dev        = "अकर्तरि च कारके संज्ञायाम् इत्यधिकारः — ३.३.१९ तः ३.३.११२ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.3.19", "3.3.112"),
)

register_sutra(SUTRA)

