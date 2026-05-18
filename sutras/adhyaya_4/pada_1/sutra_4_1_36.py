"""
4.1.36  पूतक्रतोरै च  —  VIDHI

Padaccheda: पूतक्रतोः ऐ (लुप्तप्रथमान्तनिर्देशः) च

पूतक्रतोरै च (4.1.36)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_36_pUtakrator_36"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_36_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUtakratorE ca",
    text_dev              = "पूतक्रतोरै च",
    padaccheda_dev        = "पूतक्रतोः ऐ (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "(सूत्रम् 4.1.36) पूतक्रतोरै च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
