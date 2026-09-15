"""
8.1.54  हन्त च  —  VIDHI

Padaccheda: हन्त च

हन्त च (8.1.54)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_54_hanta_54"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.54", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hanta ca",
    text_dev              = "हन्त च",
    padaccheda_dev        = "हन्त च",
    why_dev               = "(सूत्रम् 8.1.54) हन्त च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
