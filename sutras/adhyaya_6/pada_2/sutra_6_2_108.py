"""
6.2.108  क्षेपे  —  VIDHI

Padaccheda: क्षेपे

क्षेपे (6.2.108)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_108_kzepe_108"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.108", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.108"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.108",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kzepe",
    text_dev              = "क्षेपे",
    padaccheda_dev        = "क्षेपे",
    why_dev               = "(सूत्रम् 6.2.108) क्षेपे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
