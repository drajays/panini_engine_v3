"""
8.3.90  सूत्रं प्रतिष्णातम्  —  VIDHI

Padaccheda: सूत्रम् प्रतिष्णातम्

सूत्रं प्रतिष्णातम् (8.3.90)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_90_sUtraM_90"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_90_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.90"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sUtraM pratizRAtam",
    text_dev              = "सूत्रं प्रतिष्णातम्",
    padaccheda_dev        = "सूत्रम् प्रतिष्णातम्",
    why_dev               = "(सूत्रम् 8.3.90) सूत्रं प्रतिष्णातम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
