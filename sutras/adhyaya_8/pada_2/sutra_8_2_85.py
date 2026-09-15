"""
8.2.85  हैहेप्रयोगे हैहयोः  —  VIDHI

Padaccheda: है-हे-प्रयोगे है-हयोः

हैहेप्रयोगे हैहयोः (8.2.85)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_85_hEheprayog_85"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.85", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.85"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.85",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hEheprayoge hEhayoH",
    text_dev              = "हैहेप्रयोगे हैहयोः",
    padaccheda_dev        = "है-हे-प्रयोगे है-हयोः",
    why_dev               = "(सूत्रम् 8.2.85) हैहेप्रयोगे हैहयोः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
