"""
6.1.72  संहितायाम्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=61072):** *saṃhitāyām* —
*saṃhitādhikāraḥ (prathamaḥ)* (scope through **6.1.157**
पारस्करप्रभृतीनि च संज्ञायाम्).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "6.1.72" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "6.1.72",
        "scope_end" : "6.1.157",
        "text_dev"  : "संहितायाम्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.72",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "saMhitAyAm",
    text_dev       = "संहितायाम्",
    padaccheda_dev = "संहितायाम्",
    why_dev        = "संहिताधिकारः (प्रथमः) — ६.१.७२ तः ६.१.१५७ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.1.72", "6.1.157"),
)

register_sutra(SUTRA)

