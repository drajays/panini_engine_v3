"""
6.4.167  अन्  —  VIDHI

Padaccheda: अन्

अन् (6.4.167)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_167_an_167"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.167", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.167"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.167",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "an",
    text_dev              = "अन्",
    padaccheda_dev        = "अन्",
    why_dev               = "(सूत्रम् 6.4.167) अन्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
