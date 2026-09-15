"""
3.4.57  अस्यतितृषोः क्रियाऽन्तरे कालेषु  —  VIDHI

Padaccheda: अस्यति-तृषोः क्रिया-अन्तरे कालेषु

krt-suffix rule: अस्यतितृषोः क्रियाऽन्तरे कालेषु
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_57_asyatitfzo_57"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.57", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "asyatitfzoH kriyA'ntare kAlezu",
    text_dev              = "अस्यतितृषोः क्रियाऽन्तरे कालेषु",
    padaccheda_dev        = "अस्यति-तृषोः क्रिया-अन्तरे कालेषु",
    why_dev               = "धातोः प्रत्ययः (३.4.57)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
