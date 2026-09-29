"""
8.2.34  नहो धः  —  VIDHI

Padaccheda: नहः धः

नहो धः (8.2.34)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology    import mk
from sutras.adhyaya_8.pada_2._tape import (
    AC, BAS_TO_BHAS, JHAS, dhatu_span, flat, followed_by_jhal_or_end, slp, substitute,
)


def _site(state: State):
    if not state.tripadi_zone:
        return None
    c = flat(state)
    for k in range(len(c)):
        if slp(c[k]) != "h" or not followed_by_jhal_or_end(c, k):
            continue
        span = dhatu_span(c, k)
        if span and span[1] == k and "".join(slp(x) for x in c[span[0]:span[1] + 1]) == "nah":
            return c[k]
    return None


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    while (hit := _site(state)) is not None:
        substitute(hit, "D")
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.34",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "naho DaH",
    text_dev              = "नहो धः",
    padaccheda_dev        = "नहः धः",
    why_dev               = "नहो धः: the ह् of नह् → ध् (apavāda of 8.2.31) — नह्+त → नद्ध.",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
