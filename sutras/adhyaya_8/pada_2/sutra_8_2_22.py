"""
8.2.22  परेश्च घाङ्कयोः  —  VIDHI

Padaccheda: परेः च घ-अङ्कयोः

परेश्च घाङ्कयोः (8.2.22)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_22_pareSca_22"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_22_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pareSca GANkayoH",
    text_dev              = "परेश्च घाङ्कयोः",
    padaccheda_dev        = "परेः च घ-अङ्कयोः",
    why_dev               = "(सूत्रम् 8.2.22) परेश्च घाङ्कयोः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
