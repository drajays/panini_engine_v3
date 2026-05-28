"""
8.2.71  भुवश्च महाव्याहृतेः  —  VIDHI

Padaccheda: भुवः (अविभक्तिकम्) च महाव्याहृतेः

भुवश्च महाव्याहृतेः (8.2.71)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_71_BuvaSca_71"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.71"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.71",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BuvaSca mahAvyAhfteH",
    text_dev              = "भुवश्च महाव्याहृतेः",
    padaccheda_dev        = "भुवः (अविभक्तिकम्) च महाव्याहृतेः",
    why_dev               = "(सूत्रम् 8.2.71) भुवश्च महाव्याहृतेः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
