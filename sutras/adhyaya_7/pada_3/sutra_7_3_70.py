"""
7.3.70  घोर्लोपो लेटि वा  —  VIDHI

Padaccheda: घोः लोपः लेटि वा

घोर्लोपो लेटि वा (7.3.70)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_70_Gorlopo_70"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_70_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Gorlopo lewi vA",
    text_dev              = "घोर्लोपो लेटि वा",
    padaccheda_dev        = "घोः लोपः लेटि वा",
    why_dev               = "(सूत्रम् 7.3.70) घोर्लोपो लेटि वा।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
