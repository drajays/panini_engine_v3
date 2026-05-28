"""
6.1.74  आङ्माङोश्च  —  VIDHI

Padaccheda: आङ्-माङोः च

आङ्माङोश्च (6.1.74)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_74_ANmANoSca_74"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.74"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ANmANoSca",
    text_dev              = "आङ्माङोश्च",
    padaccheda_dev        = "आङ्-माङोः च",
    why_dev               = "(सूत्रम् 6.1.74) आङ्माङोश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
