"""
6.3.39  वृद्धिनिमित्तस्य च तद्धितस्यारक्तविकारे  —  VIDHI

Padaccheda: वृद्धि-निमित्तस्य च तद्धितस्य अरक्तविकारे

वृद्धिनिमित्तस्य च तद्धितस्यारक्तविकारे (6.3.39)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_39_vfdDinimit_39"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vfdDinimittasya ca tadDitasyAraktavikAre",
    text_dev              = "वृद्धिनिमित्तस्य च तद्धितस्यारक्तविकारे",
    padaccheda_dev        = "वृद्धि-निमित्तस्य च तद्धितस्य अरक्तविकारे",
    why_dev               = "(सूत्रम् 6.3.39) वृद्धिनिमित्तस्य च तद्धितस्यारक्तविकारे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
