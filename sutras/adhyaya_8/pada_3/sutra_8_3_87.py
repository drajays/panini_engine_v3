"""
8.3.87  उपसर्गप्रादुर्भ्यामस्तिर्यच्परः  —  VIDHI

Padaccheda: उपसर्ग-प्रादुर्भ्याम् अस्तिः य्-अच्-परः

उपसर्गप्रादुर्भ्यामस्तिर्यच्परः (8.3.87)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_87_upasargapr_87"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.87"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasargaprAdurByAmastiryacparaH",
    text_dev              = "उपसर्गप्रादुर्भ्यामस्तिर्यच्परः",
    padaccheda_dev        = "उपसर्ग-प्रादुर्भ्याम् अस्तिः य्-अच्-परः",
    why_dev               = "(सूत्रम् 8.3.87) उपसर्गप्रादुर्भ्यामस्तिर्यच्परः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
