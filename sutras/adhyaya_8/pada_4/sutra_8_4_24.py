"""
8.4.24  अन्तरदेशे  —  VIDHI

Padaccheda: अन्तः अदेशे

अन्तरदेशे (8.4.24)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_24_antaradeSe_24"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "antaradeSe",
    text_dev              = "अन्तरदेशे",
    padaccheda_dev        = "अन्तः अदेशे",
    why_dev               = "(सूत्रम् 8.4.24) अन्तरदेशे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
