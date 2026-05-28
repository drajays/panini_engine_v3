"""
8.2.32  दादेर्धातोर्घः  —  VIDHI

Padaccheda: <BV>&()द्&()आदेः धातोः घः

दादेर्धातोर्घः (8.2.32)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_32_dAderDAtor_32"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dAderDAtorGaH",
    text_dev              = "दादेर्धातोर्घः",
    padaccheda_dev        = "<BV>&()द्&()आदेः धातोः घः",
    why_dev               = "(सूत्रम् 8.2.32) दादेर्धातोर्घः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
