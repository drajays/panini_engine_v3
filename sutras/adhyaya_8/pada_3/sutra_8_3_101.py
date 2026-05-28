"""
8.3.101  ह्रस्वात् तादौ तद्धिते  —  VIDHI

Padaccheda: ह्रस्वात् त-आदौ तद्धिते

ह्रस्वात् तादौ तद्धिते (8.3.101)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_101_hrasvAt_101"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_101_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.101"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.101",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hrasvAt tAdO tadDite",
    text_dev              = "ह्रस्वात् तादौ तद्धिते",
    padaccheda_dev        = "ह्रस्वात् त-आदौ तद्धिते",
    why_dev               = "(सूत्रम् 8.3.101) ह्रस्वात् तादौ तद्धिते।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
