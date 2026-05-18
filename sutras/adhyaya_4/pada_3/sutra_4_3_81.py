"""
4.3.81  हेतुमनुष्येभ्योऽन्यतरस्यां रूप्यः  —  VIDHI

Padaccheda: हेतु-मनुष्येभ्यः अन्यतरस्याम् रूप्यः

हेतुमनुष्येभ्योऽन्यतरस्यां रूप्यः (4.3.81)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_81_hetumanuzy_81"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_81_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.81"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hetumanuzyeByo'nyatarasyAM rUpyaH",
    text_dev              = "हेतुमनुष्येभ्योऽन्यतरस्यां रूप्यः",
    padaccheda_dev        = "हेतु-मनुष्येभ्यः अन्यतरस्याम् रूप्यः",
    why_dev               = "(सूत्रम् 4.3.81) हेतुमनुष्येभ्योऽन्यतरस्यां रूप्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
