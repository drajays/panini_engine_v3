"""
3.4.68  भावे  —  ADHIKARA

Narrow v3 use: opens the *bhāve* scope for *kṛt* affixation (e.g. *lyuṭ* in
``pipelines/krdanta``) when ``state.meta['krt_artha'] == 'bhave'``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    if any(e.get("id") == "3.4.68" for e in state.adhikara_stack):
        return False
    return state.meta.get("krt_artha") == "bhave"


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.4.68",
        "scope_end" : "3.4.117",
        "text_dev"  : "भावे",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.4.68",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "BAve",
    text_dev       = "भावे",
    padaccheda_dev = "भावे",
    why_dev        = "भाव-अर्थे कृत्-प्रत्ययानां विधानम् — अधिकारः।",
    anuvritti_from = ("3.4.67",),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.4.68", "3.4.117"),
)

register_sutra(SUTRA)
