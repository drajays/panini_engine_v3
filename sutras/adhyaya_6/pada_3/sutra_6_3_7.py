"""
6.3.7  वैयाकरणाख्यायां चतुर्थ्याः  —  VIDHI

Padaccheda: वैयाकरणाख्यायाम् चतुर्थ्याः

वैयाकरणाख्यायां चतुर्थ्याः (6.3.7)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_7_vEyAkaraRA_7"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_7_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vEyAkaraRAKyAyAM caturTyAH",
    text_dev              = "वैयाकरणाख्यायां चतुर्थ्याः",
    padaccheda_dev        = "वैयाकरणाख्यायाम् चतुर्थ्याः",
    why_dev               = "(सूत्रम् 6.3.7) वैयाकरणाख्यायां चतुर्थ्याः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
