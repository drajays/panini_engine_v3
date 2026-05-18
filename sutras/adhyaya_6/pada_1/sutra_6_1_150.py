"""
6.1.150  विष्किरः शकुनिर्विकरो वा  —  VIDHI

Padaccheda: विष्किरः शकुनौ वा

विष्किरः शकुनिर्विकरो वा (6.1.150)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_150_vizkiraH_150"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_150_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.150"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.150",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vizkiraH Sakunirvikaro vA",
    text_dev              = "विष्किरः शकुनिर्विकरो वा",
    padaccheda_dev        = "विष्किरः शकुनौ वा",
    why_dev               = "(सूत्रम् 6.1.150) विष्किरः शकुनिर्विकरो वा।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
