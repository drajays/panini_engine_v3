"""
5.4.89  न संख्याऽऽदेः समाहारे  —  VIDHI

Padaccheda: न सङ्‍ख्या-आदेः समाहारे

न संख्याऽऽदेः समाहारे (5.4.89)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_89_na_89"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_89_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.89"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.89",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na saMKyA''deH samAhAre",
    text_dev              = "न संख्याऽऽदेः समाहारे",
    padaccheda_dev        = "न सङ्‍ख्या-आदेः समाहारे",
    why_dev               = "(सूत्रम् 5.4.89) न संख्याऽऽदेः समाहारे।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
