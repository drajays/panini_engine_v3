"""
4.1.82  समर्थानां प्रथमाद्वा  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=41082):** *samarthādhikāraḥ* — scope
through **5.2.140** (अहंशुभमोर्युस्), matching v2
``adhikara_prakarana.json`` sequence **33**.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "4.1.82" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "4.1.82",
        "scope_end" : "5.2.140",
        "text_dev"  : "समर्थानां प्रथमाद्वा",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "4.1.82",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "samarthAnAm prathamAd vA",
    text_dev       = "समर्थानां प्रथमाद्वा",
    padaccheda_dev = "समर्थानाम् / प्रथमात् / वा",
    why_dev        = "समर्थाधिकारः — ४.१.८२ तः ५.२.१४० पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("4.1.82", "5.2.140"),
)

register_sutra(SUTRA)

