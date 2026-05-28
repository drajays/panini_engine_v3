"""
6.1.191  सर्वस्य सुपि  —  VIDHI

Padaccheda: सर्वस्य सुपि

सर्वस्य सुपि (6.1.191)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_191_sarvasya_191"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_191_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.191"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.191",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sarvasya supi",
    text_dev              = "सर्वस्य सुपि",
    padaccheda_dev        = "सर्वस्य सुपि",
    why_dev               = "(सूत्रम् 6.1.191) सर्वस्य सुपि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
