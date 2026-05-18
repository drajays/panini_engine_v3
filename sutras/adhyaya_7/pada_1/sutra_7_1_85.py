"""
7.1.85  पथिमथ्यृभुक्षामात्  —  VIDHI

Padaccheda: पथि-मथि-ऋभुक्षाम् आत्

पथिमथ्यृभुक्षामात् (7.1.85)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_1_85_paTimaTyfB_85"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_1_85_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.85"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.85",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paTimaTyfBukzAmAt",
    text_dev              = "पथिमथ्यृभुक्षामात्",
    padaccheda_dev        = "पथि-मथि-ऋभुक्षाम् आत्",
    why_dev               = "(सूत्रम् 7.1.85) पथिमथ्यृभुक्षामात्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
