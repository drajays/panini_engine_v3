"""
8.3.105  स्तुतस्तोमयोश्छन्दसि  —  VIDHI

Padaccheda: स्तुत-स्तोमयोः छन्दसि

स्तुतस्तोमयोश्छन्दसि (8.3.105)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_105_stutastoma_105"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_105_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.105"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.105",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "stutastomayoSCandasi",
    text_dev              = "स्तुतस्तोमयोश्छन्दसि",
    padaccheda_dev        = "स्तुत-स्तोमयोः छन्दसि",
    why_dev               = "(सूत्रम् 8.3.105) स्तुतस्तोमयोश्छन्दसि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
