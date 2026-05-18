"""
5.4.44  प्रतियोगे पञ्चम्यास्तसिः  —  VIDHI

Padaccheda: प्रतियोगे पञ्चम्याः तसिः

प्रतियोगे पञ्चम्यास्तसिः (5.4.44)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_44_pratiyoge_44"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_44_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pratiyoge paYcamyAstasiH",
    text_dev              = "प्रतियोगे पञ्चम्यास्तसिः",
    padaccheda_dev        = "प्रतियोगे पञ्चम्याः तसिः",
    why_dev               = "(सूत्रम् 5.4.44) प्रतियोगे पञ्चम्यास्तसिः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
