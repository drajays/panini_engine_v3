"""
6.4.98  गमहनजनखनघसां लोपः क्ङित्यनङि  —  VIDHI

Padaccheda: गम-हन-जन-खन-घसाम् लोपः क्ङिति अन्-अङि

गमहनजनखनघसां लोपः क्ङित्यनङि (6.4.98)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_98_gamahanaja_98"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.98", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.98"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gamahanajanaKanaGasAM lopaH kNityanaNi",
    text_dev              = "गमहनजनखनघसां लोपः क्ङित्यनङि",
    padaccheda_dev        = "गम-हन-जन-खन-घसाम् लोपः क्ङिति अन्-अङि",
    why_dev               = "(सूत्रम् 6.4.98) गमहनजनखनघसां लोपः क्ङित्यनङि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
