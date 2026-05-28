"""
3.2.9  हरतेरनुद्यमनेऽच्  —  VIDHI

Padaccheda: हरतेः अनुद्यमने अच्

krt-suffix rule: हरतेरनुद्यमनेऽच् (9)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_9_harateranu_9"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "harateranudyamane'c",
    text_dev              = "हरतेरनुद्यमनेऽच्",
    padaccheda_dev        = "हरतेः अनुद्यमने अच्",
    why_dev               = "धातोः कृत्-प्रत्ययः [हरतेरनुद्यमनेऽच्] विहितः (३.२.9)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
