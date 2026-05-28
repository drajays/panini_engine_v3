"""
6.2.46  कर्मधारयेऽनिष्ठा  —  VIDHI

Padaccheda: कर्मधारये अ-निष्ठा

कर्मधारयेऽनिष्ठा (6.2.46)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_46_karmaDAray_46"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaDAraye'nizWA",
    text_dev              = "कर्मधारयेऽनिष्ठा",
    padaccheda_dev        = "कर्मधारये अ-निष्ठा",
    why_dev               = "(सूत्रम् 6.2.46) कर्मधारयेऽनिष्ठा।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
