"""
6.2.173  कपि पूर्वम्  —  VIDHI

Padaccheda: कपि पूर्वम्

कपि पूर्वम् (6.2.173)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_173_kapi_173"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.173", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.173"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.173",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kapi pUrvam",
    text_dev              = "कपि पूर्वम्",
    padaccheda_dev        = "कपि पूर्वम्",
    why_dev               = "(सूत्रम् 6.2.173) कपि पूर्वम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
