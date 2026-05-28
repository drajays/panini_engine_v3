"""
6.1.206  शुष्कधृष्टौ  —  VIDHI

Padaccheda: शुष्क-धृष्टौ

शुष्कधृष्टौ (6.1.206)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_206_SuzkaDfzwO_206"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.206"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.206",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SuzkaDfzwO",
    text_dev              = "शुष्कधृष्टौ",
    padaccheda_dev        = "शुष्क-धृष्टौ",
    why_dev               = "(सूत्रम् 6.1.206) शुष्कधृष्टौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
