"""
6.2.21  आशङ्काबाधनेदीयस्सु संभावने  —  VIDHI

Padaccheda: आशङ्क-आबाध-नेदीयस्सु संभावने

आशङ्काबाधनेदीयस्सु संभावने (6.2.21)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_21_ASaNkAbADa_21"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_21_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ASaNkAbADanedIyassu saMBAvane",
    text_dev              = "आशङ्काबाधनेदीयस्सु संभावने",
    padaccheda_dev        = "आशङ्क-आबाध-नेदीयस्सु संभावने",
    why_dev               = "(सूत्रम् 6.2.21) आशङ्काबाधनेदीयस्सु संभावने।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
