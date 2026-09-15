"""
6.1.174  उदात्तयणो हल्पूर्वात्  —  VIDHI

Padaccheda: उदात्त-यणः हल्-पूर्वात्

उदात्तयणो हल्पूर्वात् (6.1.174)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_174_udAttayaRo_174"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.174", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.174"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.174",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udAttayaRo halpUrvAt",
    text_dev              = "उदात्तयणो हल्पूर्वात्",
    padaccheda_dev        = "उदात्त-यणः हल्-पूर्वात्",
    why_dev               = "(सूत्रम् 6.1.174) उदात्तयणो हल्पूर्वात्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
