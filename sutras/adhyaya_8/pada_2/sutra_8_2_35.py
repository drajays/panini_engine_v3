"""
8.2.35  आहस्थः  —  VIDHI

Padaccheda: आहः थः

आहस्थः (8.2.35)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_35_AhasTaH_35"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_35_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AhasTaH",
    text_dev              = "आहस्थः",
    padaccheda_dev        = "आहः थः",
    why_dev               = "(सूत्रम् 8.2.35) आहस्थः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
