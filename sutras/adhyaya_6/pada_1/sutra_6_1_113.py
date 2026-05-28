"""
6.1.113  अतो रोरप्लुतादप्लुते  —  VIDHI

Padaccheda: अतः · रोः · अप्लुतात् · अप्लुते

अतो रोरप्लुतादप्लुते (6.1.113)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_113_ato_113"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.113"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.113",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ato roraplutAdaplute",
    text_dev              = "अतो रोरप्लुतादप्लुते",
    padaccheda_dev        = "अतः · रोः · अप्लुतात् · अप्लुते",
    why_dev               = "(सूत्रम् 6.1.113) अतो रोरप्लुतादप्लुते।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
