"""
3.2.134  आक्वेस्तच्छीलतद्धर्मतत्साधुकारिषु  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=32134):** *tācchīlyādhikāraḥ* — scope
through **3.2.177**, matching v2 ``adhikara_prakarana.json`` sequence **21**
(आक्वेस्तच्छीलतद्धर्मतत्साधुकारिषु ३.२.१३४ … ३.२.१७७ इति यावत्).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "3.2.134" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "3.2.134",
        "scope_end" : "3.2.177",
        "text_dev"  : "आक्वेस्तच्छीलतद्धर्मतत्साधुकारिषु",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.2.134",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "A kve tacchIla-taddharma-tatsADhukAriSu",
    text_dev       = "आक्वेस्तच्छीलतद्धर्मतत्साधुकारिषु",
    padaccheda_dev = "आ / क्वे / तच्छील-तद्धर्म-तत्साधुकारिषु",
    why_dev        = "ताच्छील्याधिकारः — ३.२.१३४ तः ३.२.१७७ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("3.2.134", "3.2.177"),
)

register_sutra(SUTRA)

