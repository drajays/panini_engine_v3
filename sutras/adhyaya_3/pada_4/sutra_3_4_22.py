"""
3.4.22  आभीक्ष्ण्ये णमुल् च  —  VIDHI

Padaccheda: आभीक्ष्ण्ये णमुँल्् च

krt-suffix rule: आभीक्ष्ण्ये णमुल् च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_22_ABIkzRye_22"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.22", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ABIkzRye Ramul ca",
    text_dev              = "आभीक्ष्ण्ये णमुल् च",
    padaccheda_dev        = "आभीक्ष्ण्ये णमुँल्् च",
    why_dev               = "धातोः प्रत्ययः (३.4.22)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
