"""
8.4.57  अणोऽप्रगृह्यस्यानुनासिकः  —  VIDHI

Padaccheda: अणः अ-प्रगृह्यस्य अनुनासिकः

अणोऽप्रगृह्यस्यानुनासिकः (8.4.57)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_57_aRopragfh_57"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_4_57_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aRo'pragfhyasyAnunAsikaH",
    text_dev              = "अणोऽप्रगृह्यस्यानुनासिकः",
    padaccheda_dev        = "अणः अ-प्रगृह्यस्य अनुनासिकः",
    why_dev               = "(सूत्रम् 8.4.57) अणोऽप्रगृह्यस्यानुनासिकः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
