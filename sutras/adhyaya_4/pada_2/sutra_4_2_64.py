"""
4.2.64  प्रोक्ताल्लुक्  —  VIDHI

Padaccheda: प्रोक्तात् लुक्

प्रोक्ताल्लुक् (4.2.64)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_64_proktAlluk_64"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_64_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.64"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.64",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "proktAlluk",
    text_dev              = "प्रोक्ताल्लुक्",
    padaccheda_dev        = "प्रोक्तात् लुक्",
    why_dev               = "(सूत्रम् 4.2.64) प्रोक्ताल्लुक्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
