"""
8.3.119  निव्यभिभ्योऽड्व्यावये वा छन्दसि  —  VIDHI

Padaccheda: नि-वि-अभिभ्यः अट्-व्यवाये वा छन्दसि

निव्यभिभ्योऽड्व्यावये वा छन्दसि (8.3.119)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_119_nivyaBiByo_119"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_119_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.119"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.119",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nivyaBiByo'qvyAvaye vA Candasi",
    text_dev              = "निव्यभिभ्योऽड्व्यावये वा छन्दसि",
    padaccheda_dev        = "नि-वि-अभिभ्यः अट्-व्यवाये वा छन्दसि",
    why_dev               = "(सूत्रम् 8.3.119) निव्यभिभ्योऽड्व्यावये वा छन्दसि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
