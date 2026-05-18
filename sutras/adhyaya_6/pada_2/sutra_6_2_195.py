"""
6.2.195  सोरवक्षेपणे  —  VIDHI

Padaccheda: सोः अवक्षेपणे

सोरवक्षेपणे (6.2.195)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_195_soravakzep_195"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_195_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.195"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.195",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "soravakzepaRe",
    text_dev              = "सोरवक्षेपणे",
    padaccheda_dev        = "सोः अवक्षेपणे",
    why_dev               = "(सूत्रम् 6.2.195) सोरवक्षेपणे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
