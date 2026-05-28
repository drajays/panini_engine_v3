"""
6.3.133  ऋचि तुनुघमक्षुतङ्कुत्रोरुष्याणाम्  —  VIDHI

Padaccheda: ऋचि तु-नु-घ-मक्षु-तङ्-कुत्र-उरुष्याणाम्

ऋचि तुनुघमक्षुतङ्कुत्रोरुष्याणाम् (6.3.133)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_133_fci_133"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.133"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.133",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fci tunuGamakzutaNkutroruzyARAm",
    text_dev              = "ऋचि तुनुघमक्षुतङ्कुत्रोरुष्याणाम्",
    padaccheda_dev        = "ऋचि तु-नु-घ-मक्षु-तङ्-कुत्र-उरुष्याणाम्",
    why_dev               = "(सूत्रम् 6.3.133) ऋचि तुनुघमक्षुतङ्कुत्रोरुष्याणाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
