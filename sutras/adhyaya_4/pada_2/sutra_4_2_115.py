"""
4.2.115  भवतष्ठक्छसौ  —  VIDHI

Padaccheda: भवतः ठक्-छसौ

भवतष्ठक्छसौ (4.2.115)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_115_BavatazWak_115"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_115_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.115"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.115",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BavatazWakCasO",
    text_dev              = "भवतष्ठक्छसौ",
    padaccheda_dev        = "भवतः ठक्-छसौ",
    why_dev               = "(सूत्रम् 4.2.115) भवतष्ठक्छसौ।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
