"""
4.4.82  संज्ञायां जन्याः  —  VIDHI

Padaccheda: संज्ञायाम् जन्याः

संज्ञायां जन्याः (4.4.82)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_82_saMjYAyAM_82"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_82_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.82"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.82",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAM janyAH",
    text_dev              = "संज्ञायां जन्याः",
    padaccheda_dev        = "संज्ञायाम् जन्याः",
    why_dev               = "(सूत्रम् 4.4.82) संज्ञायां जन्याः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
