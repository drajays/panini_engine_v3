"""
4.3.71  छन्दसो यदणौ  —  VIDHI

Padaccheda: छन्दसः यत्-अणौ

छन्दसो यदणौ (4.3.71)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_71_Candaso_71"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_71_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.71"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.71",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Candaso yadaRO",
    text_dev              = "छन्दसो यदणौ",
    padaccheda_dev        = "छन्दसः यत्-अणौ",
    why_dev               = "(सूत्रम् 4.3.71) छन्दसो यदणौ।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
