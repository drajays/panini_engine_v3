"""
6.1.49  सिध्यतेरपारलौकिके  —  VIDHI

Padaccheda: सिध्यतेः अपारलौकिके

सिध्यतेरपारलौकिके (6.1.49)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_49_siDyaterap_49"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_49_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "siDyaterapAralOkike",
    text_dev              = "सिध्यतेरपारलौकिके",
    padaccheda_dev        = "सिध्यतेः अपारलौकिके",
    why_dev               = "(सूत्रम् 6.1.49) सिध्यतेरपारलौकिके।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
