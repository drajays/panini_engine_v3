"""
6.1.1  एकाचो द्वे प्रथमस्य  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=61001):** *ekāco dve prathamasya* —
*dvitvādhikāraḥ* (scope through **6.1.12** दाश्वान् साह्वान् मीढ्वांश्च).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "6.1.1" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "6.1.1",
        "scope_end" : "6.1.12",
        "text_dev"  : "एकाचो द्वे प्रथमस्य",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.1",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "ekAco dve prathamasya",
    text_dev       = "एकाचो द्वे प्रथमस्य",
    padaccheda_dev = "एकाचः / द्वे / प्रथमस्य",
    why_dev        = "द्वित्वाधिकारः — ६.१.१ तः ६.१.१२ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.1.1", "6.1.12"),
)

register_sutra(SUTRA)

