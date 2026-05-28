"""
6.4.147  ढे लोपोऽकद्र्वाः  —  VIDHI

Padaccheda: ढे लोपः अकद्र्वाः

ढे लोपोऽकद्र्वाः (6.4.147)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_147_Qe_147"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.147", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.147"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.147",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Qe lopo'kadrvAH",
    text_dev              = "ढे लोपोऽकद्र्वाः",
    padaccheda_dev        = "ढे लोपः अकद्र्वाः",
    why_dev               = "(सूत्रम् 6.4.147) ढे लोपोऽकद्र्वाः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
