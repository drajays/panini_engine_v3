"""
3.4.67  कर्तरि कृत्  —  ADHIKARA

Scope for kṛt-pratyaya rules in the *kartṛ* sense, through 3.4.117 (per
traditional layout).  Pushes an adhikāra marker for trace alignment with
``pachak.md`` / kartṛi prakriyā.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if any(e.get("id") == "3.4.67" for e in state.adhikara_stack):
        return False
    # Kartṛ sense for kṛt (e.g. ण्वुल् agent nouns) — set by ``pipelines/krdanta``.
    return state.meta.get("krt_artha") == "kartari"


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.4.67",
        "scope_end" : "3.4.117",
        "text_dev"  : "कर्तरि कृत्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.4.67",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "kartari kft",
    text_dev       = "कर्तरि कृत्",
    padaccheda_dev = "कर्तरि कृत्",
    why_dev        = "कर्तरि अर्थे कृत्-प्रत्ययानां विधानम् — अधिकारः ३.४.६७ तः ३.४.११७ पर्यन्तम्।",
    anuvritti_from = ("3.4.66",),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.4.67", "3.4.117"),
)

register_sutra(SUTRA)
