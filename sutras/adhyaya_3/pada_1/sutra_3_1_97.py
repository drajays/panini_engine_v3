"""
3.1.97  अचो यत्  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=31097):** *kṛtya-saṃjñādhikāra* — scope
for naming / *kṛtya* readings with **yat** after a vowel-final base, through
**3.1.132** (type: कृत्यसंज्ञाधिकारः).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.1.97" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.1.97",
        "scope_end" : "3.1.132",
        "text_dev"  : "अचो यत्",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.1.97",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "aco yat",
    text_dev       = "अचो यत्",
    padaccheda_dev = "अचः यत्",
    why_dev        = "कृत्य-संज्ञाधिकारः — ३.१.९७ तः ३.१.१३२ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.1.97", "3.1.132"),
)

register_sutra(SUTRA)
