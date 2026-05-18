"""
5.1.63  तद् अर्हति  —  VIDHI

Padaccheda: तत् अर्हति (क्रियापदम्)

तद् अर्हति (5.1.63)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_63_tad_63"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_63_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tad arhati",
    text_dev              = "तद् अर्हति",
    padaccheda_dev        = "तत् अर्हति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 5.1.63) तद् अर्हति।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
