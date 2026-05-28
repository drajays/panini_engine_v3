"""
6.1.151  ह्रस्वाच्चन्द्रोत्तरपदे मन्त्रे  —  VIDHI

Padaccheda: ह्रस्वात् चन्द्र-उत्तरपदे मन्त्रे

ह्रस्वाच्चन्द्रोत्तरपदे मन्त्रे (6.1.151)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_151_hrasvAccan_151"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.151"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.151",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hrasvAccandrottarapade mantre",
    text_dev              = "ह्रस्वाच्चन्द्रोत्तरपदे मन्त्रे",
    padaccheda_dev        = "ह्रस्वात् चन्द्र-उत्तरपदे मन्त्रे",
    why_dev               = "(सूत्रम् 6.1.151) ह्रस्वाच्चन्द्रोत्तरपदे मन्त्रे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
