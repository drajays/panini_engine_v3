"""
4.4.94  उरसोऽण् च  —  VIDHI

Padaccheda: उरसः अण् च

उरसोऽण् च (4.4.94)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_94_urasoR_94"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_94_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uraso'R ca",
    text_dev              = "उरसोऽण् च",
    padaccheda_dev        = "उरसः अण् च",
    why_dev               = "(सूत्रम् 4.4.94) उरसोऽण् च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
