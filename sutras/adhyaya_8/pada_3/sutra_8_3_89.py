"""
8.3.89  निनदीभ्यां स्नातेः कौशले  —  VIDHI

Padaccheda: नि-नदीभ्याम् स्नातेः कौशले

निनदीभ्यां स्नातेः कौशले (8.3.89)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_89_ninadIByAM_89"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_89_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.89"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.89",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ninadIByAM snAteH kOSale",
    text_dev              = "निनदीभ्यां स्नातेः कौशले",
    padaccheda_dev        = "नि-नदीभ्याम् स्नातेः कौशले",
    why_dev               = "(सूत्रम् 8.3.89) निनदीभ्यां स्नातेः कौशले।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
