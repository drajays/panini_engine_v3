"""
8.4.23  वमोर्वा  —  VIDHI

Padaccheda: व-मोः वा

वमोर्वा (8.4.23)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_23_vamorvA_23"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_4_23_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vamorvA",
    text_dev              = "वमोर्वा",
    padaccheda_dev        = "व-मोः वा",
    why_dev               = "(सूत्रम् 8.4.23) वमोर्वा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
