"""
6.2.163  संख्यायाः स्तनः  —  VIDHI

Padaccheda: संख्यायाः स्तनः

संख्यायाः स्तनः (6.2.163)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_163_saMKyAyAH_163"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_163_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.163"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.163",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMKyAyAH stanaH",
    text_dev              = "संख्यायाः स्तनः",
    padaccheda_dev        = "संख्यायाः स्तनः",
    why_dev               = "(सूत्रम् 6.2.163) संख्यायाः स्तनः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
