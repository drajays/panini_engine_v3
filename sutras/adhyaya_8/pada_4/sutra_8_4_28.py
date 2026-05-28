"""
8.4.28  उपसर्गाद् बहुलम्  —  VIDHI

Padaccheda: उपसर्गात् अन्-ओत्-परः

उपसर्गाद् बहुलम् (8.4.28)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_28_upasargAd_28"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasargAd bahulam",
    text_dev              = "उपसर्गाद् बहुलम्",
    padaccheda_dev        = "उपसर्गात् अन्-ओत्-परः",
    why_dev               = "(सूत्रम् 8.4.28) उपसर्गाद् बहुलम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
