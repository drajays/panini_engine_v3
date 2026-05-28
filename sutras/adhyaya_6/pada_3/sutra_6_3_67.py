"""
6.3.67  अरुर्द्विषदजन्तस्य मुम्  —  VIDHI

Padaccheda: अरुः-द्विषत्-अच्-अन्तस्य मुम्

अरुर्द्विषदजन्तस्य मुम् (6.3.67)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_67_arurdvizad_67"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "arurdvizadajantasya mum",
    text_dev              = "अरुर्द्विषदजन्तस्य मुम्",
    padaccheda_dev        = "अरुः-द्विषत्-अच्-अन्तस्य मुम्",
    why_dev               = "(सूत्रम् 6.3.67) अरुर्द्विषदजन्तस्य मुम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
