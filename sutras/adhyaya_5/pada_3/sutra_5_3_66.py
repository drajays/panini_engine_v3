"""
5.3.66  प्रशंसायां रूपप्  —  VIDHI

Padaccheda: प्रशंसायाम् रूपप्

प्रशंसायां रूपप् (5.3.66)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_66_praSaMsAyA_66"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_66_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "praSaMsAyAM rUpap",
    text_dev              = "प्रशंसायां रूपप्",
    padaccheda_dev        = "प्रशंसायाम् रूपप्",
    why_dev               = "(सूत्रम् 5.3.66) प्रशंसायां रूपप्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
