"""
6.1.89  एत्येधत्यूठ्सु  —  VIDHI

Padaccheda: एति-एधति-ऊठ्सु

एत्येधत्यूठ्सु (6.1.89)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_89_etyeDatyUW_89"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.89"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.89",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "etyeDatyUWsu",
    text_dev              = "एत्येधत्यूठ्सु",
    padaccheda_dev        = "एति-एधति-ऊठ्सु",
    why_dev               = "(सूत्रम् 6.1.89) एत्येधत्यूठ्सु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
