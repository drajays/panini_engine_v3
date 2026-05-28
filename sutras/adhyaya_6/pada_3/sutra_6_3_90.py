"""
6.3.90  इदङ्किमोरीश्की  —  VIDHI

Padaccheda: इदम्-किमोः ईश्-की (लुप्तप्रथमान्तनिर्देशः)

इदङ्किमोरीश्की (6.3.90)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_90_idaNkimorI_90"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.90"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "idaNkimorISkI",
    text_dev              = "इदङ्किमोरीश्की",
    padaccheda_dev        = "इदम्-किमोः ईश्-की (लुप्तप्रथमान्तनिर्देशः)",
    why_dev               = "(सूत्रम् 6.3.90) इदङ्किमोरीश्की।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
