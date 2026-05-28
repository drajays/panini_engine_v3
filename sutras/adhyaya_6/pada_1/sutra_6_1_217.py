"""
6.1.217  उपोत्तमं रिति  —  VIDHI

Padaccheda: उप-उत्तमम् रिति

उपोत्तमं रिति (6.1.217)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_217_upottamaM_217"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_217_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.217"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.217",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upottamaM riti",
    text_dev              = "उपोत्तमं रिति",
    padaccheda_dev        = "उप-उत्तमम् रिति",
    why_dev               = "(सूत्रम् 6.1.217) उपोत्तमं रिति।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
