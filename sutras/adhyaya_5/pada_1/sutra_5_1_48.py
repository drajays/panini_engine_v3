"""
5.1.48  पूरणार्धाट्ठन्  —  VIDHI

Padaccheda: पूरण-अर्धात् ठन्

पूरणार्धाट्ठन् (5.1.48)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_48_pUraRArDAw_48"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_48_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUraRArDAwWan",
    text_dev              = "पूरणार्धाट्ठन्",
    padaccheda_dev        = "पूरण-अर्धात् ठन्",
    why_dev               = "(सूत्रम् 5.1.48) पूरणार्धाट्ठन्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
