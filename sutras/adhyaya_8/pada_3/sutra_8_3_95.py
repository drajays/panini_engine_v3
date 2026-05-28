"""
8.3.95  गवियुधिभ्यां स्थिरः  —  VIDHI

Padaccheda: गवि-युधिभ्याम् स्थिरः

गवियुधिभ्यां स्थिरः (8.3.95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_95_gaviyuDiBy_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_95_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gaviyuDiByAM sTiraH",
    text_dev              = "गवियुधिभ्यां स्थिरः",
    padaccheda_dev        = "गवि-युधिभ्याम् स्थिरः",
    why_dev               = "(सूत्रम् 8.3.95) गवियुधिभ्यां स्थिरः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
