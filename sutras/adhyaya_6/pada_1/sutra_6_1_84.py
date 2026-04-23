"""
6.1.84  एकः पूर्वपरयोः  —  ADHIKARA

**Pāṭha (ashtadhyayi-com ``data.txt`` i=61084):** *ekaḥ pūrvaparayoḥ* —
*ekaḥ pūrvaparayoḥ ityadhikāraḥ* (scope through **6.1.109** एङः पदान्तादति).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return not any(e.get("id") == "6.1.84" for e in state.adhikara_stack)


def act(state: State) -> State:
    state.adhikara_stack.append({
        "id"        : "6.1.84",
        "scope_end" : "6.1.109",
        "text_dev"  : "एकः पूर्वपरयोः",
    })
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.84",
    sutra_type     = SutraType.ADHIKARA,
    text_slp1      = "ekaH pUrvaparayoH",
    text_dev       = "एकः पूर्वपरयोः",
    padaccheda_dev = "एकः / पूर्वपरयोः",
    why_dev        = "एकः पूर्वपरयोः इत्यधिकारः — ६.१.८४ तः ६.१.१०९ पर्यन्तम्।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
    adhikara_scope = ("6.1.84", "6.1.109"),
)

register_sutra(SUTRA)

