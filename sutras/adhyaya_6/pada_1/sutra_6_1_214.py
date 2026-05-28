"""
6.1.214  ईडवन्दवृशंसदुहां ण्यतः  —  VIDHI

Padaccheda: ईड-वन्द-वृ-शंस-दुहाम् ण्यतः

ईडवन्दवृशंसदुहां ण्यतः (6.1.214)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_214_Iqavandavf_214"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.214"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.214",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "IqavandavfSaMsaduhAM RyataH",
    text_dev              = "ईडवन्दवृशंसदुहां ण्यतः",
    padaccheda_dev        = "ईड-वन्द-वृ-शंस-दुहाम् ण्यतः",
    why_dev               = "(सूत्रम् 6.1.214) ईडवन्दवृशंसदुहां ण्यतः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
