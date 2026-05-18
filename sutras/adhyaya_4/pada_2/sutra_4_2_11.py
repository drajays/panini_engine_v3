"""
4.2.11  पाण्डुकम्बलादिनिः  —  VIDHI

Padaccheda: पाण्डु-कम्बलात् इनिः

पाण्डुकम्बलादिनिः (4.2.11)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_11_pARqukamba_11"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_11_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.11"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.11",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pARqukambalAdiniH",
    text_dev              = "पाण्डुकम्बलादिनिः",
    padaccheda_dev        = "पाण्डु-कम्बलात् इनिः",
    why_dev               = "(सूत्रम् 4.2.11) पाण्डुकम्बलादिनिः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
