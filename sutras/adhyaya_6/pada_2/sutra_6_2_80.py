"""
6.2.80  उपमानं शब्दार्थप्रकृतावेव  —  VIDHI

Padaccheda: उपमानम् शब्दार्थप्रकृतौ एव

उपमानं शब्दार्थप्रकृतावेव (6.2.80)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_80_upamAnaM_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_80_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upamAnaM SabdArTaprakftAveva",
    text_dev              = "उपमानं शब्दार्थप्रकृतावेव",
    padaccheda_dev        = "उपमानम् शब्दार्थप्रकृतौ एव",
    why_dev               = "(सूत्रम् 6.2.80) उपमानं शब्दार्थप्रकृतावेव।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
