"""
6.1.51  विभाषा लीयतेः  —  VIDHI

Padaccheda: विभाषा लीयतेः

विभाषा लीयतेः (6.1.51)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_51_viBAzA_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA lIyateH",
    text_dev              = "विभाषा लीयतेः",
    padaccheda_dev        = "विभाषा लीयतेः",
    why_dev               = "(सूत्रम् 6.1.51) विभाषा लीयतेः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
