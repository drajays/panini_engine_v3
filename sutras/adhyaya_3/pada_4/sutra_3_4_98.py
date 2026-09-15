"""
3.4.98  स उत्तमस्य  —  VIDHI

Padaccheda: सः उत्तमस्य

krt-suffix rule: स उत्तमस्य
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_98_sa_98"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.98", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.98"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sa uttamasya",
    text_dev              = "स उत्तमस्य",
    padaccheda_dev        = "सः उत्तमस्य",
    why_dev               = "धातोः प्रत्ययः (३.4.98)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
