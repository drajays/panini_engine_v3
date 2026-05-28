"""
6.4.89  ऊदुपधाया गोहः  —  VIDHI

Padaccheda: ऊत् उपधायाः गोहः

ऊदुपधाया गोहः (6.4.89)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_89_UdupaDAyA_89"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.89", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.89"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.89",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "UdupaDAyA gohaH",
    text_dev              = "ऊदुपधाया गोहः",
    padaccheda_dev        = "ऊत् उपधायाः गोहः",
    why_dev               = "(सूत्रम् 6.4.89) ऊदुपधाया गोहः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
