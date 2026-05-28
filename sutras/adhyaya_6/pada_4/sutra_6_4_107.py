"""
6.4.107  लोपश्चास्यान्यतरस्यां म्वोः  —  VIDHI

Padaccheda: लोपः च अस्य अन्यतरस्याम् म्वोः

लोपश्चास्यान्यतरस्यां म्वोः (6.4.107)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_107_lopaScAsyA_107"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.107", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.107"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lopaScAsyAnyatarasyAM mvoH",
    text_dev              = "लोपश्चास्यान्यतरस्यां म्वोः",
    padaccheda_dev        = "लोपः च अस्य अन्यतरस्याम् म्वोः",
    why_dev               = "(सूत्रम् 6.4.107) लोपश्चास्यान्यतरस्यां म्वोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
