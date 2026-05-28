"""
6.2.161  विभाषा तृन्नन्नतीक्ष्णशुचिषु  —  VIDHI

Padaccheda: विभाषा तृन्-अन्न-तीक्ष्ण-शुचिषु

विभाषा तृन्नन्नतीक्ष्णशुचिषु (6.2.161)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_161_viBAzA_161"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.161"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.161",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA tfnnannatIkzRaSucizu",
    text_dev              = "विभाषा तृन्नन्नतीक्ष्णशुचिषु",
    padaccheda_dev        = "विभाषा तृन्-अन्न-तीक्ष्ण-शुचिषु",
    why_dev               = "(सूत्रम् 6.2.161) विभाषा तृन्नन्नतीक्ष्णशुचिषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
