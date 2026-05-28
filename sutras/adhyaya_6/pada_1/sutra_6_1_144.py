"""
6.1.144  अपरस्पराः क्रियासातत्ये  —  VIDHI

Padaccheda: अपरस्पराः क्रियासातत्ये

अपरस्पराः क्रियासातत्ये (6.1.144)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_144_aparasparA_144"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_144_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.144"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.144",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aparasparAH kriyAsAtatye",
    text_dev              = "अपरस्पराः क्रियासातत्ये",
    padaccheda_dev        = "अपरस्पराः क्रियासातत्ये",
    why_dev               = "(सूत्रम् 6.1.144) अपरस्पराः क्रियासातत्ये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
