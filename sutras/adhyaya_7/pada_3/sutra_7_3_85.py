"""
7.3.85  जाग्रोऽविचिण्णल्ङित्सु  —  VIDHI

Padaccheda: जाग्रः अ-वि-चिण्-णल्-ङित्सु

जाग्रोऽविचिण्णल्ङित्सु (7.3.85)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_85_jAgrovici_85"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_85_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.85"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.85",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jAgro'viciRRalNitsu",
    text_dev              = "जाग्रोऽविचिण्णल्ङित्सु",
    padaccheda_dev        = "जाग्रः अ-वि-चिण्-णल्-ङित्सु",
    why_dev               = "(सूत्रम् 7.3.85) जाग्रोऽविचिण्णल्ङित्सु।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
