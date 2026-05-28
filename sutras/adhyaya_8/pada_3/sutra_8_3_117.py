"""
8.3.117  सुनोतेः स्यसनोः  —  VIDHI

Padaccheda: सुनोतेः स्य-सनोः

सुनोतेः स्यसनोः (8.3.117)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_117_sunoteH_117"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.117"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.117",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sunoteH syasanoH",
    text_dev              = "सुनोतेः स्यसनोः",
    padaccheda_dev        = "सुनोतेः स्य-सनोः",
    why_dev               = "(सूत्रम् 8.3.117) सुनोतेः स्यसनोः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
