"""
4.3.17  प्रावृष एण्यः  —  VIDHI

Padaccheda: प्रावृषः एण्यः

प्रावृष एण्यः (4.3.17)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_17_prAvfza_17"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_17_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prAvfza eRyaH",
    text_dev              = "प्रावृष एण्यः",
    padaccheda_dev        = "प्रावृषः एण्यः",
    why_dev               = "(सूत्रम् 4.3.17) प्रावृष एण्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
