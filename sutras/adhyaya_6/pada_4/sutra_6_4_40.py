"""
6.4.40  गमः क्वौ  —  VIDHI

Padaccheda: गमः क्वौ

गमः क्वौ (6.4.40)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_40_gamaH_40"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.40", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.40"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gamaH kvO",
    text_dev              = "गमः क्वौ",
    padaccheda_dev        = "गमः क्वौ",
    why_dev               = "(सूत्रम् 6.4.40) गमः क्वौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
