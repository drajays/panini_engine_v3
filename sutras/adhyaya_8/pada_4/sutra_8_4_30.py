"""
8.4.30  णेर्विभाषा  —  VIDHI

Padaccheda: णेः विभाषा

णेर्विभाषा (8.4.30)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_30_RerviBAzA_30"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_4_30_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.30"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.30",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "RerviBAzA",
    text_dev              = "णेर्विभाषा",
    padaccheda_dev        = "णेः विभाषा",
    why_dev               = "(सूत्रम् 8.4.30) णेर्विभाषा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
