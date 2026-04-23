"""
3.1.3  आद्युदात्तश्च  —  ADHIKARA

Within the *pratyaya* adhikāra (3.1.1–5.4.160), the property “first syllable
*udātta*” governs *pratyaya* operations until **5.4.160** (traditional layout;
ashtadhyayi-com type: प्रत्ययस्य आद्युदात्तत्वाधिकारः).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.1.3" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.1.3",
        "scope_end" : "5.4.160",
        "text_dev"  : "आद्युदात्तश्च",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.3",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "AdyudAttaS ca",
    text_dev       = "आद्युदात्तश्च",
    padaccheda_dev = "आद्युदात्तः च",
    why_dev        = "प्रत्ययस्य आद्युदात्तत्वम् — अधिकारः ३.१.३ तः ५.४.१६० पर्यन्तम्।",
    anuvritti_from = ("3.1.1", "3.1.2"),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.1.3", "5.4.160"),
)

register_sutra(SUTRA)
