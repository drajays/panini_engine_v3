"""
2.3.28  अपादाने पञ्चमी  —  VIDHI

Padaccheda: अपादाने पञ्चमी

Pancami marks the apadana (ablative) role.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_28_apadane_pancami"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "apAdAne paYcamI",
    text_dev              = "अपादाने पञ्चमी",
    padaccheda_dev        = "अपादाने पञ्चमी",
    why_dev               = "अपादाने पञ्चमी (२.३.२८)।",
    anuvritti_from        = ('2.3.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
