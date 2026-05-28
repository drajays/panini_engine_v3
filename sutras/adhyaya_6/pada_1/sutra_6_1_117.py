"""
6.1.117  यजुष्युरः  —  VIDHI

Padaccheda: यजुषि उरः

यजुष्युरः (6.1.117)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_117_yajuzyuraH_117"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.117"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.117",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yajuzyuraH",
    text_dev              = "यजुष्युरः",
    padaccheda_dev        = "यजुषि उरः",
    why_dev               = "(सूत्रम् 6.1.117) यजुष्युरः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
