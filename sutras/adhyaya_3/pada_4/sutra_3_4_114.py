"""
3.4.114  आर्धधातुकं शेषः  —  SAMJNA

Śeṣa pratyayas that are not sārvadhātuka (3.4.113) are ārdhadhātuka.
Narrow v3 use: tag a **tfc** kṛt pratyaya so 7.2.35 / 7.3.84 can key off
``ardhadhatuka`` without reading string goals.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


def _krt_term(state: State):
    for t in state.terms:
        if t.kind == "pratyaya" and "krt" in t.tags:
            return t
    return None


def cond(state: State) -> bool:
    pr = _krt_term(state)
    if pr is None:
        return False
    if "ardhadhatuka" in pr.tags:
        return False
    upa = pr.meta.get("upadesha_slp1")
    # tiṅ sārvadhātuka pratyayas are out of scope here; tfc is ārdhadhātuka.
    return upa == "tfc"


def act(state: State) -> State:
    pr = _krt_term(state)
    if pr is None:
        return state
    pr.tags.add("ardhadhatuka")
    state.samjna_registry["3.4.114_ardhadhatuka"] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "3.4.114",
    sutra_type     = SutraType.SAMJNA,
    text_slp1      = "ArDaDAtukaM SezaH",
    text_dev       = "आर्धधातुकं शेषः",
    padaccheda_dev = "आर्धधातुकं शेषः",
    why_dev        = "शेषः प्रत्यय आर्धधातुक-संज्ञकः (तृच् इत्यादौ)।",
    anuvritti_from = ("3.4.113",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
