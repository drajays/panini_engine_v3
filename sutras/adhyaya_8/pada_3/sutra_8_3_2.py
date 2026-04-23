"""
8.3.2  अत्रानुनासिकः पूर्वस्य तु वा  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=83002):** *atrānunāsikaḥ pūrvasya tu vā* —
*anunāsikavidhi-adhikāraḥ* (scope through **8.3.12** कानाम्रेडिते).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "8.3.2" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "8.3.2",
        "scope_end" : "8.3.12",
        "text_dev"  : "अत्रानुनासिकः पूर्वस्य तु वा",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "8.3.2",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "atrAnunAsikaH pUrvasya tu vA",
    text_dev       = "अत्रानुनासिकः पूर्वस्य तु वा",
    padaccheda_dev = "अत्र / अनुनासिकः / पूर्वस्य / तु / वा",
    why_dev        = "अनुनासिकविध्यधिकारः — ८.३.२ तः ८.३.१२ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("8.3.2", "8.3.12"),
)

register_sutra(SUTRA)

