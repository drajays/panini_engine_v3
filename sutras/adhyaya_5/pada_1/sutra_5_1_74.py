"""
5.1.74  योजनं गच्छति  —  VIDHI

Padaccheda: योजनम् गच्छति (क्रियापदम्)

योजनं गच्छति (5.1.74)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_74_yojanaM_74"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_74_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.74"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yojanaM gacCati",
    text_dev              = "योजनं गच्छति",
    padaccheda_dev        = "योजनम् गच्छति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 5.1.74) योजनं गच्छति।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
