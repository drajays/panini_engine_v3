"""
8.1.55  आम एकान्तरमामन्त्रितमनन्तिके  —  VIDHI

Padaccheda: आम एकान्तरम् आमन्त्रितम् अनन्तिके

आम एकान्तरमामन्त्रितमनन्तिके (8.1.55)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_55_Ama_55"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Ama ekAntaramAmantritamanantike",
    text_dev              = "आम एकान्तरमामन्त्रितमनन्तिके",
    padaccheda_dev        = "आम एकान्तरम् आमन्त्रितम् अनन्तिके",
    why_dev               = "(सूत्रम् 8.1.55) आम एकान्तरमामन्त्रितमनन्तिके।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
