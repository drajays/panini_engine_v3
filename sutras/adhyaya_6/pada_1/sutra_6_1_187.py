"""
6.1.187  आदिः सिचोऽन्यतरस्याम्  —  VIDHI

Padaccheda: आदिः सिचः अन्यतरस्याम्

आदिः सिचोऽन्यतरस्याम् (6.1.187)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_187_AdiH_187"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_187_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.187"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.187",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AdiH sico'nyatarasyAm",
    text_dev              = "आदिः सिचोऽन्यतरस्याम्",
    padaccheda_dev        = "आदिः सिचः अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 6.1.187) आदिः सिचोऽन्यतरस्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
