"""
8.4.35  षात् पदान्तात्  —  VIDHI

Padaccheda: षात् पद-अन्तात्

षात् पदान्तात् (8.4.35)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_35_zAt_35"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_4_35_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zAt padAntAt",
    text_dev              = "षात् पदान्तात्",
    padaccheda_dev        = "षात् पद-अन्तात्",
    why_dev               = "(सूत्रम् 8.4.35) षात् पदान्तात्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
