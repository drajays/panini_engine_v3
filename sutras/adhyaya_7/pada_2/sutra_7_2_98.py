"""
7.2.98  प्रत्ययोत्तरपदयोश्च  —  VIDHI

Padaccheda: प्रत्यय-उत्तरपदयोः च

प्रत्ययोत्तरपदयोश्च (7.2.98)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_98_pratyayott_98"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.98", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.98"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pratyayottarapadayoSca",
    text_dev              = "प्रत्ययोत्तरपदयोश्च",
    padaccheda_dev        = "प्रत्यय-उत्तरपदयोः च",
    why_dev               = "(सूत्रम् 7.2.98) प्रत्ययोत्तरपदयोश्च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
