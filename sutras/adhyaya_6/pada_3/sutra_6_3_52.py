"""
6.3.52  पादस्य पदाज्यातिगोपहतेषु  —  VIDHI

Padaccheda: पादस्य पद (लुप्तप्रथमान्तनिर्देशः) आजि-आति-गोप-हतेषु

पादस्य पदाज्यातिगोपहतेषु (6.3.52)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_52_pAdasya_52"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pAdasya padAjyAtigopahatezu",
    text_dev              = "पादस्य पदाज्यातिगोपहतेषु",
    padaccheda_dev        = "पादस्य पद (लुप्तप्रथमान्तनिर्देशः) आजि-आति-गोप-हतेषु",
    why_dev               = "(सूत्रम् 6.3.52) पादस्य पदाज्यातिगोपहतेषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
