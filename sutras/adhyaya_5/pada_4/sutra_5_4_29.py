"""
5.4.29  यावादिभ्यः कन्  —  VIDHI

Padaccheda: याव-आदिभ्यः कन्

यावादिभ्यः कन् (5.4.29)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_29_yAvAdiByaH_29"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_29_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yAvAdiByaH kan",
    text_dev              = "यावादिभ्यः कन्",
    padaccheda_dev        = "याव-आदिभ्यः कन्",
    why_dev               = "(सूत्रम् 5.4.29) यावादिभ्यः कन्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
