"""
5.2.42  संख्याया अवयवे तयप्  —  VIDHI

Padaccheda: संख्यायाः अवयवे तयप्

संख्याया अवयवे तयप् (5.2.42)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_42_saMKyAyA_42"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_42_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMKyAyA avayave tayap",
    text_dev              = "संख्याया अवयवे तयप्",
    padaccheda_dev        = "संख्यायाः अवयवे तयप्",
    why_dev               = "(सूत्रम् 5.2.42) संख्याया अवयवे तयप्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
