"""
6.2.182  परेरभितोभाविमण्डलम्  —  VIDHI

Padaccheda: परेः अभितोभावि मण्डलम्

परेरभितोभाविमण्डलम् (6.2.182)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_182_pareraBito_182"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.182"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.182",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pareraBitoBAvimaRqalam",
    text_dev              = "परेरभितोभाविमण्डलम्",
    padaccheda_dev        = "परेः अभितोभावि मण्डलम्",
    why_dev               = "(सूत्रम् 6.2.182) परेरभितोभाविमण्डलम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
