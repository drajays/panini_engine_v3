"""
6.2.8  निवाते वातत्राणे  —  VIDHI

Padaccheda: निवाते वातत्राणे

निवाते वातत्राणे (6.2.8)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_8_nivAte_8"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_8_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.8"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.8",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nivAte vAtatrARe",
    text_dev              = "निवाते वातत्राणे",
    padaccheda_dev        = "निवाते वातत्राणे",
    why_dev               = "(सूत्रम् 6.2.8) निवाते वातत्राणे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
