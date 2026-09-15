"""
6.4.90  दोषो णौ  —  VIDHI

Padaccheda: दोषः णौ

दोषो णौ (6.4.90)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_90_dozo_90"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.90", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.90"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dozo RO",
    text_dev              = "दोषो णौ",
    padaccheda_dev        = "दोषः णौ",
    why_dev               = "(सूत्रम् 6.4.90) दोषो णौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
