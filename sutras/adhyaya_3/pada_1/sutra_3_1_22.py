"""
3.1.22  धातोरेकाचो हलादेः क्रियासमभिहारे यङ्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=31022):** first *dhātv‑adhikāra*
(प्रथमः), scope **3.1.22–3.1.90** — *yaṅ* after a mono‑syllabic root beginning
with a consonant, in the sense of repeated / intensive action.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.1.22" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.1.22",
        "scope_end" : "3.1.90",
        "text_dev"  : "धातोरेकाचो हलादेः क्रियासमभिहारे यङ्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.22",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "DAtor ekAco halAdeH kriyAsamabhihAre yaG",
    text_dev       = "धातोरेकाचो हलादेः क्रियासमभिहारे यङ्",
    padaccheda_dev = "धातोः एकाचः हलादेः क्रियासमभिहारे यङ्",
    why_dev        = (
        "धात्वधिकारः (प्रथमः) — ३.१.२२ तः ३.१.९० पर्यन्तम् "
        "(एकाच् हलादि-धातौ क्रियासमभिहारे यङ्)।"
    ),
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.1.22", "3.1.90"),
)

register_sutra(SUTRA)
