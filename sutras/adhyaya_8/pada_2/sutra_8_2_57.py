"""
8.2.57  न ध्याख्यापॄमूर्छिमदाम्  —  VIDHI

Padaccheda: न ध्या-ख्या-पॄ-मूर्छि-मदाम्

न ध्याख्यापॄमूर्छिमदाम् (8.2.57)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_57_na_57"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_57_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na DyAKyApFmUrCimadAm",
    text_dev              = "न ध्याख्यापॄमूर्छिमदाम्",
    padaccheda_dev        = "न ध्या-ख्या-पॄ-मूर्छि-मदाम्",
    why_dev               = "(सूत्रम् 8.2.57) न ध्याख्यापॄमूर्छिमदाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
