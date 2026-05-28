"""
6.3.135  द्व्यचोऽतस्तिङः  —  VIDHI

Padaccheda: द्वि-अचः अतः तिङः

द्व्यचोऽतस्तिङः (6.3.135)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_135_dvyacotas_135"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.135"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.135",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvyaco'tastiNaH",
    text_dev              = "द्व्यचोऽतस्तिङः",
    padaccheda_dev        = "द्वि-अचः अतः तिङः",
    why_dev               = "(सूत्रम् 6.3.135) द्व्यचोऽतस्तिङः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
