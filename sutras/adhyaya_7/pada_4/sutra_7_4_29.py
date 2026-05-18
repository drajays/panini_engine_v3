"""
7.4.29  गुणोऽर्तिसंयोगाद्योः  —  VIDHI

Padaccheda: गुणः अर्ति-संयोग-आद्योः

गुणोऽर्तिसंयोगाद्योः (7.4.29)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_29_guRortisa_29"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_29_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "guRo'rtisaMyogAdyoH",
    text_dev              = "गुणोऽर्तिसंयोगाद्योः",
    padaccheda_dev        = "गुणः अर्ति-संयोग-आद्योः",
    why_dev               = "(सूत्रम् 7.4.29) गुणोऽर्तिसंयोगाद्योः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
