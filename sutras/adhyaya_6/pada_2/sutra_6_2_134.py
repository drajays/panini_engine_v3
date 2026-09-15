"""
6.2.134  चूर्णादीन्यप्राणिषष्ठ्याः  —  VIDHI

Padaccheda: चूर्ण-आदीनि अप्राणि-षष्ठ्याः

चूर्णादीन्यप्राणिषष्ठ्याः (6.2.134)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_134_cUrRAdInya_134"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.134", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.134"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.134",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "cUrRAdInyaprARizazWyAH",
    text_dev              = "चूर्णादीन्यप्राणिषष्ठ्याः",
    padaccheda_dev        = "चूर्ण-आदीनि अप्राणि-षष्ठ्याः",
    why_dev               = "(सूत्रम् 6.2.134) चूर्णादीन्यप्राणिषष्ठ्याः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
