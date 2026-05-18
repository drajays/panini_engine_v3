"""
5.3.4  एतेतौ रथोः  —  VIDHI

Padaccheda: एत-इतौ र-थोः

एतेतौ रथोः (5.3.4)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_4_etetO_4"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_4_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.4"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "etetO raToH",
    text_dev              = "एतेतौ रथोः",
    padaccheda_dev        = "एत-इतौ र-थोः",
    why_dev               = "(सूत्रम् 5.3.4) एतेतौ रथोः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
