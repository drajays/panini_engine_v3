"""
1.1.51  उरण् रपरः  —  VIDHI

When guṇa of a vocalic **ṛ** / **ḷ** (``f`` / ``x``) yields short ``a``,
the **r** (or **l**) consonant follows (``ar``, ``al``) — operational slice
for **kar** / **har** after **7.3.84**.

Note: **1.1.50** in this repo is **स्थानेऽन्तरतमः** (vṛddhi paribhāṣā).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk


def cond(state: State) -> bool:
    if not state.terms:
        return False
    d0 = state.terms[0]
    if "dhatu" not in d0.tags:
        return False
    if d0.meta.get("urN_rapara_pending") not in ("r", "l"):
        return False
    if not d0.varnas:
        return False
    return d0.varnas[-1].slp1 == "a"


def act(state: State) -> State:
    d0 = state.terms[0]
    kind = d0.meta.get("urN_rapara_pending")
    d0.varnas.append(mk("r" if kind == "r" else "l"))
    d0.meta["urN_rapara_pending"] = None
    d0.meta["urN_rapara_done"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.51",
    sutra_type     = SutraType.VIDHI,
    text_slp1      = "uraR raparaH",
    text_dev       = "उरण् रपरः",
    padaccheda_dev = "उरण् रपरः",
    why_dev        = "ऋकार-गुणे अकारे परः रकारः (कृ→कर्, हृ→हर्)।",
    anuvritti_from = ("1.1.50",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
