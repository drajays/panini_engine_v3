"""
6.2.24  विस्पष्टादीनि गुणवचनेषु  —  VIDHI

Padaccheda: विस्पष्ट-आदीनि गुणवचनेषु

विस्पष्टादीनि गुणवचनेषु (6.2.24)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_24_vispazwAdI_24"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vispazwAdIni guRavacanezu",
    text_dev              = "विस्पष्टादीनि गुणवचनेषु",
    padaccheda_dev        = "विस्पष्ट-आदीनि गुणवचनेषु",
    why_dev               = "(सूत्रम् 6.2.24) विस्पष्टादीनि गुणवचनेषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
