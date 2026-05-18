"""
4.2.18  दध्नष्ठक्  —  VIDHI

Padaccheda: दध्नः ठक्

दध्नष्ठक् (4.2.18)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_18_daDnazWak_18"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_18_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "daDnazWak",
    text_dev              = "दध्नष्ठक्",
    padaccheda_dev        = "दध्नः ठक्",
    why_dev               = "(सूत्रम् 4.2.18) दध्नष्ठक्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
