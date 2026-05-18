"""
5.3.72  कस्य च दः  —  VIDHI

Padaccheda: कस्य च दः

कस्य च दः (5.3.72)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_72_kasya_72"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_72_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kasya ca daH",
    text_dev              = "कस्य च दः",
    padaccheda_dev        = "कस्य च दः",
    why_dev               = "(सूत्रम् 5.3.72) कस्य च दः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
