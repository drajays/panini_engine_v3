"""
3.4.29  कर्मणि दृशिविदोः साकल्ये  —  VIDHI

Padaccheda: कर्मणि दृशि-विदोः साकल्ये

krt-suffix rule: कर्मणि दृशिविदोः साकल्ये
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_29_karmaRi_29"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.29", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaRi dfSividoH sAkalye",
    text_dev              = "कर्मणि दृशिविदोः साकल्ये",
    padaccheda_dev        = "कर्मणि दृशि-विदोः साकल्ये",
    why_dev               = "धातोः प्रत्ययः (३.4.29)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
