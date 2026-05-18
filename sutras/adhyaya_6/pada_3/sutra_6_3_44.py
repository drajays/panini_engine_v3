"""
6.3.44  नद्याः शेषस्यान्यतरस्याम्  —  VIDHI

Padaccheda: नद्याः शेषस्य अन्यतरस्याम्

नद्याः शेषस्यान्यतरस्याम् (6.3.44)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_44_nadyAH_44"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_44_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nadyAH SezasyAnyatarasyAm",
    text_dev              = "नद्याः शेषस्यान्यतरस्याम्",
    padaccheda_dev        = "नद्याः शेषस्य अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 6.3.44) नद्याः शेषस्यान्यतरस्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
