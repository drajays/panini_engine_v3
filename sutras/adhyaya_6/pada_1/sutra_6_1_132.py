"""
6.1.132  एतत्तदोः सुलोपोऽकोरनञ्समासे हलि  —  VIDHI

Padaccheda: एतद्-तदोः सु-लोपः अ-कोः अ-नञ्-समासे हलि

एतत्तदोः सुलोपोऽकोरनञ्समासे हलि (6.1.132)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_132_etattadoH_132"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.132"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.132",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "etattadoH sulopo'koranaYsamAse hali",
    text_dev              = "एतत्तदोः सुलोपोऽकोरनञ्समासे हलि",
    padaccheda_dev        = "एतद्-तदोः सु-लोपः अ-कोः अ-नञ्-समासे हलि",
    why_dev               = "(सूत्रम् 6.1.132) एतत्तदोः सुलोपोऽकोरनञ्समासे हलि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
