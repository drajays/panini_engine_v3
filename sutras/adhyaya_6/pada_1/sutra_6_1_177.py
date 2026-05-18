"""
6.1.177  नामन्यतरस्याम्  —  VIDHI

Padaccheda: नाम् अन्यतरस्याम्

नामन्यतरस्याम् (6.1.177)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_177_nAmanyatar_177"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_177_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.177"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.177",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nAmanyatarasyAm",
    text_dev              = "नामन्यतरस्याम्",
    padaccheda_dev        = "नाम् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 6.1.177) नामन्यतरस्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
