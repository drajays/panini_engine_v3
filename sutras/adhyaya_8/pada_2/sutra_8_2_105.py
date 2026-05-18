"""
8.2.105  अनन्त्यस्यापि प्रश्नाख्यानयोः  —  VIDHI

Padaccheda: अन्-अन्त्यस्य अपि प्रश्न-आख्यानयोः

अनन्त्यस्यापि प्रश्नाख्यानयोः (8.2.105)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_105_anantyasyA_105"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_105_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.105"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.105",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anantyasyApi praSnAKyAnayoH",
    text_dev              = "अनन्त्यस्यापि प्रश्नाख्यानयोः",
    padaccheda_dev        = "अन्-अन्त्यस्य अपि प्रश्न-आख्यानयोः",
    why_dev               = "(सूत्रम् 8.2.105) अनन्त्यस्यापि प्रश्नाख्यानयोः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
