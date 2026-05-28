"""
8.4.11  प्रातिपदिकान्तनुम्विभक्तिषु च  —  VIDHI

Padaccheda: प्रातिपदिक-अन्त-नुम्-विभक्तिषु च

प्रातिपदिकान्तनुम्विभक्तिषु च (8.4.11)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_11_prAtipadik_11"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.11"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.11",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prAtipadikAntanumviBaktizu ca",
    text_dev              = "प्रातिपदिकान्तनुम्विभक्तिषु च",
    padaccheda_dev        = "प्रातिपदिक-अन्त-नुम्-विभक्तिषु च",
    why_dev               = "(सूत्रम् 8.4.11) प्रातिपदिकान्तनुम्विभक्तिषु च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
