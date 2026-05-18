"""
5.4.146  ककुदस्यावस्थायां लोपः  —  VIDHI

Padaccheda: ककुदस्य अवस्थायाम् लोपः

ककुदस्यावस्थायां लोपः (5.4.146)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_146_kakudasyAv_146"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_146_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.146"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.146",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kakudasyAvasTAyAM lopaH",
    text_dev              = "ककुदस्यावस्थायां लोपः",
    padaccheda_dev        = "ककुदस्य अवस्थायाम् लोपः",
    why_dev               = "(सूत्रम् 5.4.146) ककुदस्यावस्थायां लोपः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
