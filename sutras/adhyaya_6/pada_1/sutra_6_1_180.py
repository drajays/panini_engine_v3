"""
6.1.180  झल्युपोत्तमम्  —  VIDHI

Padaccheda: झलि उप-उत्तमम्

झल्युपोत्तमम् (6.1.180)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_180_Jalyupotta_180"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_180_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.180"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.180",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Jalyupottamam",
    text_dev              = "झल्युपोत्तमम्",
    padaccheda_dev        = "झलि उप-उत्तमम्",
    why_dev               = "(सूत्रम् 6.1.180) झल्युपोत्तमम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
