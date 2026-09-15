"""
3.4.8  उपसंवादाशङ्कयोश्च  —  VIDHI

Padaccheda: उपसंवाद-आशङ्कयोः च

krt-suffix rule: उपसंवादाशङ्कयोश्च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_8_upasaMvAdA_8"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.8", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.8"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.8",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasaMvAdASaNkayoSca",
    text_dev              = "उपसंवादाशङ्कयोश्च",
    padaccheda_dev        = "उपसंवाद-आशङ्कयोः च",
    why_dev               = "धातोः प्रत्ययः (३.4.8)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
