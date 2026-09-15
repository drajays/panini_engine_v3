"""
6.2.50  तादौ च निति कृत्यतौ  —  VIDHI

Padaccheda: त-आदौ च न्-इति कृति अतौ

तादौ च निति कृत्यतौ (6.2.50)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_50_tAdO_50"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.50", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tAdO ca niti kftyatO",
    text_dev              = "तादौ च निति कृत्यतौ",
    padaccheda_dev        = "त-आदौ च न्-इति कृति अतौ",
    why_dev               = "(सूत्रम् 6.2.50) तादौ च निति कृत्यतौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
