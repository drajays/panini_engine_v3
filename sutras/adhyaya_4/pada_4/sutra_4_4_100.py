"""
4.4.100  भक्ताण्णः  —  VIDHI

Padaccheda: भक्तात् णः

भक्ताण्णः (4.4.100)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_100_BaktARRaH_100"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_100_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.100"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BaktARRaH",
    text_dev              = "भक्ताण्णः",
    padaccheda_dev        = "भक्तात् णः",
    why_dev               = "(सूत्रम् 4.4.100) भक्ताण्णः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
