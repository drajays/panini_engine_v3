"""
6.4.54  शमिता यज्ञे  —  VIDHI

Padaccheda: शमिता यज्ञे

शमिता यज्ञे (6.4.54)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_54_SamitA_54"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.54", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SamitA yajYe",
    text_dev              = "शमिता यज्ञे",
    padaccheda_dev        = "शमिता यज्ञे",
    why_dev               = "(सूत्रम् 6.4.54) शमिता यज्ञे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
