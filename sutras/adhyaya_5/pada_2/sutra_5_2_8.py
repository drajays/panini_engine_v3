"""
5.2.8  आप्रपदं प्राप्नोति  —  VIDHI

Padaccheda: आप्रपदम् प्राप्नोति (क्रियापदम्)

आप्रपदं प्राप्नोति (5.2.8)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_8_AprapadaM_8"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_8_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.8"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.8",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AprapadaM prApnoti",
    text_dev              = "आप्रपदं प्राप्नोति",
    padaccheda_dev        = "आप्रपदम् प्राप्नोति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 5.2.8) आप्रपदं प्राप्नोति।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
