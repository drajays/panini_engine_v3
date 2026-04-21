"""
1.1.50  स्थानेऽन्तरतमः  —  PARIBHASHA

Operational v3 role: sets ``paribhasha_gates['sthanantara_vrddhi']`` so
*sthānāntara* choice for *vṛddhi* (e.g. ``I`` → ``E``) is available to
**7.2.115** without reading surface strings.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def cond(state: State) -> bool:
    return "sthanantara_vrddhi" not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates["sthanantara_vrddhi"] = {
        "a": "A",
        "i": "E",
        "I": "E",
        "u": "O",
        "U": "O",
    }
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.50",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "sTAne antaratamaH",
    text_dev       = "स्थानेऽन्तरतमः",
    padaccheda_dev = "स्थाने अन्तरतमः",
    why_dev        = "वृद्धौ स्थानानुसारेण अन्तरतमः वर्णः (इकारादौ ऐ)।",
    anuvritti_from = ("1.1.49",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
