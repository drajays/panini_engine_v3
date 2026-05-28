"""
6.1.178  ङ्याश्छन्दसि बहुलम्  —  VIDHI

Padaccheda: ङ्याः छन्दसि बहुलम्

ङ्याश्छन्दसि बहुलम् (6.1.178)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_178_NyASCandas_178"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.178"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.178",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "NyASCandasi bahulam",
    text_dev              = "ङ्याश्छन्दसि बहुलम्",
    padaccheda_dev        = "ङ्याः छन्दसि बहुलम्",
    why_dev               = "(सूत्रम् 6.1.178) ङ्याश्छन्दसि बहुलम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
