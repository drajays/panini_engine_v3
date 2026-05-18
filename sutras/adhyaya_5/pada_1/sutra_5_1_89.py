"""
5.1.89  चित्तवति नित्यम्  —  VIDHI

Padaccheda: चित्तवति नित्यम्

चित्तवति नित्यम् (5.1.89)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_89_cittavati_89"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_89_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.89"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.89",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "cittavati nityam",
    text_dev              = "चित्तवति नित्यम्",
    padaccheda_dev        = "चित्तवति नित्यम्",
    why_dev               = "(सूत्रम् 5.1.89) चित्तवति नित्यम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
