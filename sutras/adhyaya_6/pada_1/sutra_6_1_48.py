"""
6.1.48  क्रीङ्जीनां णौ  —  VIDHI

Padaccheda: क्री-इङ्-जीनाम् णौ

क्रीङ्जीनां णौ (6.1.48)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_48_krINjInAM_48"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "krINjInAM RO",
    text_dev              = "क्रीङ्जीनां णौ",
    padaccheda_dev        = "क्री-इङ्-जीनाम् णौ",
    why_dev               = "(सूत्रम् 6.1.48) क्रीङ्जीनां णौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
