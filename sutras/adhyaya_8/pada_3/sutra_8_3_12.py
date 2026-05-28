"""
8.3.12  कानाम्रेडिते  —  VIDHI

Padaccheda: कान् (लुप्तषष्ठ्यन्तनिर्देशः) आम्रेडिते

कानाम्रेडिते (8.3.12)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_12_kAnAmreqit_12"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_12_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.12"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kAnAmreqite",
    text_dev              = "कानाम्रेडिते",
    padaccheda_dev        = "कान् (लुप्तषष्ठ्यन्तनिर्देशः) आम्रेडिते",
    why_dev               = "(सूत्रम् 8.3.12) कानाम्रेडिते।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
