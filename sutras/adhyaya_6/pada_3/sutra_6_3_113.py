"""
6.3.113  साढ्यै साढ्वा साढेति निगमे  —  VIDHI

Padaccheda: साढ्यै साढ्वा साढा इति निगमे

साढ्यै साढ्वा साढेति निगमे (6.3.113)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_113_sAQyE_113"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_113_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.113"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.113",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sAQyE sAQvA sAQeti nigame",
    text_dev              = "साढ्यै साढ्वा साढेति निगमे",
    padaccheda_dev        = "साढ्यै साढ्वा साढा इति निगमे",
    why_dev               = "(सूत्रम् 6.3.113) साढ्यै साढ्वा साढेति निगमे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
