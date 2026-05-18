"""
6.2.94  संज्ञायां गिरिनिकाययोः  —  VIDHI

Padaccheda: संज्ञायाम् गिरि-निकाययोः

संज्ञायां गिरिनिकाययोः (6.2.94)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_94_saMjYAyAM_94"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_94_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAM girinikAyayoH",
    text_dev              = "संज्ञायां गिरिनिकाययोः",
    padaccheda_dev        = "संज्ञायाम् गिरि-निकाययोः",
    why_dev               = "(सूत्रम् 6.2.94) संज्ञायां गिरिनिकाययोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
