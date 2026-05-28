"""
6.1.56  बिभेतेर्हेतुभये  —  VIDHI

Padaccheda: बिभेतेः हेतुभये

बिभेतेर्हेतुभये (6.1.56)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_56_biBeterhet_56"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "biBeterhetuBaye",
    text_dev              = "बिभेतेर्हेतुभये",
    padaccheda_dev        = "बिभेतेः हेतुभये",
    why_dev               = "(सूत्रम् 6.1.56) बिभेतेर्हेतुभये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
