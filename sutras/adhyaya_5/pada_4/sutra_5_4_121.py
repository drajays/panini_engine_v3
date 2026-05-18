"""
5.4.121  नञ्दुःसुभ्यो हलिसक्थ्योरन्यतरस्याम्  —  VIDHI

Padaccheda: नञ्-दुः-सुभ्यः हलि-सक्थ्योः अन्यतरस्याम्

नञ्दुःसुभ्यो हलिसक्थ्योरन्यतरस्याम् (5.4.121)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_121_naYduHsuBy_121"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_121_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "naYduHsuByo halisakTyoranyatarasyAm",
    text_dev              = "नञ्दुःसुभ्यो हलिसक्थ्योरन्यतरस्याम्",
    padaccheda_dev        = "नञ्-दुः-सुभ्यः हलि-सक्थ्योः अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 5.4.121) नञ्दुःसुभ्यो हलिसक्थ्योरन्यतरस्याम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
